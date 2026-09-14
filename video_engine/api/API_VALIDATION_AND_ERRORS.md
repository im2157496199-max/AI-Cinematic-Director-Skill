# API Validation & Error Contract

## Why this exists
A JSON file can be syntactically valid and still be impossible for ComfyUI to execute. The runtime node registry is authoritative.

## Static contract checks
Before contacting ComfyUI:
- top level must be an object (or a wrapper containing `prompt` object);
- each node must be an object with `class_type` and `inputs`;
- node ids referenced by links must exist;
- normal bindings may not replace a link with a constant;
- normal compilation must not change graph topology.

## Runtime preflight
Use `/object_info` to check the currently loaded installation. This catches:
- missing custom nodes;
- renamed/removed class types;
- wrong input names;
- required inputs omitted;
- obvious enum/range errors where node metadata exposes constraints.

## Server-side prompt validation
The user-provided ComfyUI source validates:
- missing `class_type`;
- node class not installed;
- absence of output nodes;
- dependency cycles;
- required inputs;
- malformed links;
- linked return-type mismatches;
- node-specific `VALIDATE_INPUTS` failures.

The server can return `error` plus a `node_errors` map keyed by node id. The Skill must surface this evidence rather than substituting a guessed repair.

## Failure policy
- `missing_node_type` -> install/restore the exact node dependency or choose another verified template.
- `required_input_missing` -> repair binding/export; do not invent a default unless the node's contract defines one.
- `bad_linked_input` / return-type mismatch -> topology/export problem; stop automatic scalar patching.
- invalid model/file choice -> confirm runtime model/input inventory.
- execution-time error -> preserve prompt id, failing node, class type, and server message in the run report.
