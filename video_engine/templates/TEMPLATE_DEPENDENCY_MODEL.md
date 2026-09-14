# Template Dependency Model

## Dependency categories from official ComfyUI guidance
A workflow may require more than its JSON graph:
1. **Assets** — source images, video, audio, masks, etc.
2. **Models** — diffusion/checkpoint, VAE, text encoders, CLIP vision, LoRA, ControlNet, etc.
3. **Custom nodes** — community extensions.
4. **Python dependencies** — packages required by ComfyUI or custom nodes.
5. **Software/runtime compatibility** — ComfyUI/frontend/Python/CUDA/node versions.

## Manifest schema
Use `templates/template_dependency_manifest.yaml`.

Each model record should preserve source evidence when present:
```yaml
- name: model.safetensors
  directory: diffusion_models
  url: https://...
  hash: null
  hash_type: null
  declared_by_node:
    node_id: 37
    node_type: UNETLoader
```

Never synthesize a URL from the filename.

## Model-detection caveat
The Template browser's missing-model check may look for the filename at the expected top-level model directory. If the same model is stored in a nested user folder and is selectable in the loader node, the popup can be a false positive.

Status vocabulary:
- `DECLARED`
- `UI_DETECTION_WARNING`
- `USER_CONFIRMED_AVAILABLE`
- `LOADER_SELECTED`
- `RUN_VERIFIED`
- `MISSING`

## Custom node rule
`cnr_id: comfy-core` is evidence of core-node provenance in current templates.
Any other `cnr_id`, or absent provenance on a suspicious/unknown type, must be reported—not auto-installed.

## Safe distribution rule
Dependency manifests may contain model names and official direct URLs discovered in the workflow metadata, but must not bundle model weights.
