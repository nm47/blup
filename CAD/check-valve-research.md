# Check valve selection — 2026-09-07

## Confirmed baseline and operating arrangement

The user reports that `prints/test_with_oring.stl` screws on perfectly and
appears watertight. Preserve its bottle threads, internal groove overrun, and
bottle-mouth O-ring geometry. A FreeCAD copy was saved as
`baselines/cap_fit_oring_pass_20260907.FCStd`.

The user plans a drilled vent at the top of the inverted bottle. It must
communicate with the headspace above the liquid during operation. With an open
vent, the pump-off reverse pressure is principally the liquid head. For a
water-density liquid 0.30 m deep, rho*g*h is approximately 2.94 kPa / 0.43 psi.
That height and density are estimates, not measurements of the intended fill.

The valve permits air from the pump into the bottle and blocks liquid returning
toward the pump. The current central cap hole is a 5 mm placeholder.
Exact liquid formulation and filled storage duration remain pending.
The valve must be hidden: the user rejects hardware protruding visibly into
the glass bottle. Their initial prototype placed the valve body in the bottle
with one end through the cap, sealed with silicone caulk. Its model is pending.

## Proposed mounting

### Accepted direction — 2026-09-08

**Current live placement — inside cap:** user approved trying the interior
position to save vertical space. Applied rotation X = 180 degrees and translation
`(0, 0, 4.58724)` mm to `CheckValveReference`, placing
`Part__Feature001.Face17` on the internal floor at z = 0. The inlet now extends
6.796 mm below the cap underside, saving 10.898 mm compared with the previous
underside-face trial. The outlet reaches 12.970 mm above the skirt edge.
Boolean checks show zero glass or bottle O-ring overlap and unchanged cap
geometry. The remaining 1.528 mm³ overlap around the inlet neck requires a
clearance recess; the gasket and retainer remain undesigned. Cap transparency
is 65% and bottle transparency 85% for inspection. Saved in `blüp.FCStd`;
backup: `baselines/before_interior_valve_trial_20260908_110144.FCStd`.

**Compression concept checked:** user accepts the visible protrusion in the
interior trial. Use a separate annular retaining ring that passes over the
upper outlet and screws onto a raised threaded collar around the valve body,
integrated with the cap floor. Its inward lip presses the upper rigid annular
face (`Part__Feature.Face17`, currently z = 5.89788 mm, OD 17.653 / ID 9.93775)
to compress a gasket beneath the lower housing face. Add a geometric stop to
control final gasket squeeze. The printed support must originate within the
central area inside the bottle O-ring groove; any outward widening must clear
the O-ring. A read-only provisional 27 mm OD retaining-ring envelope at z =
1..8.5 mm had zero glass/O-ring overlap. The modeled glass bore is 29.3 mm,
giving 1.15 mm nominal radial clearance at that diameter. This establishes
space for the concept, not finished thread, support-wall or gasket dimensions.

**Prior interior-mount evaluation (now applied above):** user says the current
2.1 mm protrusion is acceptable and suggests an approximately 18 mm limit;
the reference edge for that limit was asked for and remains pending. The user
is open to the valve body being inside the cap. A read-only geometry trial
with the opposite annular face resting on the internal floor uses rotation
X = 180 degrees and translation z = 4.58724 mm. Its gasket contact face is
`Part__Feature001.Face17`, OD 17.653 mm / ID 6.858 mm. With no gasket allowance,
the top tip reaches 12.970 mm above the skirt edge (20.970 mm above the internal
floor), and the bottom tip reaches 6.796 mm below the underside. There is zero
overlap with the modeled glass. The valve body is smaller than the 22.8 mm
central area inside the bottle O-ring groove. A small relief is still required
around the cap hole (1.528 mm³ cap overlap in this trial).

Proposed retention for this alternative: a removable ring above the rigid
valve housing clamps its lower annular face onto a captured gasket in the cap
floor, with a hard stop controlling compression. This needs a dimensional
design check for the ring, threads and clearance from the bottle seal; it is
not a completed mounting design. A compressed gasket or raised seat shifts
the valve upward and consumes additional protrusion allowance. This evaluation
preceded the interior placement now applied above.

**Previous underside face-contact trial:** per the user's correction of flow orientation,
`CheckValveReference` is rotated 180 degrees about X and centered on the cap
axis, at placement translation `(0, 0, -6.31064)` mm. The former lower annular
face of housing part 1 (`Part__Feature.Face17`) now faces upward at z = -5 mm,
coplanar with the cap underside. Its annulus is OD 17.653 mm / ID 9.93775 mm.
This face fits within the cap's central region, but the tapered neck intersects
the existing cap around its 5 mm hole (17.513 mm³ overlap). A matching relief
and gasket allowance are still needed; this placement is a trial, not an
assembled interference-free fit. The upper barb tip is at z = 10.07236 mm,
10.072 mm above the internal floor and 2.072 mm above the current skirt top.
The lower tip is at z = -22.69364 mm, 17.694 mm below the cap underside.
Cap solid geometry was verified unchanged. Base/cap are visible and the test
ring is hidden for inspection; the FreeCAD document is saved. Backup:
`baselines/before_valve_face_trial_20260908_105313.FCStd`.

