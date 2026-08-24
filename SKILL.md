---
name: cinematic-director
version: 0.8.3
description: >
  AI 导演 / 角色具象化 / 分镜 / 摄影 / 美术 / 剪辑 / ComfyUI 视频执行 Skill。
  集成官方 Workflow Template / Workflow API 机制与 LTX-2 工作流智能，
  支持能力选择、语义绑定、关键帧、控制、音频、V2V/V2A 路由，
  并以用户本机跑通的工作流与 Export Workflow (API) 作为生产权威。
---


# LTX-2 WORKFLOW INTELLIGENCE

本版本不把第三方工作流“照搬进包”，而是把真实工作流当作**工程案例语料**，提炼成可验证的选择、绑定和迁移规则。生产权威仍是：**用户本机已跑通的工作流 + Export Workflow (API) + `/object_info` + 回归运行**。

```text
SCRIPT / SHOT_SPEC (authoritative)
  ↓
APPROVED STILL / VIDEO_SHOT_PLAN
  ↓
LTX2 REQUIREMENT CLASSIFICATION
  ↓
REFERENCE WORKFLOW FAMILY SELECTION
  ↓
USER-LOCAL WORKING UI WORKFLOW
  ↓
EXPORT WORKFLOW (API)
  ↓
SET/GET SEMANTIC ANCHOR TRACE → MUTABLE SOURCE NODE
  ↓
SAME NODE-ID + CLASS_TYPE MATCH IN API GRAPH
  ↓
/object_info PREFLIGHT
  ↓
TYPED ALLOWLIST PATCH (NO LINK TOPOLOGY MUTATION)
  ↓
RUN → HISTORY/WEBSOCKET → VIDEO QA → EDIT
```

## LTX-2 硬规则

1. `appvikalabs/LTX-2-Workflows` 是**社区参考语料**，不是当前官方 LTX 权威，也不是自动生产模板库；本版本静态解析了 19 个真实 UI workflow，但没有冒充在用户机器上跑过它们。
2. 对 `SetNode/GetNode` 结构，**不得直接覆盖 linked `SetNode` input**。先从 `Set_*` 语义锚点沿 link 回溯到真正可编辑源（如 `INTConstant`、`CLIPTextEncode`、`LoadImage`），再进入 API binding。
3. UI workflow 的节点 ID 只有在对应的 **Export Workflow (API)** 中仍存在且 `class_type` 匹配时，才可转成 binding 候选；随后仍必须通过目标机器 `/object_info`。
4. 关键帧控制按需求升级：start-only → start/end → start/middle/end；姿态、Canny、Depth、音频、voice clone、V2V、V2A 只在镜头需求出现时升级，禁止为了“功能多”默认选择 All-In-One。
5. 简单镜头优先选择更窄、更少节点的已验证 workflow；复杂 workflow 是能力升级路径，不是质量默认值。
6. 参考工作流里的帧数、分辨率、采样器、LoRA、GGUF、低显存写法是**案例值**，不得提升为所有 LTX 版本的硬默认；本机实际 workflow 与运行时契约优先。
7. 第三方仓库未检测到明确 LICENSE，因此最终工程包**不重新分发其原始 workflow JSON**；仅包含派生 catalog、哈希、能力/依赖分析和工具。
8. 最终包目录、命名与校验契约由 `FINAL_FORMAT_CONTRACT.md` 固定；后续迭代默认继承此结构，不随意重排工程骨架。

核心入口：
- `video_engine/ltx2/DEEP_STUDY_REPORT.md`
- `video_engine/ltx2/WORKFLOW_FAMILY_MATRIX.md`
- `video_engine/ltx2/SELECTOR_POLICY.md`
- `video_engine/ltx2/SEMANTIC_BINDING_STRATEGY.md`
- `video_engine/ltx2/CURRENTNESS_AND_MIGRATION.md`
- `tools/ltx2_repo_inspect.py`
- `tools/ltx2_select_profile.py`
- `tools/ltx2_binding_candidates.py`
- `tools/ltx2_ui_to_api_binding.py`
- `tests/T13_ltx2_repo_ingestion/` through `tests/T16_final_format/`


# COMFYUI WORKFLOW API FORMAT CORE

本版本补齐 Template 之后的“真正执行语言”。核心原则：**UI Template 负责选择机器；API export 才是机器实际执行图。**

```text
APPROVED STILL / VIDEO_SHOT_PLAN
  ↓
VERIFIED UI TEMPLATE
  ↓
FILE -> EXPORT WORKFLOW (API)
  ↓
API GRAPH INSPECT
  ↓
/object_info RUNTIME PREFLIGHT
  ↓
UPLOAD APPROVED STILL (/upload/image)
  ↓
SEMANTIC BINDING + TYPED ALLOWLIST PATCH
  ↓
TOPOLOGY SIGNATURE MUST STAY IDENTICAL
  ↓
POST /prompt
  ↓
WEBSOCKET + /history/{prompt_id}
  ↓
VIDEO QA / EDIT
```

