# ComfyUI Workflow Binding System

## 为什么不用 GPT 每次从零写节点图
ComfyUI API graph 的节点 ID 由具体 workflow 决定，同一个 `CLIPTextEncode` 在不同图里可能是 6、17 或 120。
直接让 LLM 猜 node id 会产生看似正确、实际无法运行的 JSON。

因此当前系统使用：

`已验证 workflow API JSON + binding map + compile request -> compiled API JSON`

## Binding 的作用
把语义字段绑定到真实节点输入：

```yaml
bindings:
  positive_prompt:
    node_id: "6"
    expected_class_type: CLIPTextEncode
    input: text
  source_image:
    node_id: "57"
    expected_class_type: LoadImage
    input: image
  frame_length:
    node_id: "55"
    expected_class_type: Wan22ImageToVideoLatent
    input: length
```

## 选择器
优先级：
1. explicit `node_id`
2. 唯一 `class_type`
3. `class_type + _meta/title` 辅助定位

若 class_type 出现多次且没有可区分条件，必须报 `AMBIGUOUS_BINDING`。

## 白名单修改
Skill 只能改 binding 声明的 input。
模型加载器、采样器、VAE、custom node 链等默认视作 workflow 作者的“已验证基础设施”，不能因为语言模型觉得“更好”就擅自改。

## 两种 JSON
- UI workflow JSON：用于界面保存，包含节点位置、连线、group 等。
- API workflow JSON：用于 `/prompt` 执行，核心形态为 node-id keyed `{class_type, inputs}`。

Skill 的最终执行目标是 API workflow JSON。
