# UI Template JSON vs API Workflow JSON

## UI workflow/template JSON
Typical characteristics:
- root `nodes` array,
- root `links` array,
- layout metadata (`pos`, `size`, groups),
- `widgets_values`,
- `properties`,
- optional `definitions.subgraphs`,
- workflow `version` such as `0.4` or `1`.

Purpose:
- visual editing,
- sharing,
- template browser,
- subgraphs and user-facing organization.

## API format
Typical characteristics:
```json
{
  "6": {
    "class_type": "CLIPTextEncode",
    "inputs": {
      "text": "...",
      "clip": ["38", 0]
    }
  }
}
```

Purpose:
- programmatic execution / prompt queue.

## Hard rule
Do not patch `widgets_values[3]` in a UI template and call that an executable API binding.
Widget indexes are UI-node-version-sensitive and may be hidden/promoted through subgraphs.

The automation target is the **API export from the exact workflow that the user successfully ran**.

## When UI JSON is still valuable
UI template JSON is the best source for:
- template identity,
- official source and human layout,
- model metadata,
- subgraph interfaces,
- example values,
- node provenance (`cnr_id`, versions),
- discovering candidate controls before API export.

## Version rule
Workflow JSON v1.0 is the current documented schema, but official repository examples may still use legacy 0.4. Therefore:
- parser: accept both,
- writer: do not rewrite schema version unless ComfyUI itself exports it,
- binder: target API format instead of mutating schema versions.
