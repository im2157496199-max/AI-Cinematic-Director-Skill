# Director Intent -> Video Decision

## 目的
把“导演能理解的话”转换成 AI 视频生成能执行、能验证的决策，但不直接捏造 ComfyUI 节点。

## 输入
- `shot_spec`
- `entity_sheet`
- 本镜 approved still
- previous shot end_state（多镜头时）
- target workflow profile / binding

## 输出
`video_shot_plan`

## 决策顺序
1. **叙事事件**：这一镜发生什么变化？
2. **动作阶段**：主体从 start_state 到 end_state 怎样变化？
3. **镜头运动**：摄像机是否真的需要移动？为什么？
4. **时间预算**：动作需要多少秒，而不是先定帧数再塞动作。
5. **运动幅度**：low / medium / high 只是语义等级；只有 workflow 暴露对应参数时才映射成数值。
6. **身份稳定优先级**：脸 / 发型 / 服装 / 标志道具必须保持。
7. **可控机制需求**：是否需要 start image、end image、camera control、control video、pose/depth reference。
8. **执行可用性**：真实 workflow 是否具备这些能力？缺失则标记 `UNBOUND`。

## 动作阶段化
不要只写：`draws sword`。
应写成：
- phase A: notice / prepare
- phase B: hand reaches grip
- phase C: blade exits sheath
- phase D: settle into final stance

是否需要四阶段都在一个 clip 中出现，由时长和运动复杂度决定；复杂动作宁可拆镜头，不要强塞。

## 重要约束
导演语言中的 `dolly in`、`handheld`、`subtle breathing` 等，并不天然对应一个 ComfyUI 参数。
必须先进入 adapter，确认具体 workflow 里有什么可控输入。
