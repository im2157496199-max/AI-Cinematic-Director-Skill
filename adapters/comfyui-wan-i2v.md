# ComfyUI Wan I2V Adapter

## What this adapter does
Maps `video_shot_plan` into a user-provided, already-working Wan API workflow.

## Core nodes confirmed in ComfyUI 0.33.0
### WanImageToVideo
Inputs include:
- width / height
- length
- batch_size
- optional start_image
- optional clip_vision_output

### Wan22ImageToVideoLatent
Inputs include:
- width / height (step 32)
- length (step 4)
- optional start_image

### WanFirstLastFrameToVideo
Adds optional end_image conditioning.

### WanCameraEmbedding
Exposes camera_pose and speed.

## Do not invent generic fields
The core Wan I2V nodes do **not** expose a universal input called `motion_strength`.
If a concrete workflow has a custom motion parameter, bind it there; otherwise keep `motion_amplitude` as a semantic decision used to shape prompt/action/control selection.

## Length
Use `4n + 1` snapping when binding to the core Wan length inputs.
Record target and actual duration.

## Camera
Only map to `WanCameraEmbedding` when the workflow actually contains it.
Native pose names must remain exact.

## First/last frame
Use only when both references exist and are intentionally designed.
Do not extract a random final video frame and automatically treat it as a clean next-shot anchor without review.