硬规则：
1. API graph 节点以 `class_type + inputs` 为执行契约；`_meta.title` 仅用于诊断。
2. 正常编译禁止改 node id / class_type / link topology；只改 binding 白名单里声明的常量输入。
3. 所有节点和 input 名在生产前必须对照目标机器 `/object_info`；记忆中的节点接口不算证据。
4. I2V 的 approved still 必须先进入 ComfyUI input 空间；不得把任意本地 Windows 路径直接塞进远端/不同进程工作流。
5. `/prompt` 返回的 `error/node_errors` 必须保留并定位到 node id/class_type/input，不得自动换成“差不多”的节点。
6. 生产监控默认使用官方示例推荐的 WebSocket + History；HTTP-only 仅用于明确的 submit-and-forget。
7. `executed` 不是每个节点都会发送的完成事件；不能把它误作普遍的 node-done 信号。
8. 当前默认 backend 仍为用户本机 Self-hosted Server API；Comfy API v2/SDK 只登记迁移路径，本版本不冒充已实现。

核心新增：
- `video_engine/api/API_FORMAT_CORE.md`
- `video_engine/api/API_EXECUTION_LIFECYCLE.md`
- `video_engine/api/API_INPUT_ASSET_PIPELINE.md`
- `video_engine/api/API_VALIDATION_AND_ERRORS.md`
- `video_engine/api/API_BACKEND_POLICY.md`
- `video_engine/api/BEGINNER_API_HANDOFF.md`
- `tools/comfy_api_inspect.py`
- `tools/comfy_api_preflight.py`
- `tools/comfy_upload_image.py`
- `tools/comfy_run_api_ws.py`
- `tests/T11_api_format_contract/`
- `tests/T12_api_preflight/`

# OFFICIAL COMFYUI TEMPLATE CORE

本版本把 ComfyUI 官方 Template 系统正式放到“视频决策 → API workflow”之间。

生产链更新为：

```text
VIDEO_SHOT_PLAN
  ↓
TEMPLATE SELECT / SOURCE PROVENANCE
  ↓
UI TEMPLATE INSPECTION
  ├─ workflow JSON version
  ├─ node provenance
  ├─ properties.models
  ├─ assets / custom-node dependencies
  └─ subgraphs / promoted inputs / proxyWidgets
  ↓
USER COMFYUI LOAD + UNCHANGED RUN
  ↓
EXPORT API-FORMAT WORKFLOW
  ↓
SEMANTIC BINDING / MUTABLE ALLOWLIST
  ↓
COMPILE + REGRESSION
  ↓
PRODUCTION I2V
```

硬规则：
1. 官方 Template 提高来源可信度，但**不等于已经在用户机器验证可运行**。
2. UI/Template JSON 与 API execution JSON 必须分开；自动 patch 只绑定真实 API export。
3. Workflow JSON v1.0 是当前文档最新版，但官方仓库仍存在 `version: 0.4` 模板；两类都必须能识别。
4. `definitions.subgraphs` 必须递归分析；与 subgraph id 匹配的 UUID 类型节点不是第三方节点错误。
5. 优先绑定 template 作者暴露的 promoted inputs；不直接依赖脆弱的 `widgets_values` 数组索引。
6. `properties.models` 只作为声明依赖证据；不得捏造模型 URL。
7. 模型缺失弹窗不是绝对判定：官方文档明确指出深层自定义模型子目录可能触发同名检测警告。
8. 不承诺任意 UI JSON 可脱离 ComfyUI 前端/节点定义无损转换为 API JSON。
9. 生产状态最低要求：`RUN_VERIFIED -> API_EXPORTED -> BINDING_VERIFIED -> REGRESSION_PASS`。

核心文件：
- `video_engine/templates/OFFICIAL_TEMPLATE_SYSTEM_CORE.md`
- `video_engine/templates/TEMPLATE_INGESTION_PIPELINE.md`
- `video_engine/templates/UI_API_WORKFLOW_SEPARATION.md`
- `video_engine/templates/TEMPLATE_DEPENDENCY_MODEL.md`
- `video_engine/templates/SUBGRAPH_BINDING_RULES.md`
- `video_engine/templates/OFFICIAL_VIDEO_TEMPLATE_STUDY.md`
- `tools/comfy_ui_template_inspect.py`
- `tools/comfy_template_gate.py`
- `tools/comfy_template_profile.py`
- `tests/T10_template_ingestion/`

# COMFYUI VIDEO EXECUTION CORE

本版本正式补齐此前缺失的“导演意图 → AI 视频决策 → ComfyUI API workflow”中间层。

项目默认视频生产链：

```text
USER INTENT
  ↓
SCRIPT / STORY
  ↓
8-SHOT OR VARIABLE SHOT SEQUENCE
  ↓
CHARACTER / WORLD / VISUAL LOCKS
  ↓
TEXT-TO-IMAGE SHOT STILLS
  ↓
USER APPROVAL GATE
  ↓
IMAGE-TO-VIDEO SHOT PLAN
  ↓
WORKFLOW BINDING
  ↓
COMFYUI API-FORMAT JSON
  ↓
ONE VIDEO CLIP PER SHOT
  ↓
VIDEO QA / CONTINUITY REVIEW
  ↓
EDIT SEQUENCE
```

