# Video Engine

本目录负责 Skill 的“技术导演 / 工作流编译”层。

它不替代导演、摄影、美术、剪辑理论，而是把这些理论产生的 `shot_spec` 转成可执行的视频生产计划，并严格区分：

- 创意意图
- 工作流选择
- UI Workflow / Template
- API Workflow
- 运行时节点契约
- 实际生成结果与 QA

默认流程：

```text
script
→ shot_spec
→ approved still
→ video_shot_plan
→ workflow selector
→ verified UI workflow
→ Export Workflow (API)
→ semantic binding
→ /object_info preflight
→ topology-preserving compile
→ ComfyUI run
→ clip QA
→ edit
```

## 新增 LTX-2 层

`video_engine/ltx2/` 深入学习了 `appvikalabs/LTX-2-Workflows` 的 19 个工作流文件，并把它们转成：

- workflow family catalog
- capability selector
- semantic Set/Get anchor analysis
- UI → API binding candidate logic
- keyframe/control/audio/V2V/V2A decision rules
- currentness/migration boundary

重点不是把第三方 JSON 原样塞进 Skill，而是让 GPT 学会：

> **什么时候该选哪类 LTX 工作流，以及怎样把一个真实可运行的工作流安全绑定到 API。**

## 关键原则

- 创意层与执行层分离。
- 任何具体 ComfyUI 节点 ID 必须来自真实 workflow。
- Community workflow 只能做参考案例，不能自动标记生产可用。
- 模型专用约束只写在 adapter / workflow profile，不污染导演层。
- 生成参数没有真实节点承载时，不要假装“已经映射”。
- 生产执行必须通过 API export + `/object_info` + regression run。
