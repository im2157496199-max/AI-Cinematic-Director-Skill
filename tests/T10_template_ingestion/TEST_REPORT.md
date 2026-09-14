# T10 Template Ingestion — Test Report

## Purpose

验证当前 Template ingestion 工具不会把“文件可解析”误报成“工作流可运行”，并覆盖 flat UI workflow 与 subgraph UI workflow 两种结构。

## Fixtures

- `tests/fixtures/ui_template_basic_i2v.json`：最小 flat I2V UI/template fixture。
- `tests/fixtures/ui_template_subgraph_i2v.json`：最小 subgraph fixture，含 promoted controls 与 proxyWidgets 形态。

这些 fixture 是测试夹具，不冒充 Comfy-Org 官方模板快照。

## Assertions

- Workflow JSON 0.4 可识别。
- `properties.models` 可抽取，不虚构缺失 URL/目录。
- `LoadImage` 类输入资产可登记。
- subgraph instance 能按 definitions 中的 subgraph id 识别，不误报成第三方节点。
- nested subgraph model dependencies 能递归抽取。
- promoted controls / proxyWidgets 只能作为候选绑定线索；不能直接当生产 API binding。
- gate 的 PASS 仅代表静态结构门槛通过。
- profile 在无真机证据时必须保持 `production_ready: false`。

## Result

`T10 PASS: flat + subgraph template inspection/gate/profile`

## Not proven by this test

- 模型文件真实存在；
- 模板在用户 GPU/ComfyUI 版本上可运行；
- UI workflow 已正确转换为 API workflow；
- 任何视频已经实际生成；
- 角色一致性或视频质量已经通过视觉评分。