硬规则：
1. 未获得本镜头 approved still，不进入 I2V 编译。
2. 不从零“幻想” ComfyUI 节点图；优先绑定用户已验证可运行的 API workflow 模板。
3. workflow 的 node id / class_type / input name 必须来自真实导出的 API JSON；不存在的节点或参数标记为 `UNBOUND`，不得编造。
4. `shot_spec` 描述创作意图；`video_shot_plan` 描述机器可执行的时间 / 运动 / 连续性决策；adapter 再将其映射到具体 workflow。
5. 多镜头默认逐镜 I2V 后剪辑，不把 8 镜头一次性当成长视频生成。
6. 用户已经确认的角色 / 服装 / 道具 / 场景锁继续沿用，不因进入视频阶段而重写。

核心文件：
- `video_engine/DIRECTOR_TO_VIDEO_DECISION.md`
- `video_engine/SHOT_TO_VIDEO_COMPILER.md`
- `video_engine/WORKFLOW_BINDING_SYSTEM.md`
- `video_engine/FRAME_TIME_RULES.md`
- `video_engine/CAMERA_MOTION_MAPPING.md`
- `video_engine/SEQUENCE_I2V_PIPELINE.md`
- `adapters/comfyui-api.md`
- `adapters/comfyui-wan-i2v.md`
- `templates/video_shot_plan.yaml`
- `templates/comfyui_workflow_binding.yaml`
- `validators/video_shot_plan.md`
- `evaluation/VIDEO_SHOT_SCORECARD.md`

## FOUR-VOLUME VISUAL CASE LIBRARY

The neutral theory engine includes an optional Blue Archive visual case-study layer for secondary creation, scene design, CG/PV analysis, and anime/commercial visual anchoring.

Core case files:
- `case_library/blue_archive/BLUE_ARCHIVE_FOUR_VOLUME_VISUAL_CORE.md`
- `case_library/blue_archive/CASE_LIBRARY_INDEX.md`
- `case_library/blue_archive/CASE_LIBRARY_AUDIT.md`
- `references/CASE_STUDY_APPLICATION_POLICY.md`
- `templates/blue_archive_case_query.yaml`
- `validators/blue_archive_case_usage.md`

Runtime:
`user reference > named student > school/faction > task case library > neutral theory > default Blue Archive anchor (only if unspecified)`

For derivative work, identity locks are stricter than scene/style freedom.

## CHARACTER EMBODIMENT / PERSONALITY-TO-VISUAL
More complete bridge layer with archetype translation, color hierarchy and empirical anime-character trend validation.

Purpose:
- translate personality and archetype into observable face/body/gesture/clothing/color behavior
- preserve character identity across expression and pose changes
- improve ensemble differentiation and prompt compilation quality

Default:
`identity -> role -> base personality + secondary trait/contradiction -> archetype energy -> visible behavior -> face/hair/silhouette -> color hierarchy -> costume attitude -> pose -> camera -> light -> prompt`

Active files:
- `references/CHARACTER_EMBODIMENT_CORE.md`
- `references/MOE_CHARACTER_APPLICATION.md`
- `references/MOE_EXPRESSION_GESTURE_APPLICATION.md`
- `references/CHARACTER_DIFFERENTIATION_CORE.md`
- `references/CHARACTER_ARCHETYPE_VISUALIZATION_CORE.md`
- `references/CHARACTER_COLOR_DESIGN_CORE.md`
- `references/ANIME_PERSONA_TRENDS_CORE.md`
- `references/raw/21_moe_character_personality_emotion_focused_extraction.md`
- `references/raw/22_moe_gesture_emotion_focused_extraction.md`
- `references/raw/23_moe_character_basic_technique_focused_extraction.md`
- `references/raw/24_wang_archetype_visual_design_focused_extraction.md`
- `references/raw/25_moe_character_basic_technique_color_focused_extraction.md`
- `references/raw/26_pixels_to_personas_focused_extraction.md`
- `templates/character_embodiment_spec.yaml`
- `templates/archetype_visual_spec.yaml`
- `validators/character_embodiment.md`
- `validators/character_color_design.md`

Notes:
- Do not use archetypes as one-line clichés.
- Do not differentiate only by color.
- Empirical trend data informs validation; it never replaces project intent.


## CASE LIBRARY / BLUE ARCHIVE P0
Blue Archive is the project-default high-priority anime/commercial-character visual anchor unless the user specifies another style.

Source:
- Blue Archive Official Artworks Vol.1–4 case library. Vol.1, Vol.3 and Vol.4 include deep image-analysis layers; Vol.2 retains its imported gallery/audit layer.

Core files:
- `case_library/blue_archive/vol1/BLUE_ARCHIVE_VOL1_IMAGE_BY_IMAGE_ANALYSIS.md`
- `case_library/blue_archive/vol1/BLUE_ARCHIVE_VOL1_CHARACTER_DNA.md`
- `case_library/blue_archive/vol1/BLUE_ARCHIVE_VISUAL_DNA_CORE.md`
- `case_library/blue_archive/vol1/BLUE_ARCHIVE_WORLD_VISUAL_SYSTEM_VOL1.md`
- `case_library/blue_archive/vol1/BLUE_ARCHIVE_P0_DEFAULT_POLICY.md`

Public distribution: do not bundle or redistribute third-party copyrighted artwork. Publish analysis/indexes only.
Private local working copies may retain user-supplied reference assets, but they must be excluded from a public release unless redistribution permission is known.


