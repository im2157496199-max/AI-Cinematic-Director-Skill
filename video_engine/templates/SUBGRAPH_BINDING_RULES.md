# Subgraph-Aware Binding Rules

## Why this matters
Modern official ComfyUI templates can collapse large video graphs into reusable subgraphs. A top-level node may have a UUID-like `type` and expose a small set of promoted inputs while the real loaders/samplers/conditioning nodes live in `definitions.subgraphs`.

A flat node scanner will misclassify such a template as "unknown custom node" or fail to find prompt/duration controls.

## Definitions
- **Subgraph instance**: a top-level node whose `type` matches a `definitions.subgraphs[].id`.
- **Promoted input**: an input on the subgraph instance surfaced from an internal widget/input.
- **proxyWidgets**: metadata mapping a top-level control to an internal node/widget.

## Binding policy
### SG-001 — Prefer promoted inputs
When a template intentionally promotes `prompt`, `duration`, model choices, camera controls, etc., bind through the promoted interface rather than reaching into internal node IDs.

Reason: the promoted interface is the template author's public control surface and is more stable than internal topology.

### SG-002 — Do not infer API binding from UI proxy alone
`proxyWidgets` helps explain the UI template but the executable API graph must still be exported and inspected. A UI proxy path is not automatically the same as an API node/input path.

### SG-003 — Recurse for dependency/provenance analysis
Inspect internal nodes to find:
- `properties.models`,
- `cnr_id` / versions,
- actual generation/control node types,
- fps/length nodes,
- hidden output pipeline.

### SG-004 — Keep namespace in reports
Represent an internal node as:
`subgraph:<subgraph_id>/node:<node_id>`
so repeated numeric IDs do not collide with root nodes.

### SG-005 — Subgraph is not a custom-node dependency by itself
A UUID-like node type that matches a bundled subgraph definition is a subgraph instance, not automatically a missing third-party custom node.

## Official Wan2.2 I2V observation
The current official `video_wan2_2_14B_i2v` template exposes a compact top-level interface around an `Image to Video (Wan2.2)` subgraph. Visible promoted controls include prompt, duration, high/low-noise model choices, LoRA choices and turbo enablement, while width/height/length/fps and the generation internals are represented inside the subgraph/proxy layer.

This is why the current system is subgraph-aware.
