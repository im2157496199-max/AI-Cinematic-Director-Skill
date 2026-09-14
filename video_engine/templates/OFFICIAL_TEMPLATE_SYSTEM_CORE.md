# Official ComfyUI Template System Core

## Purpose
This layer turns ComfyUI's official Template system into a stable execution substrate for the Skill.
It does **not** replace directing, cinematography, art direction, editing, or character continuity. It defines how a finished `video_shot_plan` is attached to a real ComfyUI workflow without inventing nodes.

## Source authority
Use this order when facts conflict:
1. **User's installed/running ComfyUI and exported workflow** — execution truth for the user's machine.
2. **User-provided ComfyUI source snapshot** — code behavior reference. The supplied source reports ComfyUI `0.33.0` and pins `comfyui-workflow-templates==0.11.44`.
3. **Current ComfyUI official documentation** — user-facing contract and current schema guidance.
4. **Comfy-Org/workflow_templates repository** — actual official template examples and current template topology.
5. Secondary/community tutorials — reference only, never binding authority.

Do not silently combine settings from different versions.

## Official facts promoted to runtime rules
### TPL-001 — Template Browser is a workflow source, not an execution format
ComfyUI Templates provide natively supported workflows plus examples shipped by custom nodes. A template is loaded into the visual graph, where the user can edit and run it.

**Runtime rule:** `Template JSON != API execution JSON`.
A UI template must be loaded/validated and an API-format graph exported before unattended `/prompt` execution.

### TPL-002 — Prefer known templates over invented graphs
Official templates are complete runnable examples built from supported capabilities. The Skill should select and bind a known template before considering topology creation.

Default order:
`verified user workflow > official template adapted and run-verified > trusted custom-node example > new workflow design`.

### TPL-003 — Dependency completeness is a gate
A workflow may depend on:
- input assets (images / video / audio),
- models,
- custom nodes,
- Python dependencies,
- compatible ComfyUI/frontend/software versions.

A JSON file alone is not proof that a workflow is runnable.

### TPL-004 — Embedded model metadata is machine-readable evidence
Official templates can attach model records under node `properties.models` with:
- `name`
- `url`
- `directory`
- and in newer schema/repository data, optionally `hash` / `hash_type`.

The Skill may extract these records into a dependency manifest. It must not invent download links.

### TPL-005 — Missing-model UI detection is not a definitive filesystem audit
Official docs note that missing-file detection can be based on matching the model file name in the expected top-level model directory. A model stored in a deeper custom subfolder can therefore trigger a warning even if the user can select it successfully.

**Runtime rule:** popup warning = `MODEL_DETECTION_WARNING`, not automatically `MODEL_MISSING`.
Actual loader selection/run result has higher authority.

### TPL-006 — Core official templates and custom-node templates have different trust profiles
Official repository contribution rules avoid third-party nodes for official templates. Custom-node authors can expose example workflows separately.

Default trust labels:
- `official_core_template`
- `custom_node_example`
- `user_verified_workflow`
- `unknown_external_workflow`

Never label a custom-node example as official core.

### TPL-007 — Template package version is independent from ComfyUI core version
`comfyui-workflow-templates` is a separate dependency. A user's ComfyUI code version and installed template package version must be recorded separately.

### TPL-008 — Accept legacy and current Workflow JSON
Official docs define Workflow JSON v1.0 as latest, while many current official repository templates still carry `version: 0.4`.

**Runtime rule:** do not reject a template merely because it is v0.4. Parse both known families and record the observed version.

### TPL-009 — Subgraphs are first-class
Current official video templates may hide large graphs behind a subgraph node and expose promoted inputs such as prompt, duration, model choices, or turbo switches.

A template inspector must recurse into `definitions.subgraphs`; a binder must understand top-level promoted inputs and `proxyWidgets` instead of assuming every control is a visible top-level node.

### TPL-010 — No offline UI→API conversion promise
UI Workflow JSON contains visual graph data (`nodes`, `links`, positions, groups, subgraphs, widget values). API format uses node IDs as keys with `class_type` and `inputs`.

Without the live node definitions/frontend conversion path, the Skill must not claim it can always losslessly convert arbitrary UI JSON to API JSON offline.

Correct production path:
`load template -> satisfy dependencies -> run once -> export/save API format -> bind API graph`.

## Verification states
A workflow profile moves only forward when evidence exists:
1. `DISCOVERED`
2. `UI_JSON_INSPECTED`
3. `DEPENDENCIES_RECORDED`
4. `LOADED_IN_COMFYUI`
5. `RUN_VERIFIED`
6. `API_EXPORTED`
7. `BINDING_VERIFIED`
8. `REGRESSION_PASS`

A profile at state 1–3 is a **candidate**, not a runnable production workflow.

## Skill-facing result
The creative system should never expose raw graph complexity to the user unless requested. It should return a human-readable summary:
- selected template/profile,
- required input still,
- prompt/action intent,
- target duration/fps,
- special controls requested,
- missing dependencies or unsupported controls,
- verification state.
