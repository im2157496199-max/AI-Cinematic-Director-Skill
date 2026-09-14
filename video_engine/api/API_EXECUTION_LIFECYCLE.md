# API Execution Lifecycle — self-hosted ComfyUI

Default production lifecycle for the user's local ComfyUI:

```text
APPROVED STILL
 -> VIDEO_SHOT_PLAN
 -> VERIFIED API EXPORT
 -> OBJECT_INFO PREFLIGHT
 -> ASSET UPLOAD (if required)
 -> BINDING PATCH
 -> STRUCTURAL INVARIANT CHECK
 -> POST /prompt
 -> MONITOR (WebSocket + history preferred)
 -> HISTORY / OUTPUT REVIEW
 -> SHOT QA
```

## 1. Preflight
Query `/object_info` (or load a fresh saved snapshot) and verify:
- every `class_type` in the API graph exists on this machine;
- required inputs exist;
- every binding points to a real constant input;
- every link points to an existing upstream node and valid output slot where that can be checked.

A successful offline JSON parse is not a runtime validation.

## 2. Submit
Self-hosted Server API submission uses `POST /prompt` with at minimum:
```json
{"prompt": {"...": {}}}
```
Optional server fields can include `client_id`, `prompt_id`, `extra_data`, queue priority controls, and partial-execution targets when intentionally used.

## 3. Validation response
- accepted: `prompt_id`, `number`, `node_errors`
- rejected: HTTP 400 with `error` and `node_errors`

Do not hide `node_errors`; report node id + class type + input error to the user.

## 4. Completion monitoring
Official examples describe three patterns. For normal production the Skill prefers **WebSocket + History** because the official docs call it the best balance of reliability and simplicity. HTTP-only submit-and-forget is permitted for batch/background operation.

Important event semantics:
- `execution_start`: job starts
- `execution_cached`: cached nodes announced
- `executing`: node about to run; `node: null` is completion marker in the classic example
- `progress`: node progress where supported
- `execution_error`: execution failed
- `execution_interrupted`: interrupted
- `execution_success`: all nodes completed
- `executed`: only sent when a node returns a UI update; do not treat it as a universal per-node completion event

## 5. Retrieve result
Use `/history/{prompt_id}` as execution record. Image examples may retrieve files using `/view`; video/custom save nodes can expose different output fields, so output retrieval must be profiled per verified workflow rather than guessed.