# Cinematic Director / Visual Storytelling Skill

## 0. 核心修正记录

保留的核心能力：
- Semantic Priority
- Visual Executability
- Visual Salience
- Positive Contrast
- Prompt Compression
- Action / Prop Plausibility

系统同时覆盖导演流程、多镜头状态与 Story / Character Construction。

```text
USER INTENT
   ↓
TASK ROUTER
   ↓
STORY CONSTRUCTION (when needed)
   ├─ premise / designing principle
   ├─ need / desire / opponent / plan
   ├─ character web
   ├─ story world / reveal logic
   └─ scene weave
   ↓
CHARACTER CONSTRUCTION (when needed)
   ├─ desire / frustration
   ├─ contradiction
   ├─ vulnerability / secret
   ├─ behavior / relational modes
   └─ voice
   ↓
ART DIRECTION / PRODUCTION DESIGN (when needed)
   ├─ design concept / metaphor
   ├─ research / reference board
   ├─ architecture / space
   ├─ color palette
   ├─ material / texture / age
   ├─ décor / props
   └─ camera-compatible environment
   ↓
MANGA / SEQUENTIAL ADAPTATION (when requested)
   ├─ hook / 5W1H baseline
   ├─ page & panel budget
   ├─ NAME rough pass
   ├─ panel rhythm / importance
   ├─ emotional readability
   └─ panel -> video promotion
   ↓
DIRECTOR ANALYSIS
   ├─ whose film / whose scene
   ├─ circumstance / spine / want
   ├─ dramatic blocks
   ├─ narrative beats
   └─ fulcrum
   ↓
ENTITY / PROJECT LOCKS
   ↓
PERFORMANCE DESIGN
   ├─ objective
   ├─ action verb
   ├─ subtext
   ├─ physical task
   └─ prop / costume physical life
   ↓
STAGING / SPACE
   ├─ blocking
   ├─ relationship geometry
   └─ floor-plan logic when useful
   ↓
CAMERA AS NARRATOR
   ├─ scene owner / audience alignment
   ├─ essence of moment
   ├─ required information
   ├─ reveal / entrance
   └─ spatial orientation
   ↓
SHOT / SEQUENCE DESIGN
   ↓
APPLICABILITY FILTER
   ↓
SEMANTIC PRIORITY
   ↓
VISUAL EXECUTABILITY
   ↓
SALIENCE / RELATION PLAN
   ↓
LOCKED DESCRIPTOR INJECTION
   ↓
PROMPT COMPRESSION
   ↓
MODEL ADAPTER
   ↓
GENERATE
   ↓
EVALUATE / REPAIR
```

原则：
> 导演可以知道很多；Final Prompt 只保留当前镜头真正需要的东西。
>
> 但“跨镜头身份锁定信息”不能被压缩掉或随意改写。

---

# 1. Task Router

## SINGLE_IMAGE
只加载：
- subject / action / environment
- visual hierarchy
- frame / camera
- visible relations
- light / color / material（按需要）
- references / constraints
- Prompt Compiler

默认跳过：
- full scene dramatic blocks
- sequence continuity database
- shot-to-shot state inheritance

如果单图包含人物表演，仍可使用：
- objective
- action verb
- physical task
- subtext（仅在能转译为可见结果时）

## SINGLE_VIDEO_SHOT
在 SINGLE_IMAGE 上增加：
- start_state / end_state
- subject motion phases
- camera motion intent
- target_duration_s
- target_fps（若 workflow 已确定）
- temporal progression
- continuity locks（若接上一镜）
- approved still gate
- source_image_ref
- video_shot_plan_ref

若本镜尚未有用户确认的静帧，只生成导演 / I2V 计划，不生成 ComfyUI API JSON。
具体执行见 `video_engine/SHOT_TO_VIDEO_COMPILER.md`。

## MULTI_SHOT_SEQUENCE
必须增加：
- entity_sheet
- dramatic_blocks
- narrative_beats
- fulcrum
- shots[]
- previous_shot_state inheritance
- identity / costume / prop / environment locks
- POV / viewer placement
- shot flow
- continuity
- coverage
- visual progression

## MUSIC_SOUND / SCORE_DESIGN
动漫 / 游戏 / AI视频统一音乐设计层。理论负责音乐为什么进入、如何服务叙事与镜头；作品OST与设定案例负责审美。

负责：
- narrative / emotional function
- motif / thematic transformation
- diegesis
- music states
- horizontal resequencing / vertical layering
- music-sound-design relationship
- cut / reveal / action synchronization
- dialogue / silence windows
- AI music-generation specification
- OST + picture joint analysis

不负责：
- 固定“动漫和弦公式”
- 强迫任何作品风格
- 乐理学院课程
- Unity / FMOD / Wwise 教程（除非任务明确需要）

核心文件：
- `references/MUSIC_SOUND_CORE.md`
- `references/raw/18_game_music_handbook_kellman_focused_dedup_extraction.md`
- `references/raw/19_anime_music_research_focused_notes.md`
- `references/raw/20_ai_music_generation_2024_2026_research_notes.md`
- `templates/music_design_spec.yaml`
- `validators/music_sound.md`

## EDITING / SEQUENCE_ASSEMBLY
用于多镜头视频 / 漫画关键帧转视频的最终镜头组合。

