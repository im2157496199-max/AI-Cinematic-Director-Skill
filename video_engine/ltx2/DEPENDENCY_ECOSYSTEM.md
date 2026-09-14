# Dependency Ecosystem Observed in Appvikalabs LTX-2 Workflows

## README-level requirements

The repository README explicitly calls out:

- current/updated ComfyUI
- `ComfyUI-KJNodes`
- `ComfyUI-GGUF`
- extracted LTX-2 model files from Kijai's LTXV2 repackaging
- Gemma 3 12B GGUF text encoder as an option

## Static graph provenance observed

Across all 19 parsed workflows, `properties.cnr_id` reveals these non-core packages:

- `comfyui-kjnodes`
- `ComfyUI-GGUF`
- `comfyui-videohelpersuite`
- `ComfyUI-MelBandRoFormer`
- `rgthree-comfy`
- `comfyui_controlnet_aux`
- `ComfyUI-QwenTTS`
- `comfy-mtb`
- `comfyui-easy-use`
- `comfyui_essentials`
- `comfymath`
- `ComfyUI-LTXVideo` (observed in the V2A Foley workflow)

The exact commit-like `ver` values are preserved in `catalog/appvikalabs_workflow_catalog.json`.

## Why package names are not enough

The same node type appears with different recorded versions across source workflows. ComfyUI core versions also vary substantially in node metadata. This means “I have the extension installed” is not enough to prove compatibility.

Production preflight remains:

```text
workflow API export
+ target /object_info
+ exact class_type/input contract
+ required model files
+ successful local regression run
```

## Model families observed

Common source model filenames include variants of:

- LTX-2 19B dev / distilled transformer
- GGUF dev/distilled transformer
- Gemma 3 12B text encoder / GGUF text encoder
- LTX embedding connectors
- video VAE
- audio VAE
- spatial latent upscaler
- distilled LoRA
- IC-LoRAs for pose/canny/depth/detailing
- camera-control LoRAs

Specialized branches add:

- pose/depth preprocessor models
- MelBand RoFormer
- Qwen-TTS voice clone dependencies
- tiny VAE for sampler previews

## Dependency policy in

1. **Never auto-download from a third-party workflow just because a filename is present.**
2. Resolve model locations through the user's actual ComfyUI environment.
3. Treat third-party node versions as provenance evidence, not a forced downgrade/upgrade target.
4. If `/object_info` lacks a required class type, report the exact missing node; do not substitute a similarly named node.
5. If a workflow requires many specialized packages for a feature the shot does not need, select a simpler profile instead.
