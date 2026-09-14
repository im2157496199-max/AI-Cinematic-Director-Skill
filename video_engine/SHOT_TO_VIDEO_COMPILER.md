# Shot -> Video Compiler

## Pass V0 — Approval Gate
必须存在：
- `approved_still: true`
- `source_image_ref`

否则输出 `APPROVAL_REQUIRED`，停止 I2V 编译。

## Pass V1 — Load Explicit Locks
每次编译重新显式传入：
- locked identity
- costume anchors
- prop anchors
- location anchors（需要时）

不得依赖聊天记忆复述。

## Pass V2 — Temporalize the Shot
从 `shot_spec.start_state` 到 `shot_spec.end_state` 提取：
- subject motion
- prop motion
- environment motion
- camera motion
- hold / pause

## Pass V3 — Duration First
先根据戏剧动作确定 `target_duration_s`，再由 adapter 把它换成模型合法 `length`。
不要把“5秒”直接硬写成任意帧数。

## Pass V4 — Camera Mapping
把导演意图归类：
- static
- pan / tilt
- push / pull
- roll
- orbit / truck / handheld（需要 workflow 特定能力）

只有 adapter 确认有对应控制时才绑定。

## Pass V5 — Control Requirement
输出语义需求，不先指定节点：
- identity_reference_required
- pose_control_required
- depth_or_composition_control_required
- first_last_frame_control_required
- camera_control_required

## Pass V6 — Workflow Select
从 `workflow_registry` 中选择满足能力的已验证模板。
不存在满足条件的模板时：`NO_COMPATIBLE_WORKFLOW`。

## Pass V7 — Binding
读取该模板的 `comfyui_workflow_binding`。
只修改白名单 input。
不改拓扑、不新造 node id、不改 class_type，除非用户明确要求生成新 workflow。

## Pass V8 — Compile API Graph
生成 ComfyUI API format graph：
- node-id keyed object
- 每节点至少包含 `class_type` + `inputs`
- 连接保持 `[node_id, output_slot_index]`

## Pass V9 — Lint
检查：
- 所有 binding node 存在
- 所有绑定 input 存在
- 必须 output node 存在
- source image 已绑定
- frame/length 满足 profile 约束
- fps 与实际时长记录一致
- 未绑定需求必须显式输出，不能静默丢弃
