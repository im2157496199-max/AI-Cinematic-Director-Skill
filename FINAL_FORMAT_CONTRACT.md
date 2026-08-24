# Final Package Format Contract

本文件定义长期稳定的最终工程包格式。后续迭代默认保持此结构。

## 1. 包与根目录

- ZIP 文件名默认不含版本号：`AI-character-embodiment-ltx2-final.zip`
- ZIP 内只允许一个顶层根目录：`AI-character-embodiment-ltx2-final/`
- 当前版本只写入 `VERSION` 与 `SKILL.md` frontmatter
- 根目录不得堆积历代 Release Notes、Migration、旧 Build Audit

## 2. 必需根文件

- `README.md`
- `SKILL.md`
- `SOURCES.md`
- `VERSION`
- `FINAL_FORMAT_CONTRACT.md`
- `PACKAGE_MANIFEST.md`
- `BUILD_AUDIT.md`
- `ASSET_STORAGE_POLICY.md`

## 3. 必需目录

- `compiler/`
- `adapters/`
- `references/`
- `templates/`
- `validators/`
- `tests/`
- `tools/`
- `video_engine/`
- `evaluation/`
- `case_library/`
- `distribution/`

## 4. 命名规则

- 知识文件名、核心规则文件名、索引文件名默认不带 `v0.x` / `v1.x` 版本尾缀。
- 如需记录来源本身的产品版本（例如模型官方名称），允许保留来源自己的版本号；不得把工程版本号混入知识文件名。
- 历史变更信息不作为根目录常驻文件；需要时由 Git 历史或单独外部发布记录承担。

## 5. SKILL 规则

- `SKILL.md` 第一字节必须是 YAML frontmatter 起始 `---`。
- frontmatter `version` 必须等于 `VERSION`。
- `SKILL.md` 保留当前有效能力与执行规则，不重复堆叠历代版本章节。

## 6. 解析与卫生检查

发布前必须验证：

- 全部 JSON 可解析。
- 全部 YAML 可解析。
- 全部 Python 可编译。
- 无 `__pycache__` / `.pyc`。
- 无嵌套 ZIP。
- 无临时解压目录或第三方源仓库整包。
- ZIP CRC 完整性通过。
- 文档引用不存在明显死链。
- UI Workflow 不可直接当 API Workflow 提交。

## 7. 第三方工作流与资产

- 第三方工作流可用于学习、分析、哈希、能力 catalog 和 binding 研究。
- 若许可不明确，不在分发包中重新打包原始第三方 JSON / 媒体资产。
- 生产执行以用户本机已跑通工作流、Export Workflow (API)、`/object_info` 与真实回归结果为权威。
