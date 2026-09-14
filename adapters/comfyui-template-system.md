# ComfyUI Template-System Adapter

## Scope
This adapter connects the Skill's `video_shot_plan` to ComfyUI Workflow Templates and then to a verified API-format workflow.

## Required separation
- Template/UI JSON: discovery, dependencies, provenance, subgraph interface.
- API JSON: execution and automatic patching.

## Supported source kinds
- official Comfy-Org template
- custom-node example workflow
- user-created/user-exported workflow
- external unknown workflow

## Adapter sequence
1. Inspect UI template.
2. Extract provenance/dependencies/subgraphs.
3. User loads and runs the unchanged workflow.
4. User exports API format.
5. Inspect API graph.
6. Create semantic binding.
7. Compile only allowlisted fields.
8. Run regression.

## Runtime guard
An official template that has not been run on the user's machine is `OFFICIAL_CANDIDATE`, not `VERIFIED_WORKFLOW`.
Official status increases provenance confidence, not execution certainty.

## Current source note
The user's uploaded ComfyUI source reports version 0.33.0 and its `requirements.txt` pins `comfyui-workflow-templates==0.11.44`. Treat this as the local source snapshot, not a claim about every current installation.
