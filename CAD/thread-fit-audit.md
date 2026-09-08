# Bottle thread fit audit — 2026-09-07

## Successful physical fit — preserve this baseline

- User printed `prints/test_with_oring.stl`, a byte-identical copy of
  `prints/collar_p3.5_w2.5_s2.2_rad0.3_ax0.2_overrun1.stl`.
- User reports the cap now screws on perfectly and appears watertight with the
  O-ring. This is a successful fit observation, not a quantified pressure or
  long-duration leakage test.
- Tested STL SHA-256:
  `101635f5eb58a39d5f9801eb51fa3a8734bf58f81a1fd392a0a97d91383e2a80`.
- Preserve the thread geometry, one-turn internal overrun, and bottle-mouth seal
  while designing the central check-valve mounting. Its body seal and reverse
  leakage are separate from the now-successful bottle/cap fit.

## Current revision: extend the internal groove past its deep end

- User reports seeing the glass thread reach the end of the internal groove,
  push past it, and tilt the cap. This is the current physical failure hypothesis.
- The modeled internal groove had a closed end face at the sealing-face end,
  spanning z=1.8542–4.7542 mm with only 15° of extension before the nominal glass
  thread start. The entry at the open rim was already cut through.
- Added `BaseParams.ThreadOverrunTurns = 1.0`. Both internal profiles now begin
  one full lead (3.5 mm) deeper, and both cutting helices gain one turn to retain
  their existing upper extent. `ThreadLeadIn` remains 15°; pitch, profile,
  radial clearance, and axial clearance are unchanged. Use the new float
  property for whole-turn extension: the existing angle property caps at 360°.
- The new closed end spans z=-1.6458–1.2542 mm, entirely below the modeled glass
  thread, whose lowest point when seated is z=2.2 mm. This gives about 0.946 mm
  separation from the end wall at the intended seated position. The groove still
  has a finite end; it has been moved out of the bottle thread's seating path.
- The extension removes material around the outer edge of the floor, leaving
  at least 3.354 mm beneath its lowest point. Solid comparisons confirm the
  sealing land, O-ring groove, and supporting floor within bottle-mouth radius
  17.5 mm are unchanged. The entire floor is therefore not unchanged, but its
  sealing region is preserved. No material was added to the cap.
- Bottle and O-ring geometry are unchanged. Cap and ring remain valid single
  solids; the ring still matches the cap above z=0. Nine aligned screw-path
  positions have zero overlap. Both exported meshes are closed.
- **Next print: the full cap**, to check whether the sealing face stops travel
  before the glass thread can reach the groove end:
  `prints/collar_p3.5_w2.5_s2.2_rad0.3_ax0.2_overrun1.stl`.
  Matching ring: `prints/thread_test_ring_p3.5_w2.5_s2.2_rad0.3_ax0.2_overrun1.stl`.
  A floorless ring has no seating stop and can be advanced beyond the cap's
  intended seating position, so it cannot validate that stopping behavior.
- Subsequent physical test succeeded as recorded above. The earlier aligned CAD
  checks alone did not predict the observed end-stop failure.

## Reference after bottle measurements

- User confirms approximately 3.5 mm pitch and approximately 2.5 mm thread width
  on the glass bottle, with a noticeably round profile. Only the 3.5 mm previous
  test ring was tried; the original VOSS cap seats squarely.
- User subsequently measured approximately 2.2 mm from the bottle mouth to the
  start of the thread, replacing the 3.0 mm estimate. Updated `ThreadParams.LipOffset`
  to 2.2 mm; the bottle, cap, and test-ring thread profiles all follow this parameter.
  The skirt remains 8 mm tall with 2 mm clearance below the neck bead.
- User observes the thread end close to the start around the circumference and
  almost merged into the bead after two loops. Updated `ThreadParams.Turns` from
  1.75 to a provisional 2.0, retaining the single-start assumption. At two turns,
  the ending profile spans 9.2–11.7 mm from the mouth, while the bead starts at
  10 mm, so much of that profile lies within the bead.
- This added 28.83 mm³ to the bottle reference. Solid comparisons found zero
  geometry change to the cap or open ring: their rims stop at 8 mm, before the
  extra quarter-turn. Four additional aligned screw-path checks pass. The `s2.2`
  STLs listed below remain current and were not regenerated for this change.
- Further user comparison indicates approximately another eighth-turn before
  the thread merges. Current `ThreadParams.Turns` is therefore **2.125**, still
  an approximate observation. The ending profile spans 9.6375–12.1375 mm from
  the mouth; the bead begins at 10 mm. A small portion of the idealized rounded
  profile can still project below the bead at its endpoint. This turn-count
  adjustment does not reshape the idealized bead or add a blended runout.
  Cap and test-ring solid comparisons again show zero geometry difference, so
  the same `s2.2` STLs remain current.
- Updated `ThreadParams.ThreadWidth` from 2.0 to 2.5 mm and `CrestRadius` from
  0.8 to 1.0 mm. The radius is a provisional rounded-profile approximation,
  not a measured radius. Pitch remains 3.5 mm and radial clearance remains 0.3 mm.
