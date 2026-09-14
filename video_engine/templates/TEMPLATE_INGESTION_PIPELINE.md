# Template Ingestion Pipeline

This is the required path for turning an official or user workflow into something the Skill may modify automatically.

## Stage 0 — Preserve source identity
Record:
- template name / ID,
- source kind,
- source URL or local file ref,
- observed workflow JSON version,
- ComfyUI version tested,
- template package version if known,
- import date.

Never overwrite the original source snapshot with compiled output.

## Stage 1 — UI JSON inspection
Run `tools/comfy_ui_template_inspect.py`.
Collect:
- top-level node inventory,
- subgraph inventory,
- `cnr_id` / node version metadata,
- model dependency records from `properties.models`,
- input media filenames from loader widgets where detectable,
- promoted subgraph inputs and `proxyWidgets`,
- possible control surfaces.

Result: `template_profile.json`.

## Stage 2 — Dependency gate
Run `tools/comfy_template_gate.py`.
The gate checks what can be known statically:
- JSON parseability,
- UI workflow shape,
- observed workflow version,
- presence of nodes,
- core vs non-core node metadata,
- declared models,
- subgraph presence,
- whether input assets are referenced.

It **does not** claim models exist on disk or that the graph executes.

## Stage 3 — Load in the user's ComfyUI
User action is authoritative:
1. Open Templates or load the JSON.
2. Resolve required models/assets.
3. Ensure loader nodes point to installed models.
4. Run the workflow without Skill-generated changes.

If it cannot run untouched, do not bind it yet.

## Stage 4 — Run verification
Record:
- success/failure,
- ComfyUI version,
- GPU/VRAM if relevant,
- actual model variants,
- actual output duration/resolution,
- known warnings.

A successful screenshot alone is weaker evidence than saved workflow + output + run report, but may still be recorded as manual evidence.

## Stage 5 — Export API-format workflow
For automation, export the graph in API format from ComfyUI.
Do not treat UI template JSON as if it were already the `/prompt` graph.

Store as:
`workflow_library/api/<profile_id>.api.json`

## Stage 6 — API graph inspection
Run existing `tools/comfy_workflow_inspect.py`.
Identify exact API fields for:
- positive prompt,
- negative prompt,
- source image,
- optional end image,
- width / height,
- model-valid frame length,
- fps,
- optional camera/control inputs,
- seed when deliberately exposed.

## Stage 7 — Build explicit binding
Populate `templates/comfyui_workflow_binding.yaml`.
Only fields in the allowlist are mutable.

If a requested semantic field has no concrete API input, mark `UNBOUND`.
Do not "approximate" silently.

## Stage 8 — Compile and regression test
Patch a copy of the API graph with `tools/comfy_workflow_compile.py`.
Then:
- validate node IDs and `class_type`,
- reject overwrite of linked inputs,
- run the patched workflow,
- compare output against the baseline.

Only after this stage may the registry mark `REGRESSION_PASS`.

## Why this pipeline exists
The Skill's job is not to become a fragile JSON generator. It is to become a reliable technical director:
`director intent -> choose a proven machine -> expose only safe controls -> run -> review`.
