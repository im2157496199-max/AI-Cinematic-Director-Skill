# ComfyUI + Animagine XL Adapter ()

## Role mapping: reference -> mechanism

| reference_role | ComfyUI mechanism | purpose |
|---|---|---|
| identity | IPAdapter / IPAdapter Plus / FaceID when supported | preserve character identity |
| face | FaceID or face-focused reference workflow | preserve facial features |
| costume | IPAdapter Plus or reference image conditioning | preserve clothing/material |
| pose | ControlNet OpenPose | preserve body action |
| composition | ControlNet Depth / Canny / Lineart | preserve framing/layout |

## Consistency priority

Text only < single reference conditioning < IPAdapter + ControlNet combination < dedicated character LoRA.

Use escalation:
- one image: identity reference may be enough
- multi-shot sequence: use explicit identity lock + pose/composition controls
- recurring protagonist across many scenes: consider dedicated LoRA training

## Animagine XL notes

- Keep character identity tokens stable.
- Avoid replacing locked descriptors with synonyms.
- Use tag-style anime descriptors when the checkpoint/workflow expects tags.
- Use natural language only when the workflow is designed for it.
- Record checkpoint, sampler, steps, CFG, resolution, LoRA and reference settings.

## Node responsibility

Prompt compiler decides: what should appear.
Adapter decides: how conditioning enters ComfyUI.
Validator decides: whether identity continuity succeeded.
