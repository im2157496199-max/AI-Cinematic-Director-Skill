# Beginner Template Handoff — 你只需要做什么

目标：用户不需要会写 ComfyUI JSON。Skill 负责分析、选择和绑定；用户只负责在自己的 ComfyUI 中确认模板真的能跑。

## 最短操作链

1. 打开 ComfyUI → **Templates**（或 `Workflow → Browse Workflow Templates`）。
2. 选择与你当前镜头任务匹配的模板，优先官方原生模板。
3. 不改节点结构，先把模型/输入图/提示词补齐，**原样跑通一次**。
4. 保存两份文件：
   - **UI Workflow JSON**：用于检查节点、模型、依赖、subgraph、可见控件。
   - **API Format JSON**：用于真正提交 `/prompt`；这是后续自动绑定的执行目标。
5. 把两份 JSON + 你要生成的镜头需求交给 Skill。
6. Skill 必须先做静态检查，再建立白名单 binding；没有 API JSON 时，不得声称“已经能自动执行”。
7. 第一次 binding 完成后，在你的机器上做一次真实回归；成功后才把该模板标记为 `BINDING_VERIFIED`。

## 你不用学的东西

你不需要手工：
- 记 node id；
- 改 `class_type`；
- 写 `links`；
- 从零拼完整节点图；
- 猜模型下载地址；
- 把 UI JSON 硬改成 API JSON。

## 你需要看懂的 5 个词

- **Template**：现成机器骨架。
- **UI Workflow JSON**：给 ComfyUI 画布/模板系统看的完整图结构。
- **API Workflow JSON**：给 ComfyUI `/prompt` 执行接口看的节点输入图。
- **Binding**：把 `shot_spec` 里的语义字段精确对应到 API JSON 的可改输入。
- **Verified**：这个工作流在你的 ComfyUI 机器上真的跑过，不只是文件语法正确。

## 对当前 8 镜 I2V 流程的使用方式

```text
剧本
→ 8 个 shot_spec
→ 每镜 T2I 静帧
→ 用户批准静帧
→ Skill 生成 video_shot_plan
→ 选择已验证 I2V Template
→ 绑定 prompt / start_image / duration-or-length / fps / seed / 模型特定控制
→ 编译 API workflow
→ ComfyUI 逐镜生成
→ 视频 QA
→ 剪辑
```

如果模板没有暴露某项能力（例如 camera control），Skill 不能假装一个通用 `camera_motion` 参数存在；应改选支持该能力的模板，或把导演意图降级为 prompt / source-image staging / 后期处理方案。
