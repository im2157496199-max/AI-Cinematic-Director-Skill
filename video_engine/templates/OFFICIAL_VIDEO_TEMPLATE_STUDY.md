# Official Video Template Study

This is a source-grounded study of representative templates in `Comfy-Org/workflow_templates`. It is **not** a universal parameter recommendation.

## 1. `image_to_video_wan.json` — Wan 2.1 baseline I2V
Observed topology includes core nodes for:
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- positive / negative `CLIPTextEncode`
- `LoadImage`
- `WanImageToVideo`
- sampler / decode
- `CreateVideo`
- `SaveVideo`

Example `WanImageToVideo` widget values in the official snapshot correspond to width=512, height=512, length=33, batch=1. `CreateVideo` example fps is 16.

**Skill lesson:** this old-style flat template is easy to inspect, but its widget positions are still not a stable automation contract. Export API format before binding.

## 2. `ltxv_image_to_video.json` — LTXV flat I2V example
Observed core topology includes:
- checkpoint and text-encoder loaders,
- positive/negative text conditioning,
- `LoadImage`,
- `LTXVImgToVideo`,
- `LTXVConditioning`,
- sampler / VAE decode,
- `CreateVideo`, `SaveVideo`.

Example values visible in the official snapshot:
- LTXV I2V: 768×512, length 97, batch 1, conditioning strength 0.15,
- output video fps: 24.

**Skill lesson:** `strength` is model-conditioning strength, not a generic "motion intensity" control. Never map a director's `motion_strength` semantic directly without adapter evidence.

## 3. `video_wan2_2_14B_i2v.json` — Wan 2.2 I2V with subgraph
Current official template uses a compact root graph:
`LoadImage -> Image to Video (Wan2.2) subgraph -> SaveVideo`.

Promoted controls observed on the subgraph instance include:
- prompt,
- duration,
- high-noise model,
- high-noise Lightning LoRA,
- low-noise model,
- low-noise Lightning LoRA,
- turbo mode.

The internal subgraph exposes/contains video-specific values such as dimensions, length and fps, while the template also records model links and GPU/VRAM example notes.

**Skill lesson:** template binding must be subgraph-aware and version-aware. Root-node scanning alone is insufficient.

## 4. `video_wan2_2_14B_flf2v.json` — First/Last Frame
This template is a separate capability, not just "I2V with another image".

**Skill routing rule:** choose FLF2V only when the shot design has a deliberate approved end image or explicit end-state anchor. Do not fabricate an end frame merely because the workflow supports it.

## 5. `video_wan2_2_14B_fun_camera.json` — explicit camera control
Observed nodes include `WanCameraEmbedding` and `WanCameraImageToVideo`. The example exposes camera-pose choices and camera embedding values, with length/fps in the video path.

**Skill routing rule:** explicit camera-control template should be selected only when the requested camera motion needs deterministic control and the selected workflow is run-verified on the user's machine.

Director words like `dolly in` must not be silently equated with a model's `Zoom In` control; cinematographic difference remains active.

## 6. API/partner-node Wan I2V templates
Official repository also contains API-node workflows such as `WanImageToVideoApi`, exposing service-level fields like model, prompt, negative prompt, resolution, duration, seed and feature toggles.

**Important separation:** this is not the same execution route as a local open-weight Wan graph. The Skill must tag provider/API workflows separately from local workflows.

## Routing summary for the user's intended pipeline
The user workflow is:
`script -> 8-ish still shots -> user approval -> one I2V clip per shot -> edit`.

Default candidate routing:
- simple approved still + moderate movement -> standard I2V template,
- deliberate start/end visual state -> FLF2V,
- camera movement needs explicit supported control -> camera template,
- otherwise keep camera intent in prompt or simplify rather than invent controls.

Hardware/model choice remains a separate adapter/profile decision; official examples are evidence of topology, not proof that a specific user's GPU can run every model variant.