负责：
- keep / trim / merge / remove
- cut timing
- shot order
- Rule of Six tradeoff
- audience thought / attention
- reaction/subtext cut
- contact-sheet sequence review
- A/B edit hypothesis
- sound/music timing handoff

不负责：
- 剪辑软件教学
- 机械胶片流程
- 音乐作曲

核心文件：
- `references/EDITING_CORE.md`
- `references/raw/17_in_the_blink_of_an_eye_murch_focused_dedup_extraction.md`
- `templates/edit_sequence_spec.yaml`
- `validators/editing.md`

## COSTUME_DESIGN / CHARACTER_WARDROBE
轻量服装设计底座。后续作品设定集 / artbook 才是风格与案例的大头。

负责：costume purpose / story state、silhouette / layer logic、material / drape / movement、signature accessories、style-sheet / multi-view handoff、costume continuity。

不负责：固定历史服装百科、直接决定某个作品画风、3D建模软件教程。

核心文件：
- `references/COSTUME_DESIGN_CORE.md`
- `references/raw/16_costume_design_video_games_focused_dedup_extraction.md`
- `templates/costume_spec.yaml`
- `validators/costume_design.md`

## SPACE_DESIGN / ENVIRONMENT_TOPOLOGY
负责“空间本身怎么成立”：空间关系、围合、开口、动线、尺度、空间层级与重复节奏。

不负责：
- 建筑工程计算
- 黄金比例/模数公式
- 摄影机180度轴线
- 最终美术风格

核心文件：
- `references/SPACE_DESIGN_CORE.md`
- `references/raw/15_architecture_form_space_order_focused_dedup_extraction.md`
- `templates/space_design_spec.yaml`
- `validators/space_design.md`
- `tests/T04_space_design_dual_use.md`

关键原则：
**空间不是背景图。** 先建立“哪里能走、哪里被围合、哪里是主空间、哪里能看出去、尺度靠什么被读出来”，再交给光色和摄影。

## LIGHT_COLOR / PERCEPTION
用于把 Art Direction 的“想要什么感觉”转成光源、色彩关系、材质响应和 atmosphere 逻辑。

原则：
- 不继承 James Gurney 的绘画画风
- 不把老画作当成“好看标准”
- 只提取可迁移的 light/color/perception 规律
- 年轻化 / 动漫 / 游戏 / 潮流审美由用户 reference 与 case library 决定

核心文件：
- `references/LIGHT_COLOR_PERCEPTION_CORE.md`
- `references/LIGHT_COLOR_DEDUP_AUDIT.md`
- `templates/light_color_spec.yaml`
- `validators/light_color.md`

## ART_DIRECTION / PRODUCTION_DESIGN
用于：
- 电影 / 动画 / 漫画的场景与世界视觉设计
- 单图场景的美术指导
- 角色所处空间、道具、材质、色彩的统一
- 室内 / 家具效果图的视觉方向
- 虚拟场景 / AI 场景生成

核心输出：
- `production_design_spec.yaml`
- design concept / metaphor
- research & reference board
- architecture / space
- palette
- material / texture / aging
- décor / props
- camera-compatible environment
- digital / AI execution constraints

完整规则：
- `references/ART_DIRECTION_CORE.md`
- `templates/production_design_spec.yaml`
- `validators/art_direction.md`

Barnwell dedup delta：
- location 可作为 narrative agent / antagonist
- recurring location 的 learned geography 可被剧情有意打破
- real/reference location 必须做 signal curation + stereotype check
- design visibility 可选 supportive / expressive / spectacle-forward
- 按 story order 检查视觉演化与 motif recurrence
- past / present / future 都要检查 temporal identity，而非只做表面风格
- 详细查重记录见 `references/ART_DIRECTION_DEDUP_AUDIT.md`

## MANGA_SEQUENCE / ANIME_STILLS
在 MULTI_SHOT_SEQUENCE 的故事与身份锁定基础上增加：
- manga_sequence_spec
- opening hook
- page / panel budget
- NAME rough pass
- panel importance P0–P3
- panel rhythm / page-turn logic
- emotional reaction panels
- manga spatial continuity
- manga -> video promotion plan

必须明确：
> Beat ≠ Shot ≠ Manga Panel

漫画格优先解决“这个静止瞬间读者看见什么、感受到什么”；
视频镜头再解决“这个瞬间如何在时间中发生”。

完整规则见：
- `references/MANGA_SEQUENTIAL_CORE.md`
- `templates/manga_sequence_spec.yaml`
- `validators/manga_sequential.md`

## MANGA_TO_VIDEO
先完成可读的漫画 / 连续静帧，再选择高价值格子升级：
- P0：关键转折 / reveal / emotional peak，优先升级
- P1：必要动作 / 关系 / 方位，根据连续性升级
- P2：可合并、做桥接或省略
- P3：通常不进入视频

新增运动时不得改变：
- identity
- costume
- key props
- spatial relation
- story result
- emotional meaning

## FILM / CAMPAIGN
再增加：
- authorial POV
- project visual system
- long-range color / space / movement / rhythm progression

## EDIT / REPAIR
优先：
- preserve correct regions
- identify failure type
- local edit / structural control
- avoid full regeneration when unnecessary

---

