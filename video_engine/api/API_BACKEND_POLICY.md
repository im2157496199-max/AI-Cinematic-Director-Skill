# API Backend Policy

## Primary backend for this Skill now
`self_hosted_server_api` on the user's own ComfyUI. Reason: the project relies on local models, local hardware, and potentially custom nodes.

## Official newer path
Current official docs recommend Comfy SDKs + Comfy API v2 for new integrations. v2 is versioned and designed around assets/jobs, with polling as the source of truth. It can target Cloud or self-hosted through the official proxy.

## decision
Do not rewrite the current production bridge around v2 yet. Keep the workflow **API format** backend-neutral, because the official docs state the same API workflow representation is shared across the supported execution surfaces.

Maintain two execution profiles:
- `self_hosted_server_api`: active/default, classic `/prompt` + WebSocket/history
- `comfy_api_v2`: future/optional adapter, not claimed implemented in this version

This avoids confusing a beginner while preserving a migration path.
