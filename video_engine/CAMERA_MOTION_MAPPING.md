# Camera Motion Mapping

## Director intent vocabulary
- locked-off / static
- pan left/right
- tilt up/down
- push in / pull out
- roll clockwise / counter-clockwise
- truck / orbit / crane / handheld / shake

## Native WanCameraEmbedding mapping found in ComfyUI 0.33.0
Available camera poses:
- Static
- Pan Up
- Pan Down
- Pan Left
- Pan Right
- Zoom In
- Zoom Out
- Anti Clockwise (ACW)
- ClockWise (CW)

and an explicit `speed` input from 0 to 10.

## Mapping discipline
- `static` -> Static
- `pan_left/right` -> Pan Left / Pan Right
- `tilt_up/down` -> Pan Up / Pan Down (the node names are Pan Up/Down; do not rename them in binding)
- `push_in` -> may map to Zoom In **only when creative intent accepts the approximation**
- `pull_out` -> may map to Zoom Out under the same condition
- `roll` -> CW / ACW

## Important
A real dolly move and a zoom are not cinematographically identical.
The Skill must not silently equate them.
If the requested move is not represented by the current workflow, output `CAMERA_CONTROL_UNBOUND` and either:
- simplify the move,
- express it in prompt/motion language,
- or select a workflow with stronger camera control.
