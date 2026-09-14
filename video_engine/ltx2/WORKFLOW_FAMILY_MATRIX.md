# Appvikalabs LTX-2 Workflow Family Matrix

Source-derived matrix from the 19 workflow files parsed in the current build. Node counts and capability tags come from static graph inspection; they are **not runtime success claims**.

| Workflow | Nodes | Main use | Key distinction | Production status |
|---|---:|---|---|---|
| First Last Frame (guide node) | 103 | I2V | start + end guide frames, 2-stage upscale | reference case |
| First Last Frame (in-place node) | 103 | I2V | start + end in-place conditioning | reference case |
| First Middle Last Frame (guide node) | 113 | I2V | start + middle + end control | reference case |
| I2V Basic (GGUF) | 84 | I2V | GGUF model path | reference case |
| I2V Basic (custom audio) | 111 | I2V | imported audio drives/joins AV latent | reference case |
| I2V Basic | 85 | I2V | normal 2-pass path | reference case |
| I2V IC-Control (pose) | 125 | I2V | pose-preprocessor + IC LoRA branch | reference case |
| I2V Simple (no upscale) | 46 | I2V | single-stage, smallest graph | reference case |
| I2V Simple (with upscale) | 65 | I2V | compact 2-stage path | reference case |
| I2V Talking Avatar | 112 | I2V | Qwen-TTS voice clone + AV path | reference case |
| I2V and T2V (sampler previews) | 110 | I2V/T2V | mode switch + sampling previews | reference case |
| I2V and T2V IC-Control | 164 | I2V/T2V | pose + canny + depth + mode switch | reference case |
| T2V Basic (GGUF) | 68 | T2V | GGUF path | reference case |
| T2V Basic (custom audio) | 96 | T2V | imported audio | reference case |
| T2V Basic (low vram) | 71 | T2V | reduced default resolution | reference case |
| T2V Basic | 68 | T2V | normal 2-pass path | reference case |
| T2V Talking Avatar | 97 | T2V | voice clone + generated video | reference case |
| V2A Foley | 85 | V2A | audio generation from source video | reference case |
| V2V extend any video | 91 | V2V | extend a reference clip | reference case |

## Family-level conclusions

### 1. Basic I2V/T2V is the trunk

Most workflows share the same broad graph architecture:

```text
model/clip/vae/audio-vae
→ prompt conditioning
→ AV latent preparation
→ sampler pass 1
→ latent spatial upscale
→ sampler pass 2
→ video/audio separation
→ tiled decode
→ video combine/output
```

This means the Skill should select a **family** first and preserve the author's infrastructure. It should not rebuild the whole node graph to add one feature.

### 2. Features are branch additions

Observed branches include:

- `LoadImage` / keyframe guides for I2V and first-last control
- custom audio encode / trim / stem processing
- IC-LoRA pose/canny/depth preprocessors
- `PrimitiveBoolean` mode switch for I2V ↔ T2V
- Qwen-TTS voice clone
- V2V source-video encoding
- V2A audio-only/foley logic

The selector should therefore model requirements as orthogonal capabilities instead of hardcoding a single “best LTX workflow.”

### 3. Graph complexity rises sharply with controls

The all-in-one IC-Control graph reaches 164 nodes, versus 46 nodes for `I2V Simple (no upscale)`. This justifies a **minimum-complexity satisfying workflow** rule: only pay for a branch when the shot actually needs it.

### 4. Two-stage upscale is a recurring quality pattern

Most basic workflows include a first sampler pass, latent upscale, and second sampler pass. The simple no-upscale workflow is a deliberate exception. For planning, the current system treats “upscale” as a workflow capability, not as a parameter that can be casually toggled in any graph.
