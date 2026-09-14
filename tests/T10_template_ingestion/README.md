# T10 — Official Template Ingestion Regression

Purpose: verify the template-ingestion layer can inspect both a flat ComfyUI UI workflow and a subgraph-based workflow without confusing UI JSON with API JSON.

Checks:
- legacy `version: 0.4` accepted,
- core-node provenance recorded,
- `properties.models` extracted,
- input image reference extracted,
- subgraph instance recognized,
- internal subgraph dependencies discovered,
- promoted prompt/duration controls discovered,
- `proxyWidgets` recorded,
- static gate explicitly stops short of run-verification claims,
- profile remains `production_ready: false` until real ComfyUI run + API export + binding regression.

Fixtures are synthetic/minimal and intentionally do **not** claim to be official templates. Official repository templates are studied in `video_engine/templates/OFFICIAL_VIDEO_TEMPLATE_STUDY.md`.
