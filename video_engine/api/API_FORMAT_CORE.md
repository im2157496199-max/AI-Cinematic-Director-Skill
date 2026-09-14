# ComfyUI API Format Core

## Source scope
Primary source: official ComfyUI documentation page `Workflow API Format`, cross-checked against the user-provided official ComfyUI source snapshot (`server.py`, `execution.py`, `script_examples/*`, `openapi.yaml`).

## Hard facts from the official docs/source
1. Programmatic workflow execution requires the **API format**, not the normal frontend save/layout format.
2. The API graph is a JSON object keyed by node id. Each node has at least `class_type` and `inputs`; `_meta` may also be present.
3. Linked inputs are represented as `[upstream_node_id, output_slot_index]`.
4. The normal frontend workflow contains editing metadata such as node positions, sizes, colors/groups; API format omits that UI-only state.
5. The beginner-safe conversion path is: load the workflow in ComfyUI -> `File -> Export Workflow (API)`.
6. For self-hosted ComfyUI, `POST /prompt` accepts a body containing `prompt: <api_graph>` and validates it before queueing.
7. Validation errors may return `error` plus `node_errors`; successful queueing returns `prompt_id`, queue `number`, and `node_errors`.
8. `GET /object_info` and `/object_info/{node_class}` expose the node definitions currently loaded on the user's machine. This is the correct runtime authority for node names and input contracts.
9. An API workflow does **not** carry model binaries, input images, or custom-node packages. These are external dependencies.

## Skill policy derived from those facts
- Never generate a full production graph from memory when a verified exported API graph exists.
- Treat the exported graph as an immutable topology template; patch only declared scalar/widget inputs.
- Do not overwrite link-valued inputs unless a separate topology-edit operation is explicitly requested.
- Before production submission, compare every `class_type` and bound input name against the target machine's `/object_info` snapshot.
- Preserve `class_type`, node ids, and link topology across normal shot compilation.
- Keep `_meta` if present; it is useful for diagnostics but must never be used as the execution identity of a node.
- If the user only has UI/save-format JSON, do not promise lossless offline conversion. Ask ComfyUI itself to export API format whenever possible.

## Minimum API node contract
```json
{
  "6": {
    "class_type": "CLIPTextEncode",
    "inputs": {
      "text": "...",
      "clip": ["4", 1]
    },
    "_meta": {"title": "CLIP Text Encode (Prompt)"}
  }
}
```

## What GPT is allowed to decide
GPT/Skill may choose semantic values such as prompt text, seed policy, approved source image, target frame length, resolution, or workflow profile. It may only write those values into node inputs after a binding file proves which exported node/input owns that semantic field.

## What GPT must not guess
- unknown node ids
- unknown `class_type` values
- custom-node input names
- link slot indexes
- model filenames/paths not found in the verified workflow/runtime
- output retrieval schema for a custom output node
