# API Input Asset Pipeline — approved still -> LoadImage

For the user's image-to-video route, the approved still is an execution dependency, not merely prompt text.

## Self-hosted image upload contract
Official source exposes `POST /upload/image` as multipart form. Important fields:
- `image`: required file
- `type`: use `input` for normal I2V source images
- `subfolder`: optional
- `overwrite`: optional

The server returns at least:
- `name`
- `subfolder`
- `type`

The compiled workflow must patch the verified `LoadImage.image` (or model-specific equivalent) input with the uploaded file reference expected by that workflow.

## Skill hard rules
1. Never place a local Windows path such as `C:\\...\\shot03.png` directly into a remote/server workflow unless that exact runtime is known to share the path.
2. For local Server API automation, upload/copy the approved still into ComfyUI input space first.
3. The binding profile must identify the actual image-loader node and input name from the exported API graph.
4. Keep source-image upload separate from prompt compilation, so failed uploads cannot silently generate a different shot.
5. Store returned upload metadata in the run report.
