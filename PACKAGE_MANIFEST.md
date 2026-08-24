# Package Manifest

## 核心入口

- `SKILL.md` — 当前有效的总路由与硬规则。
- `README.md` — 工程用途、生产链和目录说明。
- `SOURCES.md` — 来源与证据层级。
- `VERSION` — 唯一机器可读版本号。
- `FINAL_FORMAT_CONTRACT.md` — 长期稳定包格式。
- `BUILD_AUDIT.md` — 当前包的结构与解析审计。
- `ASSET_STORAGE_POLICY.md` — 资产去重、分发和本地引用策略。

## 功能层

- `compiler/` — Prompt / shot / workflow 编译。
- `references/` — 创作与视觉规则。
- `templates/` — 生产数据结构。
- `validators/` — 规则与字段验证。
- `adapters/` — ComfyUI / 模型适配。
- `video_engine/` — 视频工作流选择、绑定、执行与 QA。
- `tools/` — 工程工具脚本。
- `tests/` — 回归测试。
- `evaluation/` — 质量评分卡。
- `case_library/` — 可选案例研究。
- `distribution/` — 分发清理与本地资产策略。

## 清理策略

工程根目录不保存历代版本文件；知识文件名也不再携带工程版本尾缀。历史信息不参与当前运行时决策。