# 1.5 Story / Character Layer：有故事任务时先把“为什么”建立起来

这层不是所有任务都加载。

对于用户只要一张已有角色的图：跳过。
对于从一句 idea 生成漫画 / 动画短片 / 连续镜头：优先加载。

最小 Story Core：
- premise
- weakness / need
- desire
- opponent / opposing force
- plan / decisive conflict
- change / ending state

最小 Character Core：
- desire
- frustration pattern
- contradiction
- vulnerability / secret（若重要）
- behavior signature
- relational mode
- voice（若有对白）

不要把心理设定直接塞进 Final Prompt。
先把它翻译成：
- decision
- action
- reaction
- blocking
- gaze / distance
- dialogue intent
- visible state change

完整规则见：
- `references/STORY_CHARACTER_CORE.md`
- `templates/story_spec.yaml`
- `templates/character_bible.yaml`
- `validators/story_character.md`

---


# 1.6 Scene Dynamics：场景必须发生“有意义的变化”

对于剧情型场景，在进入导演镜头设计前优先检查：

```text
VALUE AT STAKE
   ↓
OPENING STATE
   ↓
CHARACTER ACTION / EXPECTATION
   ↓
CONFLICT
   ↓
ACTUAL RESULT
   ↓
GAP
   ↓
TURNING POINT
   ↓
CLOSING VALUE STATE
   ↓
NEXT DECISION
```

Story Event 不等于“发生了很多动作”。
如果角色的关键处境、关系、信息、权力、自由、信任等价值从头到尾没有可感知变化，就要质疑这个场景是否有必要。

结构单位不要混淆：
- Beat：行为交换 / action-reaction
- Scene：有意义的 value turn
- Sequence：多个场景累积成更强的转折
- Shot / Manga Panel：视觉呈现单位

因此：
> 一个 Beat 不必等于一个镜头，也不必等于一个漫画格。

宏观上按需要使用：
`Inciting Incident -> Progressive Complications -> Crisis -> Climax -> Resolution`

短动画 / 短漫画允许高度压缩，不为了填模板制造废镜头。

# 1.7 Art Direction / Production Design Layer：把“故事”变成“看得见的世界”

当任务包含场景、世界、室内、建筑、材质、色彩、道具或整体视觉风格时加载。

核心原则：

> **Art Direction ≠ 风格关键词堆叠。**

最小流程：

```text
STORY / CHARACTER / THEME
        ↓
DIRECTORIAL POV / USER INTENT
        ↓
DESIGN CONCEPT
        ↓
REFERENCE / RESEARCH
        ↓
SPACE / ARCHITECTURE
        ↓
COLOR / MATERIAL / TEXTURE
        ↓
DÉCOR / PROPS
        ↓
ATMOSPHERE / PSYCHOLOGY
        ↓
CAMERA / PANEL COMPATIBILITY
```

规则：
1. 场景不能只是“漂亮”；必须服务人物、故事和视角。
2. 先有 design concept，再扩散细节。
3. visual metaphor 可用但不是强制；不要让每个物体都象征化。
4. 真实资料用于**扎根**，而不是把创意锁死。
5. “真实”不是唯一目标：写实、动漫、漫画、表现主义、JOJO式、幻想建筑都可以，只要内部逻辑成立。
6. 每个重要空间都要回答：**它和人物是什么关系？它让观众感觉什么？**
7. 色彩要有戏剧目的，不使用固定“红=危险、蓝=悲伤”硬表。
8. 材质必须有 finish / age / wear / maintenance 逻辑；不要默认所有东西全新无瑕。
9. 建筑要支持 blocking、景别、前中后景、出入口、视线和镜头位置。
10. AI 能生成“不可能空间”不等于可以无结构；仍要守住尺度、深度、材质、空间关系和连续性。
11. 室内/家具效果图可把这层直接作为主要视觉设计模块使用。
12. 具体画风仍由用户 / reference 决定，不继承任何一本书的默认风格。

# 1.8 Manga / Sequential Layer：先把连续静帧做“能读懂”

当任务目标是漫画、动漫静帧、动态漫画前置帧或“先出图再做视频”，加载本层。

最小流程：

```text
STORY / CHARACTER
   ↓
CORE IDEA / PROMISE
   ↓
PAGE / PANEL BUDGET
   ↓
ROUGH SCRIPT
   ↓
NAME / THUMBNAIL PASS
   ↓
PANEL IMPORTANCE + RHYTHM
   ↓
FINAL PANEL SPECS
   ↓
IMAGE GENERATION
   ↓
SELECT KEY PANELS
   ↓
VIDEO SHOTS (optional)
```

核心检查：

1. **第一页 / 前 1–3 格必须有继续看的理由。**
2. **5W1H 是清晰度基线，不是强制“先来一个大远景”。**
3. **重要格尽量同时承载动作 + 人物 + 世界 + 关系 + 气氛。**
4. **漫画格大小 / 密度 / 景别跟随重要性与节奏，不平均分配。**
5. **日本漫画式连续静帧不能只描述身体动作，还要给表情、反应、心理转折足够空间。**
6. **连续动作保持方位清楚；不要为了“镜头多”随机跳轴。**
7. **先做便宜的 NAME，再花算力做最终图。**
8. **漫画格不是视频镜头。只把值得动起来的格子升级。**

