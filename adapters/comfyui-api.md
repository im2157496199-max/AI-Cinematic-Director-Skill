# ComfyUI API Adapter

Basis:
- official ComfyUI `Workflow API Format` documentation;
- official Server API examples/routes/messages documentation;
- current API-v2 overview;
- user-provided official ComfyUI source snapshot (`server.py`, `execution.py`, `openapi.yaml`, `script_examples/`).

## Input
- **exported API-format workflow graph** from the real workflow that already runs in the user's ComfyUI;
- semantic binding file;
- compile request generated from `video_shot_plan`;
- optional fresh `/object_info` snapshot;
- approved input still(s).

## Output
- compiled API graph;
- structural patch report;
- preflight report;
- optional `/prompt` submission payload/run report.

## API graph contract
1. Execution graph is keyed by node id.
2. Every node must contain `class_type` and `inputs`.
3. Connections are `[upstream_node_id, output_slot_index]`.
4. `_meta` is diagnostic/editor metadata only; never use title as the node identity.
5. Do not submit normal UI/save workflow JSON as `prompt`.

## Compilation policy
- topology is immutable during normal shot compilation;
- node ids and `class_type` are immutable;
- linked inputs are immutable;
- only fields declared in `mutable_allowlist` + `bindings` may change;
- typed/range/step constraints in the binding are enforced;
- compile report records every changed scalar and a topology/class signature hash before/after.

## Runtime authority
Before production, query `GET /object_info` (or use a fresh captured snapshot) to validate the actual installation. A remembered node name is never stronger evidence than the target machine's node registry.

## Self-hosted execution lifecycle
1. Upload approved source image with `POST /upload/image` when the workflow expects `LoadImage`/equivalent.
2. Patch the returned input filename into the verified image binding.
3. `POST /prompt` with `{ "prompt": api_graph, ... }`.
4. Monitor with WebSocket + `/history/{prompt_id}` for normal interactive production.
5. Preserve `error` and `node_errors` on rejection/failure.

## Important official server endpoints used by this Skill
- `POST /prompt`
- `GET /history/{prompt_id}`
- `GET /queue`
- `POST /interrupt`
- WebSocket `/ws?clientId=...`
- `POST /upload/image`
- `GET /view?...`
- `GET /object_info`
- `GET /object_info/{node_class}`
- `GET /system_stats`

## Backend policy
The current project uses the local self-hosted Server API as the default because the user's models/hardware/custom nodes are local. Comfy API v2/SDKs are a future execution adapter; do not claim v2 support is complete simply because it uses the same API workflow representation.
