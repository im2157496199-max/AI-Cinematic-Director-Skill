# Control and Keyframe Patterns

## First + last frame

Two source workflows implement the same creative requirement with different graph mechanics:

- `First Last Frame (guide node)`
- `First Last Frame (in-place node)`

Both expose semantic anchors for:

- `firstframe`
- `lastframe`
- width / height / frames / fps
- positive / negative conditioning
- final video / final audio

### Director interpretation

Use first+last control when the **start and end visual states are both non-negotiable**. Examples:

- character begins facing camera and must finish profile-left;
- an object must start closed and finish open;
- a camera move must land on a specific final composition.

Do not use it simply because “more control sounds better.” Extra keyframe constraints can reduce motion freedom and add failure points.

## First + middle + last frame

The `First Middle Last Frame (guide node)` workflow adds `Set_middleframe` and uses an observed midpoint calculator (`ceil(a/2)` appears in the UI graph).

### Director interpretation

Use three-keyframe control when the middle beat itself carries narrative information:

```text
start: sword lowered
middle: blade at contact point
end: follow-through pose
```

If the middle frame is only an interpolation convenience, prefer first+last or basic I2V to avoid over-constraining.

## Pose IC-Control

`I2V IC-Control (pose)` adds:

- pose preprocessing (`DWPreprocessor` observed)
- pose reference semantic anchors
- IC-LoRA branches
- optional detail/control LoRAs
- additional switching/performance nodes

The source note explicitly states that the pose IC LoRA must be enabled for pose-video input; the detailer LoRA is optional.

### Director interpretation

Pose control is for **body choreography**, not identity. Identity remains anchored by the approved still/entity system. A pose video can control skeleton/motion while still failing face/wardrobe consistency; those are separate QA dimensions.

## All-in-one pose + canny + depth

The largest studied graph (`164` nodes) exposes separate anchors for:

- `ref_pose`
- `ref_canny`
- `ref_depth`
- `ref_control`
- corresponding audio/control branches
- I2V/T2V mode switch

### Meaning of the controls

- **pose**: body joint/choreography guidance
- **canny**: edge/silhouette/layout guidance
- **depth**: scene geometry / near-far structure guidance

The Skill should request only the controls that directly protect a shot requirement. Enabling all controls by default is rejected because it increases graph complexity and can make constraints compete.

## Escalation ladder

```text
approved still only
↓ if endpoint must match
first + last
↓ if a critical middle beat must match
first + middle + last
↓ if body motion must follow a reference
pose IC-control
↓ if spatial/silhouette structure must also be constrained
pose + canny/depth
```

## Production binding rule

Control assets are external inputs. They must be uploaded into the target ComfyUI input space just like approved stills, then bound to the exact API-export nodes. Local paths embedded in a community workflow are not portable production inputs.
