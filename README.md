# AI Cinematic Director / Character Embodiment

这是当前工程包的统一入口。工程本身不再把历代版本记录、迁移说明和旧 Release Notes 堆在根目录；**当前版本只在 `VERSION` 与 `SKILL.md` frontmatter 中保留一份机器可读版本信息**。

## 核心生产链

```text
用户创意 / 剧本
→ 角色与视觉约束
→ shot_spec
→ 分镜 / approved still
→ video_shot_plan
→ 工作流能力选择
→ 已验证的 ComfyUI UI Workflow
→ Export Workflow (API)
→ 语义绑定 + 白名单参数 patch
→ /object_info 预检
→ /prompt 执行
→ WebSocket / History 监控
→ 视频 QA / 修复 / 拼接
```

## 当前能力

- 电影导演、分镜、摄影、构图、连续性、剪辑、空间、美术、服装、光色、声音规则。
- 角色具象化：人格 / 原型 → 体型、轮廓、面部、姿态、服装、道具、颜色与镜头表现。
- 单镜头与多镜头 `shot_spec` 体系；LOCKED 描述符保持与连续性验证。
- ComfyUI 官方 Workflow Template 学习、模板依赖检查、UI Workflow 与 API Workflow 分离。
- Workflow API：节点 `class_type / inputs` 检查、白名单 patch、拓扑保护、`/object_info` 预检、图片上传、`/prompt` + WebSocket 执行。
- LTX-2 工作流智能：I2V、T2V、首尾帧、首中尾帧、GGUF、低显存、IC-Control、音频、V2V、V2A 等能力路由。
- Appvikalabs LTX-2 工作流案例仅作为工程学习语料；生产权威仍是用户本机已跑通并导出的 API Workflow。

## 主要目录

- `SKILL.md`：总路由、硬规则与执行策略。
- `compiler/`：从导演语义到生成参数的编译规则。
- `references/`：导演、角色、美术、剪辑、色彩、声音等知识核心。
- `templates/`：`shot_spec`、视频计划、工作流绑定等结构模板。
- `validators/`：字段、连续性、绑定与执行前验证规则。
- `video_engine/`：ComfyUI 视频执行、官方模板、LTX-2 选择/绑定/QA。
- `tools/`：模板检查、API 工作流检查、预检、执行与 LTX-2 分析工具。
- `tests/`：结构、解析、绑定、API 与最终格式回归测试。
- `case_library/`：可选视觉案例层，不是中立核心的默认规则来源。
- `evaluation/`：单镜头 / 多镜头质量评分与验收。
- `distribution/`：公开发布与本地资产分离策略。

## 根目录文件

根目录只保留当前状态所需文件：

- `README.md`
- `SKILL.md`
- `SOURCES.md`
- `VERSION`
- `FINAL_FORMAT_CONTRACT.md`
- `PACKAGE_MANIFEST.md`
- `BUILD_AUDIT.md`
- `ASSET_STORAGE_POLICY.md`

不再保留旧 `RELEASE_NOTES_*`、`MIGRATION_*`、历代 `BUILD_AUDIT_*` 或带版本号的知识文件名。

## 版本规则

版本号只承担机器识别与兼容性用途：

1. `VERSION` 保存当前版本。
2. `SKILL.md` YAML frontmatter 的 `version` 必须与 `VERSION` 一致。
3. ZIP 文件名、根目录名、知识文档名默认不再携带版本号。
4. 后续升级直接在同一最终工程格式上迭代，不重新制造历史文件堆积。

## 生产原则

**不要让 GPT 从零猜一整张 ComfyUI 节点图。**

默认路线是：

1. 选择官方或已验证的工作流；
2. 在用户环境中确认可以运行；
3. 导出 `Workflow (API)`；
4. Skill 识别可绑定字段；
5. 只修改白名单输入；
6. 用 `/object_info` 校验当前机器节点接口；
7. 执行并读取真实错误；
8. 通过镜头 / 序列 QA 后再进入拼接。

社区工作流、案例库、书籍规则和 AI 推论必须保持来源层级，不得替代用户本机真实可运行工作流。