- Reduced axial clearance from 0.5 to 0.2 mm per flank. Retaining the old value
  with a 2.5 mm thread would make the groove 3.5 mm wide, equal to the pitch.
  The revised groove is 2.9 mm wide, leaving a 0.6 mm minimum axial crest.
- Added `TestRingEntryRelief` using the same parameters as the cap's entry relief.
  A solid comparison verifies that the open ring exactly reproduces the cap's
  geometry above the sealing plane. It is 8 mm tall, with no floor or seal.
- Bottle, cap, and ring are valid single solids. Eight aligned screw-path samples
  per printed part have zero modeled overlap. The cap's floor and sealing groove
  are unchanged. Both exported meshes are closed, using 0.03 mm linear and
  0.15 rad angular mesh deflection, placed with their bottoms at z=0.
- **Not a confirmed fix:** the revised bottle also has zero seated overlap with
  the prior cap shape. A width correction alone has therefore not reproduced the
  physical failure in CAD. Actual profile, print dimensions, engagement, and
  thread-start count remain fit-test inputs.
- Prints at this earlier stage:
  `prints/thread_test_ring_p3.5_w2.5_s2.2_r1.0_rad0.3_ax0.2_relief2.stl` and
  `prints/collar_p3.5_w2.5_s2.2_r1.0_rad0.3_ax0.2_relief2.stl`.
  The `s2.2` identifies the corrected thread-start distance. The preceding exports
  without `s2.2` retain the old 3.0 mm start distance.
  These supersede the previous print for the next trial, not its failure record.

## Physical observations

- User reports that the printed PLA cap bends unevenly as it screws onto the real
  bottle. One half remains flat while the other bends upward.
- This also happened with the earlier open test ring, before a floor existed,
  and occurs with and without the O-ring. Floor or seal reinforcement is therefore
  not the next diagnostic change.
- Only the 3.5 mm pitch ring was tried. Its exact clearance variant is unspecified.
  The original VOSS cap seats squarely on the same bottle.

## Baseline audit before the new width measurement

- Source: live `CAD/blüp.FCStd`, collar tip `ThreadEntryRelief`.
- Project notes record caliper measurements of bottle thread crest diameter
  37 mm and root diameter 35 mm. They describe the 3.5 mm pitch, single start,
  1.75 turns, 2 mm thread width, 0.8 mm crest corner radius, and 3 mm thread-start
  offset as estimates, not validated physical thread specifications.
- Bottle and cap helices both use `ThreadParams.Pitch * ThreadParams.Starts`.
  Agreement between these two modeled parts establishes internal consistency,
  not agreement with the real glass thread.
- The cap uses 0.3 mm radial clearance: nominal bore diameter 35.6 mm and groove
  maximum diameter 37.6 mm. Axial clearance is 0.5 mm on each flank, giving a
  3.0 mm groove width at its opening and a minimum 0.5 mm axial thread crest
  between successive turns at the current 3.5 mm pitch. This is a local crest
  dimension, not the thickness of the complete thread support or cap wall.
- The single-start helices and their reversal/assembly orientation passed the
  earlier sampled aligned screw-path collision checks. Those checks do not
  simulate deformation, contact forces, print errors, or a different real thread.
- `Starts` currently changes helix lead only. There are no repeated, angularly
  offset helices. If the real bottle has multiple starts, setting that parameter
  alone would not create the required geometry.
- All five original test-ring STLs load as closed meshes. They are 43 mm nominal
  outer diameter and 8 mm high. Their names encode pitches 3.3/3.5/3.7 mm with
  radial/axial clearances 0.3/0.5 mm, plus 3.5 mm variants at 0.2/0.3 and 0.4/0.7.
  Mesh closure does not establish thread accuracy or fit.

## Prior cap revision

The face-stop cap has a 2 mm gap below the modeled neck bead and a 2 mm-deep
tapered entry relief (radius 17.8 mm at z=6 to 19.8 mm at z=8). Its sealing face
is at z=0, floor thickness is 5 mm, and the O-ring groove is 3 mm deep. The latest
print is `prints/collar_face_stop_gap2_relief2.stl`. This revision did not resolve
the reported bending; do not describe it as a validated fit.

## Next diagnostic steps

1. Test the new `overrun1` full cap for square engagement and seating without the
   groove end lifting the cap. Record the result against its exact filename.
   Inspect it for permanent distortion first; then test O-ring compression/sealing.
2. Confirm thread-start count, which remains assumed to be one. The user has
   now measured approximately 3.5 mm spacing. Adjacent interleaved starts must not
   be mistaken for successive turns of one helix; lead equals pitch times starts.
3. Compare the printed ring's bore and thread profile against the model and bottle.
   Pitch/lead mismatch, profile mismatch, print dimensional error, or incorrect
   engagement remain hypotheses; the present observations do not select one.
4. Set the bottle reference from measurements, then vary cap fit independently,
   changing one quantity at a time. Avoid treating extra clearance as a substitute
   for a correct lead/profile; it also reduces retained thread material.

The successful profile is saved in `blüp.FCStd`; check-valve integration is next.
