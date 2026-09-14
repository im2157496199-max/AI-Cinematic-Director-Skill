# Video Capability Matrix

This matrix separates **core/API capability evidence** from **community workflow-pattern evidence**. It is not a promise that the user's current runtime exposes every listed node.

## Core / previously studied capabilities

| Capability | Example node evidence | Important exposed concepts |
|---|---|---|
| Wan I2V | `WanImageToVideo` | width, height, length, start image, vision conditioning |
| Wan first+last frame | `WanFirstLastFrameToVideo` | start image, end image, length |
| Wan 2.2 latent I2V | `Wan22ImageToVideoLatent` | width, height, length, start image |
| Wan control video | `WanFunControlToVideo` | start image, control video, length |
| Wan camera | `WanCameraEmbedding` | camera pose, length, speed, intrinsics |
| LTX I2V core family | LTX video nodes | image/text conditioning, video/audio latent, timing |
| Hunyuan 1.5 I2V | `HunyuanVideo15ImageToVideo` | start image, width, height, length, vision conditioning |
| Images → video object | `CreateVideo` | images, fps, audio, color space |
| Video save | `SaveVideo` | video, format, codec |

## LTX-2 workflow-family evidence added in

Derived from 19 Appvikalabs UI workflows:

| Capability | Source workflow pattern | Selector meaning |
|---|---|---|
| Basic I2V | I2V Basic / Simple | approved still → motion |
| Basic T2V | T2V Basic | text-only generation |
| First+last | First Last Frame | hard endpoint control |
| First+middle+last | First Middle Last Frame | hard middle beat + endpoints |
| Pose control | I2V IC-Control pose | choreography/control clip |
| Pose+canny+depth | All-In-One IC-Control | multi-constraint structure control |
| I2V↔T2V mode | I2V and T2V | explicit mode switching |
| Custom audio | I2V/T2V custom audio | supplied audio drives/joins generation |
| Voice clone | Talking Avatar | speaker reference + generated speech/video |
| V2V extension | V2V extend | continue an existing clip |
| V2A Foley | V2A Foley | generate audio from picture |
| GGUF variant | Basic (GGUF) | alternate model-loading envelope |
| Low-VRAM reference | T2V Basic (low vram) | lower-memory reference case, not a hardware guarantee |
| Two-stage upscale | most Basic/control workflows | pass 1 → latent upscale → pass 2 |
| No-upscale | I2V Simple (no upscale) | minimum-complexity single-stage path |

## Currentness warning

The Appvikalabs material is a community/legacy architecture corpus. Current Lightricks documentation lists newer LTX-2.3 workflows separately from older LTX-2.0 examples. Therefore node/model specifics must be re-resolved for the user's actual workflow.

## Rule

Selection happens through workflow profiles and bindings. A capability listed here is **evidence that a workflow family exists**, not permission to invent or splice nodes into an unrelated graph.
