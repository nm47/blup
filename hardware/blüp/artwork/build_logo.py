"""Build the outlined blüp wordmark and its mirrored KiCad import artwork.

Requires Shapely. All lettering is original vector geometry; no fonts required.
"""
from pathlib import Path
from math import cos, sin, pi
import json

from shapely import affinity
from shapely.geometry import LineString, Point, box
from shapely.ops import unary_union, split

OUT = Path(__file__).parent


def arc(x, y, radius, start, end, width):
    steps = max(16, int(abs(end - start) * 0.8))
    points = [(x + radius * cos((start + (end-start)*i/steps)*pi/180),
               y + radius * sin((start + (end-start)*i/steps)*pi/180))
              for i in range(steps + 1)]
    return LineString(points).buffer(width / 2, quad_segs=12)


def line(points, width):
    return LineString(points).buffer(width / 2, quad_segs=12)


def bubble(x, y, r, width=3.5, opening=False):
    ring = arc(x, y, r, 17 if opening else 0, 347 if opening else 360, width)
    highlight = arc(x, y, r * (0.48 if r < 12 else 0.64), 188, 266,
                    width * (0.75 if r < 12 else 0.9))
    return unary_union([ring, highlight])


# Layered bubbles: the foreground bubble cleanly occludes the one behind it.
rear = bubble(136, 18, 20, opening=True)
rear = rear.difference(Point(105, 38).buffer(28.7, quad_segs=96))
main = bubble(105, 38, 27, 4.0)
main = main.difference(Point(105, 67).buffer(18.2, quad_segs=96))
front = bubble(105, 67, 16.5, 3.5, opening=True)
cluster = unary_union([
    rear, main, front,
    bubble(63, 12, 11, 3.0),
    bubble(119, -17, 7, 2.5),
    bubble(148, 69, 9.5, 3.0),
])

# Rounded lowercase wordmark. b/p bowls match, and the umlaut dots are bubbles.
w = 8.8
b = unary_union([line([(5, 43), (5, 109)], w), arc(25, 89, 20, 0, 360, w)])
l = unary_union([line([(70, 43), (70, 98)], w),
                 arc(81, 98, 11, 90, 180, w), line([(81, 109), (83, 109)], w)])
u = unary_union([line([(106, 69), (106, 89)], w),
                 arc(126, 89, 20, 0, 180, w), line([(146, 69), (146, 109)], w)])
p = unary_union([line([(176, 69), (176, 136)], w), arc(196, 89, 20, 0, 360, w)])
umlaut = unary_union([arc(115, 48, 4.1, 0, 360, 2.8),
                      arc(137, 48, 4.1, 0, 360, 2.8)])
word = affinity.translate(unary_union([b, l, u, p, umlaut]), yoff=52)
logo = unary_union([cluster, word])
x0, y0, x1, y1 = logo.bounds
logo = affinity.translate(logo, xoff=-x0, yoff=-y0)
width, height = x1-x0, y1-y0


def polygons(g):
    if g.geom_type == 'Polygon':
        return [g]
    return [p for child in g.geoms for p in polygons(child)]


def without_holes(poly):
    if not poly.interiors:
        return [poly]
    # Split across one counter at a time. This preserves empty letter centers
    # even in importers that treat every closed SVG subpath as a filled shape.
    inner = poly.interiors[0]
    ys = [y for x, y in inner.coords]
    cut_y = (min(ys) + max(ys)) / 2
    pieces = split(poly, LineString([(-1000, cut_y), (1000, cut_y)]))
    return [part for piece in pieces.geoms for part in without_holes(piece)]


def path(points):
    return 'M' + ' L'.join(f'{x:.5f},{y:.5f}' for x, y in points) + ' Z'


def artwork(g, fill='#111111', simple=False):
    result = []
    for polygon in polygons(g):
        for part in without_holes(polygon) if simple else [polygon]:
            d = path(part.exterior.coords)
            for interior in part.interiors:
                d += ' ' + path(interior.coords)
            result.append(f'<path fill="{fill}" fill-rule="evenodd" d="{d}"/>')
    return '\n'.join(result)


def svg(g, fill='#111111', simple=False):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="40mm" '
            f'height="{40*height/width:.5f}mm" viewBox="0 0 {width:.5f} {height:.5f}">\n'
            '<title>blüp — bubble wordmark</title>\n' + artwork(g, fill, simple) + '\n</svg>\n')


(OUT/'blup-logo.svg').write_text(svg(logo))
# B.SilkS polygons use board coordinates: reflect once here, so the back reads normally.
mirrored = affinity.scale(logo, xfact=-1, yfact=1, origin=(width/2, height/2))
(OUT/'blup-logo-back.svg').write_text(svg(mirrored))
# Konnect 0.11.1's live importer keeps only one outer contour per call and
# ignores the SVG viewBox transform. Use one hole-free path per SVG, with
# numeric viewport dimensions equal to its coordinate system.
parts_dir = OUT/'konnect-parts'
parts_dir.mkdir(exist_ok=True)
for i, part in enumerate([part for p in polygons(mirrored) for part in without_holes(p)], 1):
    (parts_dir/f'part-{i:02}.svg').write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.5f}" '
        f'height="{height:.5f}" viewBox="0 0 {width:.5f} {height:.5f}">'
        + artwork(part) + '</svg>\n')
(OUT/'blup-logo-preview.svg').write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1000" viewBox="-45 -46 310 310" style="background:#153f32">'
    '<rect x="-45" y="-46" width="310" height="310" fill="#153f32"/>'
    + artwork(logo, '#f7f5e8') + '</svg>')
(OUT/'logo-metadata.json').write_text(json.dumps({
    'width_mm': 40, 'height_mm': 40*height/width,
    'board_layer': 'B.SilkS', 'board_x_mm': 115,
    'board_y_mm': 95 - 20*height/width,
    'mirror_for_back': True, 'fonts_required': False,
    'smallest_stroke_mm': 2.5*0.75*40/width,
    'import_polygon_count': sum(len(without_holes(p)) for p in polygons(logo)),
}, indent=2) + '\n')
print((OUT/'logo-metadata.json').read_text())
