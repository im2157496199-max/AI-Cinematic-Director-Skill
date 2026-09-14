# Frame / Duration Rules

## General rule
1. Director layer chooses `target_duration_s`.
2. Output playback chooses / inherits `target_fps`.
3. Adapter converts target frames into a model-valid `length`.
4. Record `actual_duration_s = length / fps`.
5. Never hide the rounding delta.

## Core node constraints learned from ComfyUI 0.33.0

### WanImageToVideo / WanFirstLastFrameToVideo / WanCameraEmbedding
- length default 81
- length step 4
- practical valid sequence form: `4n + 1`
- width/height step 16 on WanImageToVideo / FLF and camera embedding

### Wan22ImageToVideoLatent
- width/height default 1280x704, step 32
- length default 49, step 4
- therefore use `4n + 1` snapping for target length

### LTXVImgToVideo
- length default 97, minimum 9, step 8
- valid sequence form: `8n + 1`
- width/height step 32
- has explicit `strength` input (0..1), but this is conditioning strength, not a generic “motion strength” synonym.

### HunyuanVideo15ImageToVideo
- length default 33, step 4
- width/height step 16

### CreateVideo
- fps default 30
- allowed 1..120

## Snap policy
For a model requiring `step = s` and base form `s*n + 1`:

```text
target_frames = round(target_duration_s * fps)
length = nearest_valid(target_frames, s*n + 1)
actual_duration_s = length / fps
```

若 workflow 自身有更严格限制，以 workflow profile 为准。
