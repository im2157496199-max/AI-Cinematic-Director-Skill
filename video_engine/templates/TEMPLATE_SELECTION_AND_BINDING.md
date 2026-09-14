# Template Selection & Binding

## Inputs
- `video_shot_plan`
- approved still reference
- optional approved end still
- required capabilities
- user's verified workflow registry
- hardware/runtime constraints if known

## Selection score
Reject before scoring if:
- not run-verified when production execution is requested,
- required input type unavailable,
- required control capability unavailable,
- dependency state is unresolved and blocks execution.

Then prefer:
1. exact capability fit,
2. user-run-verified profile,
3. fewer unnecessary controls,
4. stable/core dependency surface,
5. known API binding,
6. regression-tested profile.

Do not prefer a more complex template merely because it has more nodes.

## Semantic capability vocabulary
- `image_to_video`
- `first_last_frame`
- `camera_control`
- `pose_or_control_video`
- `identity_reference`
- `audio_conditioning`
- `provider_api`
- `local_open_weight`

## Binding target
All automatic patching targets the **verified API-format export**.
UI template controls are discovery evidence only.

## Mutable fields
Common candidates:
- positive prompt,
- negative prompt,
- source image,
- end image,
- width/height if explicitly exposed and workflow-valid,
- frame length,
- fps,
- seed,
- camera/control enum if explicitly exposed.

Model filenames, samplers, scheduler topology, VAE, LoRA chains and hidden subgraph internals stay locked by default unless the profile explicitly marks them mutable.

## Unbound behavior
If the director plan requires an unavailable control:
- return `UNBOUND_CAPABILITY`,
- name the missing capability,
- propose a safe creative simplification or another **registered** template.

Never invent node IDs or class types to make the report look complete.
