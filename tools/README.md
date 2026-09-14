# Tools

## API execution layer

- `comfy_workflow_inspect.py` — inspect API workflow node ids / class types / inputs.
- `frame_math.py` — apply model/profile-specific time↔frame rules.
- `comfy_workflow_compile.py` — patch only binding allowlist fields; refuse linked-input overwrite; preserve topology signature.
- `comfy_submit_api.py` — submit compiled API graph to local `/prompt`.
- `comfy_api_inspect.py` — recognize API-format graph and compute topology signature.
- `comfy_api_preflight.py` — validate exported graph against live/saved `/object_info`.
- `comfy_upload_image.py` — upload approved still into ComfyUI input space.
- `comfy_run_api_ws.py` — submit and monitor with WebSocket + history.

## Official Template ingestion

- `comfy_ui_template_inspect.py` — inspect UI/template JSON, nodes, subgraphs, `properties.models`, assets and promoted inputs.
- `comfy_template_gate.py` — static template gate; PASS is not runtime proof.
- `comfy_template_profile.py` — conservative template capability profile.

## LTX-2 workflow intelligence added in

- `ltx2_repo_inspect.py`
  - accepts an extracted repo or ZIP;
  - parses every valid ComfyUI UI workflow;
  - records hashes, node types, groups, models, `cnr_id` packages, notes, semantic SetNode anchors and inferred capabilities;
  - never executes or marks a workflow production-ready.

- `ltx2_select_profile.py`
  - maps requirements such as I2V/T2V/V2V/V2A, keyframes, pose/canny/depth, audio mode, GGUF, low-VRAM and upscale policy to a **reference case**;
  - returns `REFERENCE_CASE_SELECTED`, not `PRODUCTION_READY`.

- `ltx2_binding_candidates.py`
  - traces backward from Appvikalabs-style `Set_*` semantic buses;
  - finds upstream mutable sources such as `CLIPTextEncode`, `LoadImage`, `INTConstant`, `PrimitiveFloat`, `PrimitiveBoolean`;
  - solves the “SetNode input is linked, so compiler cannot patch it directly” problem.

- `ltx2_ui_to_api_binding.py`
  - takes semantic UI candidates plus a real API-format export;
  - requires same node id and matching `class_type`;
  - resolves constant API input names conservatively;
  - outputs candidate bindings for later `/object_info` verification.

## Hard boundary

Do not send UI/template JSON to `/prompt`.

Do not treat a community UI workflow as production-ready.

Production automation requires:

`working local workflow → Export Workflow (API) → binding → /object_info → compile → regression run`.
