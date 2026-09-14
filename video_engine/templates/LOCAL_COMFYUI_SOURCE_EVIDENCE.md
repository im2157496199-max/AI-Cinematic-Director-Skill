# Local ComfyUI Source Evidence — user-provided snapshot

Observed from the uploaded `ComfyUI-master.zip` used for this build:

- `comfyui_version.py`: `0.33.0`
- `requirements.txt`: `comfyui-workflow-templates==0.11.44`
- `app/frontend_management.py` imports `iter_templates` / `get_asset_path` from `comfyui_workflow_templates` and resolves template assets.
- `app/custom_node_manager.py` scans custom-node folders named `example_workflows`, `example`, `examples`, `workflow`, `workflows` for JSON workflows.
- The custom-node manager exposes `/workflow_templates` and statically serves example workflow folders under `/api/workflow_templates/<module>`.
- `openapi.yaml` documents `/api/workflow_templates`.

## Engineering consequence
The template package is a separate installed dependency, and custom-node examples have their own discovery path. The Skill must record source kind and template-package version separately from ComfyUI core version.
