# T12 — Runtime Node Contract Preflight
Uses a frozen mock `/object_info` snapshot to verify that the Skill can catch missing node classes, required inputs, enum problems, and bad output slots before submission. A mock snapshot is used so the regression is deterministic; it is not claimed as evidence that the user's live ComfyUI is currently reachable.
