# PROMPT_COMPILER.md — Semantic Priority Compiler

## 目的

在保留信息压缩能力的同时，解决多镜头生成的冲突：

> 单镜需要压缩。
>
> 多镜需要稳定。
>
> 因此：可压缩的是“说明”，不可随意压缩的是“身份锁”。

Compiler 不是导演。
它负责**信息选择、可视化转译、身份锁注入与压缩**。

---

## Pass 0 — Resolve Runtime Context

读取：
- task type
- scene owner
- current dramatic block
- current narrative beat
- fulcrum relevance
- previous shot end_state
- entity_sheet
- adapter target

如果是 SINGLE_IMAGE，可跳过跨镜状态继承。
如果是 MULTI_SHOT_SEQUENCE，entity_sheet 与 previous_shot_state 不可省略。

---

## Pass 1 — Inject LOCKED Descriptors

对于当前镜头出现的每个实体：

从 `entity_sheet` 注入：
- locked_descriptor
- locked costume anchors
- locked prop anchors
- location anchors
- project style locks

规则：
1. 不用同义词“润色” LOCKED descriptor。
2. 不因 Prompt Compression 删除身份关键点。
3. 不把 variable state 写进永久 identity。
4. adapter 可以改变语法形式，但不能改变语义。

---

## Pass 2 — Extract Visual Claims

把 Director Spec 拆成 visual claims。

例：
```text
“她想阻止他离开，但又不愿显得慌张。”
```

可转为：
```yaml
objective: keep_him_here
action_target: man
body_block: near_exit_path
gaze: on_man
posture: controlled
hands: one_hand_near_door_or_path
facial_intensity: restrained
```

注意：
objective 本身不是 Final Prompt 必写文字；
Compiler 要寻找它对应的可见行为。

---

## Pass 3 — Performance Translation

优先使用：
- action verb
- physical task
- prop interaction
- body orientation
- gaze
- distance
- contact
- gesture
- reaction state

警惕 Result Direction：
```text
very scared
extremely angry
mysterious
dangerous
```

如这些是用户明确要求的风格 / 情绪标签，可以保留少量；
但必须尽量有具体可见锚点支撑。

---

## Pass 4 — Priority Classification

### P0
丢失即改变故事或实体身份。

### P1
丢失会破坏读图顺序、构图、blocking、关系或 POV。

### P2
丢失会降低摄影 / 美术完成度。

### P3
世界丰富度与次要装饰。

LOCKED identity anchors 默认至少 P0/P1，不能自动降级为 P3。

---

## Pass 5 — Visual Executability

标记：
- DIRECT_VISIBLE
- RELATIONAL_VISIBLE
- TEMPORAL_NEEDS_TRANSLATION
- ABSTRACT_NEEDS_TRANSLATION
- PERFORMANCE_NEEDS_TRANSLATION
- ADAPTER_DEPENDENT
- NON_VISUAL_CONTEXT

`PERFORMANCE_NEEDS_TRANSLATION` 示例：
```text
objective: make_him_stay
subtext: don't abandon me
```

可能转为：
```text
she occupies the path to the exit,
keeps her gaze on him,
one hand remains on the door frame,
her posture is controlled rather than openly pleading
```

---

## Pass 6 — Salience Plan

重要对象设置：
```yaml
narrative_importance:
initial_salience:
discoverability:
screen_area:
depth_layer:
occlusion:
local_contrast:
focus_priority:
```

隐藏主体不因“描述很多”自动变成第一视觉中心。

---

## Pass 7 — Relation Plan

优先提取：
```yaml
gaze:
movement:
orientation:
blocking:
proximity:
depth:
action_target:
prop_interaction:
```

多角色用 `subjects[]` 和明确关系边，避免每个人独立描述后关系丢失。

---

## Pass 8 — Continuity Inheritance

如果存在 previous shot：

先继承：
- identity locks
- costume locks
- prop ownership
- damage / dirt
- screen direction（按 continuity_mode）
- action phase
- environment state

再应用当前镜允许改变的 variable state。

若发生无解释跳变，向 validator 报 WARN / FAIL，不自动脑补修复。

---

## Pass 9 — Positive Contrast

关键缺失状态先找正向对比，再由 adapter 视能力加入 negative conditioning。

---

## Pass 10 — Compression

删除顺序：
1. 重复同义词
2. 对当前镜无影响的背景解释
3. P3 次要装饰
4. 多个表达同一摄影效果的词
5. 无法视觉验证的文学句
6. adapter 不支持的控制语法

不得删除：
1. 当前镜 P0
2. 当前镜关键 P1
3. LOCKED identity anchors
4. 本镜核心 action / blocking / relation
5. 解决当前失败模式所需 P2

---

## Pass 11 — Final Lint

检查：
- scene owner 清楚吗？
- 当前 beat / event 清楚吗？
- 主角是谁？
- 人物是在做事，还是只“演形容词”？
- 谁对谁采取什么行动？
- 道具有没有被真实使用？
- 第一眼看什么？第二眼看什么？
- 多角色关系是否明确？
- LOCKED identity 是否完整？
- 有没有和上一镜无理由漂移？
- 隐藏元素是否写得过于显眼？
- 当前模型专用语法是否只存在于 adapter 层？

通过后才交给 adapter。


### Character Embodiment Prompt Handoff
When the task centers on a designed character, compile in this order: identity -> role -> base trait -> secondary trait/contradiction -> visible behavior -> archetype-visible consequences -> face/hair/silhouette -> color hierarchy -> costume attitude -> gesture/pose -> camera/light. Do not emit archetype labels without visible translation.


## LOCKED Descriptor Runtime Rule ()

LOCKED descriptors are data, not memory.

Every shot compilation MUST receive the original locked descriptor block from entity_sheet as an explicit input.
The compiler may:
- arrange order
- attach camera/action/context
- shorten only when a declared compression rule exists

The compiler may NOT:
- paraphrase locked identity text
- replace with synonyms
- reconstruct from previous conversation memory

Source priority:
entity_sheet locked_descriptor > shot_spec variable state > style/camera instructions.


# Field Mapping — Character Embodiment -> shot_spec

When `character_embodiment_spec` exists, map visible behavior into the matching subject before prompt compression:

| character_embodiment_spec | shot_spec.subjects[] / shot fields |
|---|---|
| scene_intent.current_objective | objective |
| scene_intent.action_verb | action_verb |
| scene_intent.relationship_target | action_target / relationship edge |
| face_behavior.gaze_target | gaze_target |
| face_behavior.head_angle | visible_state.head_angle |
| upper_body.torso_lean / torso_twist | visible_state.body_pose |
| hand_behavior.prop_interaction | prop_interaction |
| full_body.motion_phase | visible_state.motion_phase |
| full_body.line_of_action | visible_state.line_of_action |
| camera_handoff.framing | frame.shot_size / framing |
| camera_handoff.camera_height_relation | camera.placement |

Mapping is explicit. Do not improvise a different field name when a canonical destination exists.

# Video Handoff
PROMPT_COMPILER ends at the approved still prompt.
It does **not** write arbitrary video workflow JSON.
After still approval, hand off to `video_engine/SHOT_TO_VIDEO_COMPILER.md`.
