# ComfyUI API Workflow Contract — studied from ComfyUI 0.33.0 source

Source basis:
- user-provided `ComfyUI-master.zip`
- `comfyui_version.py`: 0.33.0
- `script_examples/basic_api_example.py`
- `script_examples/websockets_api_example.py`
- `server.py`
- `execution.py`
- `openapi.yaml`

## API graph
`script_examples/basic_api_example.py` shows an API prompt graph as:

```json
{
  "3": {
    "class_type": "KSampler",
    "inputs": {
      "seed": 5,
      "model": ["4", 0]
    }
  }
}
```

Connections are two-item arrays: `[upstream_node_id, output_slot_index]`.

## Submit
ComfyUI local server accepts:

```json
{
  "prompt": { ...api graph... }
}
```

at `POST /prompt`.
The response contains `prompt_id`, queue number, and `node_errors` when successful.

## Validation facts from source
`execution.validate_prompt` rejects:
- node with no `class_type`
- class_type not present in installed node mappings
- graph with no output node
- linked input that is not `[node_id, slot_index]`
- linked output whose type does not match required input type
- literal values outside node min/max/list constraints

Therefore the Skill must never silently invent missing custom nodes or invalid enum values.

## Completion / result tracking
The bundled websocket example uses:
- `ws://.../ws?clientId=...`
- `POST /prompt`
- `GET /history/{prompt_id}`
- `GET /view?...`

The current system stores this as execution protocol knowledge; generation workflow topology remains user/workflow-specific.