荒木方法只作为“地图”，不得把 JOJO 画风、固定页式或某一种漫画语法自动设为默认。
JOJO 风格**可以被显式选择**，也可以作为 style reference / visual reference 使用；只有当用户或项目明确指定时才启用。
具体风格由用户 / 项目 reference 决定。

# 2. Director Analysis：先理解戏，不先选镜头

对于剧情型任务，镜头设计前至少回答：

1. **Whose film is it?** 整体情感投资主要跟谁走？
2. **Whose scene is it?** 当前场景观众应该最贴近谁？
3. **Circumstance** 人物当前处于什么客观处境？
4. **Spine / Want** 人物长期驱动力与当前需求是什么？
5. **Dramatic Blocks** 场景可以分成哪几个明显阶段？
6. **Narrative Beats** 哪些变化足以成为导演层的叙事动作单位？
7. **Fulcrum** 哪个瞬间是整场戏的支点或最大转向？

不要把每个 acting beat 都拆成镜头。
只有当动作产生足够的戏剧升级、方向变化、信息揭示或空间重组时，才优先升级为 narrative beat / shot candidate。

---

# 3. Performance Design：人物要“做”，不是“演形容词”

默认避免纯 Result Direction：

弱：
```text
她非常害怕。
他更愤怒。
她看起来很危险。
```

优先转成 Playable Direction：
- objective：角色想让谁做什么
- action verb：角色正在对谁做什么
- facts：已知事实
- images：感官意象
- events：胜 / 负 / 发现 / 选择 / 错误
- physical tasks：具体身体任务
- subtext：真正意图与字面表达的差异
- physical life：人与道具、服装、环境的真实关系

例：
```text
objective: 阻止对方离开
action_verb: 威胁
physical_task: 一只手挡住门把，另一只手仍压着药箱
subtext: “你再走一步，我就失去控制。”
```

Prompt Compiler 再把这些转换成模型可见的姿态、朝向、接触、距离与动作。

---

# 4. Staging：空间关系就是戏

Blocking 不只是“站哪里”。

优先检查：
- 人物与环境的关系
- 人物与重要物件的关系
- 人物之间的距离
- 谁靠近 / 远离 / 阻挡 / 追随
- 关系变化是否被空间变化物理化
- 运动是否有角色动机，而非“为了画面热闹”

常见关系几何：
```text
apart -> together
together -> apart
approach -> retreat
parallel -> confrontation
blocked -> released
foreground dominance -> shared frame
```

当场景空间对叙事重要时，可使用 floor-plan / bird's-eye 逻辑先设计位置与路径，再设计机位。

---

# 5. Camera as Narrator：摄影机必须有叙述任务

摄影机不是记录器。

每个镜头设计前问：
- whose scene is it?
- 观众应该贴近谁的体验？
- 这个瞬间的 essence 是什么？
- 哪个信息现在必须被看到？
- 哪个信息应该延迟 reveal？
- 哪个人物 / 地点 / 道具必须被介绍或保持“活着”？
- 是否需要建立 / 延续视觉 motif？
- 是否需要重新交代空间关系？

只有回答完这些，再选择：
- shot size
- angle
- placement
- focal-length intent
- movement
- focus
- duration / temporal behavior

主观摄影机与普通 POV shot 不视为同义词：
- subjective camera：改变叙述声音，使观众更深进入角色感知
- POV shot：表示“角色看到什么”的空间近似

---

# 6. Entity / Project Locks

多镜头任务必须先创建 `templates/entity_sheet.yaml`。

LOCKED 信息包括：
- 角色身份描述
- 关键脸部 / 发型 /种族特征
- 服装固定特征
- 必须保持的标志性道具
- 场景固定结构
- 项目固定画风 / 渲染风格 / 画幅

LOCKED descriptor：
- 允许 adapter 转成模型语法
- 不允许 Compiler 重新文学化
- 不允许每镜用不同同义词重写
- 不允许因为压缩 P3 顺手删除

VARIABLE state：
- 表情
- 污损
- 受伤
- 手里拿的临时物
- 朝向
- 动作阶段
- 局部光照状态
- 当前画面是否可见

---

# 7. Director Spec 与 Final Prompt 分离

Director Spec 可以保存：
- 世界 / setting
- 人物背景
- scene owner
- dramatic blocks / beats / fulcrum
- performance intent
- staging
- camera reason
- continuity state
- visual arc
- 备选方案

Final Prompt 不机械继承全部文本。

Compiler 只保留：
1. 当前镜头显著影响画面的信息
2. 当前模型可直接或间接表现的信息
3. 解决当前失败模式所需的信息
4. 所有本镜出现实体的 LOCKED identity descriptors

---

# 8. Semantic Priority

## P0 — Narrative Hook / Non-negotiable
丢失即改变故事或身份：
- 谁是主角
- 正在发生什么
- 核心危险 / 关系
- 必须出现的身份标志
- LOCKED identity anchor

## P1 — Visual Structure
决定观众如何读画面：
- foreground / background
- gaze relation
- screen direction
- shot size / camera placement
- blocking
- hidden vs obvious
- action target
- scene-owner alignment

## P2 — Photographic Realization
- motivated light
- color relation
- depth / focus
- material
- atmosphere