**STEP imported:** user supplied `47245K115_Check Valve.STEP`, imported into
the active `blüp.FCStd` as the separate root part `CheckValveReference`
(label: `Check valve — McMaster 47245K115 (reference)`). The source contains
two valid housing solids. Envelope is **19.431 x 19.177 x 32.766 mm**;
use this source geometry instead of the catalog's rounded 31.75 mm length.
The reference is parked beside the cap with its upper tip at z = -5 mm;
this is an inspection position, not an installed mounting or verified flow
orientation. Source path and envelope are stored as object properties.
The model was saved after import; Boolean comparison confirms the cap
geometry is unchanged. A pre-import copy is in
`baselines/before_valve_import_20260908_104825.FCStd`.
The exact pocket, valve-body sealing land and retainer are still to be designed.
An axial installation with the outlet tip at z = 0 would extend 27.766 mm
below the current floor's underside before additional clearance.

User approved a hose-barbed valve, recessed from underneath, with a separate
captured gasket against a suitable rigid body shoulder and an underside
retainer. Pump tubing connects directly to the inlet barb. Favor minimal
overall depth; neither barb ridges nor a rigid printed hole alone supply the
cap seal. This replaces the cartridge-first sourcing preference below.

Current fit candidate: **McMaster 47245K115**, clear polycarbonate body,
silicone diaphragm/seal, barbs for 1/8-inch (3.175 mm) ID tubing, 0.5 psi
opening pressure, listed for air and water, catalog overall length 1.25 inches
(31.75 mm). Soap compatibility and low-head reverse leakage remain unverified.
[Part](https://www.mcmaster.com/47245K115/)
[Catalog specifications](https://www.mcmaster.com/products/duckbill-valves/)

Live FreeCAD inspection confirmed cap floor 5 mm, OD 43 mm, current inlet hole
5 mm, and bottle O-ring groove OD 33.6 mm / width 5.4 mm / depth 3 mm. With the
valve axial and its outlet tip no higher than the liquid-facing floor, at least
26.75 mm of valve extends below the floor's underside, before any additional
clearance. A horizontal arrangement may reduce depth but requires the actual
body diameter and fitting envelope. Do not use the 2141N4 drawing as an exact
model for this other part. The product's dynamic page did not yield a STEP or
dimension drawing through the available retrieval; precise mounting is pending
that file or a measured sample. No geometry edits made.

Revised proposal: place a replaceable manufactured valve in a pocket entered
from beneath the cap. Leave only a small flush air outlet in the liquid-facing
floor. Add any required housing depth beneath the cap, outside the visible
bottle interior. This supersedes a protruding liquid-side bulkhead flange.

With a suitable rigid valve shoulder, a captured face gasket/O-ring seals it
against the underside of the pocket roof. An annular retaining plug threads
into a boss on the underside of the cap and supports the valve body. The air
inlet passes through the plug. The plug threads engage the cap housing, not the
valve. Provide a hard compression stop and do not load flexible valve lips.
Actual valve geometry may instead require a separate sleeve/cartridge to supply
the sealing shoulder. Final dimensions require a manufacturer mounting drawing.

The current 5 mm cap floor need not contain the entire valve; extra length can
extend downward. Keep the successful bottle threads and mouth seal unchanged.
No valve geometry has been added to the FreeCAD model yet.

## Candidates, not qualified selections

### Direct-order sourcing update — 2026-09-08

User prioritizes direct ordering in small quantities and minimal installed
depth. Quote-only suppliers are not preferred. No purchase has been made.

- **ISM CRTG-EPDM-PP-.5** is the leading direct-order cartridge to evaluate:
  5/8-inch (15.875 mm) diameter, polypropylene body/poppet, EPDM seal,
  0.5 psi cracking pressure. Live product HTML displayed $7.78 each, 13
  available, and Add to Cart. Its length and low-head liquid leakage are not
  established. The linked `crtg-series.PDF` returned a Magento placeholder
  JPEG, not a usable dimension drawing. No STEP was found. Obtain a physical
  sample or correct drawing before committing mounting geometry. The EPDM
  internal seal does not automatically seal the cartridge to our housing.
  [Direct product listing](https://www.industrialspec.com/shop/check-valves/modular/crtg/crtg-epdm-pp-05.html)
  [Cartridge family](https://www.industrialspec.com/shop/check-valves/modular/crtg.html)
- **McMaster 2141N4**: 25.4 mm overall length, female Luer inlet and outlet,
  polycarbonate housing, silicone diaphragm/seal, 0.5 psi opening pressure,
  listed for air and water. Consider only as a packaged-valve alternative;
  fittings add space and low-pressure soap leakage is unqualified. Catalog
  listing was accessible, but the individual page failed through the browser;
  exact price, stock and STEP availability were not confirmed.
  [Part page](https://www.mcmaster.com/2141N4/)
  [Supporting catalog table](https://www.mcmaster.com/products/duckbill-valves/)
- **ISM CVT-18VL / displayed product code V130022100**: listed $8.16 each,
  208 available. Approximately 27.7 mm long and 12.2 mm maximum diameter in
  its 2025 reference drawing; older technical sheet gives a maximum length
  28.24 mm. Acrylic housing, silicone duckbill, smooth 3.3 mm tube ends.
  Its water backflow audit permits 1 mL/hour at a 203 mm water head—up to
  24 mL/day under that test. Do not select it as a guaranteed leak-free
  storage barrier. Mean air cracking pressure is 4.5 mbar at 25 mL/min;
  this is a flow-threshold measurement, not a guaranteed opening limit.
  [Product](https://www.industrialspec.com/shop/check-valves/plastic-check-valves/duckbill/cvt-series-duckbill-check-valve/cvt-18vl.html)
  [Performance data](https://www.industrialspec.com/shop/media/catalog/product/pdf/CVT-18VL_Technical.pdf)
  [2025 drawing](https://www.industrialspec.com/shop/media/catalog/product/pdf/CVT-18VL_07092025.pdf)
  Both valid PDFs saved under `reference/check-valves/`.

Other investigated parts did not improve the shortlist: Vernay V246110200
is sold in 500-piece lots; the Air Logic floating-disk drawing specifies clean,
dry gases; Clippard MCV-1 lists air as its medium. No better documented small
liquid-compatible candidate was found at DigiKey, Mouser or Amazon in this pass.

An alternative packaging concept is a horizontal valve beneath the cap with
a short passage turning upward to the flush outlet. That trades lateral area
for height; its fittings, passage, retained liquid and housing still need a CAD
fit check. Do not equate bare valve diameter with final assembly depth.

### Earlier manufacturer candidates

- **Smart Products Model 502:** inline valve for 1/8-inch-ID (3.18 mm) tubing.
  Polypropylene body and EPDM seal are offered; available opening spring
  pressures start at 0.09 psi. This is the first candidate for a modular bench
  prototype. Specify the actual compound and spring pressure with the supplier;
  compatibility, required airflow and reverse liquid leakage remain unverified.
  Price, stock and minimum order are not confirmed.
  [Manufacturer specifications](https://smartproducts.com/series-500-check-pressure-relief-valves/)
- **Minivalve DU047.001:** sleeved duckbill, 7 mm tall, effective diameter
  4.7 mm, published opening differential 0.185 kPa. It is a compact integration
  candidate, requiring enough clearance for its flexible outlet inside the
  recessed liquid passage. Effective diameter is not a mounting-hole dimension: obtain the
  seating drawing and exact elastomer before designing the insert. Its published
  750+ kPa back-pressure rating does not establish leakage at our much lower
  pressure. Flow and seating information require access on the supplier site;
  no request or order has been submitted.
  [Manufacturer specifications](https://minivalve.com/products/catalog-valves/du-047-001/)

Neither public specification establishes months of zero leakage with this
project's soap solution. Valve resealing, debris, material interaction and
opening after inactivity matter as well as nominal cracking pressure.
[Manufacturer operating guidance](https://smartproducts.com/technical-resources/check-valve-operation/)

## Qualification before committing the cap design

1. Identify the liquid, intended fill height, temperature range and storage
   duration. Obtain low-reverse-pressure liquid leakage data and wetted-material
   compatibility for the specific valve configuration.
2. Test the valve independently with the actual solution and maximum intended
   liquid head, headspace vented. Leave the pump-side port open into a collection
   vessel so trapped air cannot hide a leak. Also test a shallow fill, since a
   reduced reverse pressure may provide less assistance to sealing.
3. Run an initial week-long collection test, then extend to the intended storage
   duration. Account for evaporation when measuring small volumes or masses.
   An example liquid leak of 1 microlitre/minute accumulates 43.2 mL in 30 days.
4. Repeat after pumping cycles, prolonged soaking and representative drying;
   verify the first opening after inactivity and usable bubble flow. Pump
   pressure must exceed liquid head plus valve and other flow losses; current
   readings alone do not establish available pump pressure.
5. Test the mounting seal separately with the flow passage plugged, then test
   the complete installed assembly. Record volume collected, duration, fill
   head and solution rather than relying only on visual dryness.
