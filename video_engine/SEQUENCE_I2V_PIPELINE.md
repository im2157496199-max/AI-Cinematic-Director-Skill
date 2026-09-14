# Multi-shot I2V Pipeline

用户当前主流程固定为：
**先文生图做分镜静帧，再逐镜图生视频。**

## Sequence stages
### Stage A — Script and shot design
先把故事拆成可读的镜头计划，通常 8 镜，但不是强制固定 8。

### Stage B — T2I stills
每个镜头独立生成静帧，但共同读取：
- entity locks
- style / palette locks
- location locks
- previous shot continuity state

### Stage C — Human approval
只有用户明确确认的静帧进入视频阶段。
修改静帧比让视频模型补救构图/身份错误更可靠。

### Stage D — I2V per shot
每镜生成一个 clip：
`approved still + shot motion intent + camera intent + workflow binding`。

### Stage E — Clip continuity
检查：
- first frame 是否继承 approved still 的身份和构图
- end_state 是否符合下一镜的 start_state
- 服装 / 道具 / 损伤 / 天气是否连续

### Stage F — Edit
把通过 QA 的 clips 交给 `edit_sequence_spec` 决定：
- in/out point
- duration
- rhythm
- eye trace
- sound handoff

## First / last frame mode
当 workflow 使用 ComfyUI 核心 `WanFirstLastFrameToVideo` 时，可把下一状态设计成 end image 约束。
这不是默认要求；只有 workflow 支持并且 end frame 已被设计/批准时启用。