## P3 — Enrichment
- 次要世界细节
- 非关键装饰
- 不影响镜头关系的信息

Compiler：
- 必保 P0
- 高比例保留 P1
- 按需要选择 P2
- 压缩 P3

---

# 9. Visual Executability

对每句话问：

> 模型最终应该画出什么可见结果？

优先：
- 姿态
- 位置
- 朝向
- 接触
- 道具使用
- 明暗
- 材质
- 视线
- 表情
- 尺度
- 对比
- 空间距离

抽象情绪必须尽量经过 Performance Design 再进入 Prompt。

---

# 10. Positive Contrast First

关键特征是“缺失”时，不只写 negative state。

例：
```text
周围衣服：wet reflective fabric
目标衣服：dry matte fabric

周围人：前倾奔跑
目标人：垂直、静止、脚步扎稳
```

Negative Prompt 由 adapter 按能力补充。

---

# 11. Hidden Subject / Reveal Control

“重要”不等于“最大、最亮、最清楚”。

隐藏主体同时定义：
- narrative_importance
- initial_salience
- discoverability
- screen_area
- depth_layer
- occlusion
- local_contrast
- lighting
- gaze relation

Reveal 是导演任务，不只是 prompt 关键词。

---

# 12. Relational Instructions

优先描述：
- A 看 B
- A 背对 B
- A 阻挡 B
- A 靠近 / 远离 B
- A 静止而 B 运动
- A 在 foreground，B 在 background
- A 的动作目标是 B
- A 的身体方向与 gaze 是否一致

多角色镜头必须用 `subjects[]`，不要退回单一 subject 字段。

---

# 13. Still Image Motion Translation

单张图片没有真实时间轴。

时间状态转成可见瞬间：
- static：balanced stance / planted feet / stable axis
- moving：lean / asymmetric stride / cloth trail / direction cue
- transition：姿态或动作已经跨过明显阈值

---

# 14. Human Face Realism

真人 / 写实任务按需要使用：
- natural proportions
- subtle asymmetry
- natural jaw / cheek structure
- realistic skin texture
- restrained makeup
- natural lip / eye texture

不机械堆 pores / vellus hair。
动漫任务交给对应 adapter，不把真人脸规则硬套过去。

---

# 15. Action / Prop / Costume Plausibility

检查：
- 手是否真的使用道具
- 身体重心是否匹配动作
- 道具方向是否与空间相容
- 服装重量 / 限制是否影响动作
- 是否只是为了展示道具而摆 pose
- 重要道具是否与人物发生“关系”，而非只存在

---

# 16. Prompt Compiler 纪律

Final Prompt 前：
1. detect core narrative
2. resolve scene owner
3. resolve current beat / fulcrum relevance
4. inject locked descriptors
5. classify P0/P1/P2/P3
6. convert performance intent into visible action
7. remove redundant synonyms
8. convert abstract statements to visible relations
9. detect hidden-vs-prominent conflict
10. detect static-vs-motion ambiguity
11. detect pose/prop plausibility risks
12. compress non-visible worldbuilding
13. pass clean spec to adapter

Compiler 不得：
- 擅自重新导演
- 改写 LOCKED identity 导致跨镜漂移
- 自动加 shallow DOF / rim light / Dutch tilt
- 自动加 teal-orange
- 自动加质量魔法词
- 在 generic 层加入模型专用权重语法

---

# 17. Multi-shot State Inheritance

每个 shot 结束后生成 `end_state`。

下一镜开始：
```text
previous_shot.end_state
      ↓
continuity inheritance
      ↓
current_shot.start_state
```

至少检查：
- identity
- costume
- prop ownership / hand
- visible damage / dirt
- position / screen direction
- gaze
- action phase
- environment state
- time / light state

只有明确设计为 discontinuity 的字段才允许跳变。

---

# 18. Evaluation

生成后检查：
1. Narrative readability
2. Scene-owner / POV readability
3. Performance readability
4. Visual hierarchy
5. Core relation
6. Spatial logic
7. Pose / prop plausibility
8. Identity continuity
9. Costume / prop / state continuity
10. Hidden-subject discoverability
11. Face / material realization
12. Light / color motivation
13. Model artifacts

失败后只修改导致失败的变量。

---

# 19. Source & Evidence Discipline

电影 / 摄影原则：
`references/MASTER_RULES.md`

导演与表演补充：
`references/DIRECTING_CORE.md`

概念知识：
`references/REFERENCE_FACTS.md`

Prompt Compiler：
`compiler/PROMPT_COMPILER.md`

实战证据：
`tests/`

模型语法：
`adapters/`

书中明确内容标记为 `SOURCE_EXPLICIT` / `SOURCE_SYNTHESIS`。
针对 AI 生成的转换必须标记 `AI_ADAPTATION`。
测试经验只能升级为工程启发式，不能冒充原书规定。


Moegirl Database Reference Layer:
- Use `references/MOEGIRL_ATTRIBUTE_DATABASE_CORE.md` for attribute retrieval and comparison.
- Convert tags into visible behavior, silhouette, costume and expression decisions.
- Never treat database attributes as a complete character design.


Beginner handoff: `video_engine/templates/BEGINNER_TEMPLATE_HANDOFF.md`
