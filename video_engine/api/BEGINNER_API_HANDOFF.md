# 小白操作：你只做这 4 步

1. 在 ComfyUI 里打开你要用的 I2V Template。
2. 原样跑通一次，确认它真的能出视频。
3. `File -> Export Workflow (API)`，把导出的 JSON 保存下来。
4. 把 **API JSON + 这一镜批准的图片** 给 GPT/Skill。

你不需要手写 node id，也不需要知道 `class_type`。

Skill 应该自动做：
- 识别节点；
- 检查 `/object_info`；
- 找到 prompt / image / frame / fps / seed 等可绑定字段；
- 生成 binding；
- 只修改白名单字段；
- 提交后把 ComfyUI 原始报错翻译成人能看懂的问题位置。

如果只有普通 `Save` 出来的 workflow JSON：先在 ComfyUI 中 `File -> Load`，再 `File -> Export Workflow (API)`。不要自己手改成 API JSON。
