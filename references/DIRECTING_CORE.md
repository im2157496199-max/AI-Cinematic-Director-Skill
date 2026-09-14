# DIRECTING_CORE.md

> 作用：补齐偏摄影 / 分镜而缺少真正导演与表演调度的问题。
>
> 本文件只保存适合 runtime 的导演规则。原 PDF 不作为 runtime dependency。

## Sources

- S6 — Nicholas T. Proferes, *Film Directing Fundamentals: From Script to Screen*（用户提供 PDF）
- S7 — Judith Weston, *Directing Actors: Creating Memorable Performances for Film and Television*（用户提供 PDF）

标记：
- `SOURCE_EXPLICIT`：书中明确原则
- `SOURCE_SYNTHESIS`：由同一书多处内容综合
- `AI_ADAPTATION`：为了 AI 图像 / 视频生成而做的工程翻译，不冒充原书原话

---

## D01 — 先做剧本侦查，再设计镜头
**类型**：PRINCIPLE / REQUIRED  
**来源**：S6 / SOURCE_EXPLICIT

导演先明确故事、人物处境、行动与场景功能，再进入 staging / camera。
镜头不是第一步。

**AI_ADAPTATION**：
用户给一句故事时，先生成 Director Analysis，再生成 Shot Spec。

---

## D02 — Whose Film / Whose Scene
**类型**：DECISION_GUIDE / REQUIRED（剧情任务）  
**来源**：S6 / SOURCE_EXPLICIT

整部作品主要情感投资对象与当前场景的体验中心可以不同。
当前镜头应明确观众最需要贴近谁的体验。

**AI_ADAPTATION**：
写入 `scene_owner`，供 camera planner 决定主客观距离与信息分配。

---

## D03 — 区分 Dramatic Block / Narrative Beat / Acting Beat
**类型**：ARCHITECTURE / REQUIRED（多镜头）  
**来源**：S6 / SOURCE_EXPLICIT

- Dramatic Block：场景较大的戏剧阶段
- Narrative Beat：足以形成明显升级 / 转向的导演层动作单位
- Acting Beat：演员更细的 moment-to-moment 单位

不要把每个 acting beat 都自动拆成一个镜头。

---

## D04 — 找 Fulcrum
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S6 / SOURCE_EXPLICIT

为场景识别最关键的叙事支点 / 转向。
Staging 与 Camera 可围绕它建立强调、延迟、空间变化或镜头变化。

**AI_ADAPTATION**：
`sequence_spec.fulcrum` 决定哪些镜头负责 build-to / fulcrum / aftermath。

---

## D05 — Staging 必须有叙事任务
**类型**：VALIDATOR / REQUIRED  
**来源**：S6 / SOURCE_EXPLICIT

人物移动可用于：
- 呈现动作
- 物理化内在状态
- 表达人际关系
- 介绍空间 / 道具
- 调整空间分离
- 为长段落组织注意力
- 给动作加“标点”

禁止只为了“画面热闹”而无动机走位。

---

## D06 — 心理关系可转成空间关系
**类型**：PRINCIPLE / DEFAULT  
**来源**：S6 / SOURCE_SYNTHESIS

靠近、远离、阻隔、并肩、对峙都能把关系变化物理化。

**AI_ADAPTATION**：
优先使用 `relationship_geometry` 而非只写“关系越来越亲密”。

---

## D07 — 重要空间先做 Floor Plan
**类型**：WORKFLOW / OPTIONAL  
**来源**：S6 / SOURCE_EXPLICIT

当空间、人物路线或镜头连续性重要时，先用俯视空间关系组织：
- 门 / 窗 / 固定家具
- 人物起点与终点
- 关键道具
- 视线与夹角
- 距离变化

**AI_ADAPTATION**：
同一结构可复用于室内 / 家具展示模式。

---

## D08 — Camera is Narrator
**类型**：PRINCIPLE / REQUIRED  
**来源**：S6 / SOURCE_EXPLICIT

摄影机选择必须完成叙述任务，而不是只记录表演。

设计镜头时先问：
- scene owner
- moment essence
- required information
- reveal / entrance
- spatial orientation
- motif

---

## D09 — Subjective Camera 不等于普通 POV
**类型**：REFERENCE_FACT / DEFAULT  
**来源**：S6 / SOURCE_EXPLICIT

POV 可以只是空间上的“角色看到什么”。
Subjective camera 更深地改变叙述声音，使观众进入人物感知 / 内在体验。

---

## D10 — Reveal 是信息控制
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S6 / SOURCE_EXPLICIT

重要人物、危险或信息不必一出现就完全展示。
Reveal 的价值来自“何时、以谁的体验、以多少信息量让观众知道”。

---

## P01 — 禁止只给 Result Direction
**类型**：VALIDATOR / REQUIRED（表演任务）  
**来源**：S7 / SOURCE_EXPLICIT

不要只指导：
- 更害怕
- 更愤怒
- 更性感
- 更神秘

这些只是结果，不是可执行行为。

---

## P02 — 使用 Playable Direction
**类型**：PRINCIPLE / REQUIRED  
**来源**：S7 / SOURCE_EXPLICIT

优先：
- verbs
- facts
- images
- events
- physical tasks

**AI_ADAPTATION**：
把抽象情绪编译为姿态、动作、视线、接触、阻挡、使用道具。

---

## P03 — Objective 与 Action Verb
**类型**：ARCHITECTURE / REQUIRED（人物冲突）  
**来源**：S7 / SOURCE_EXPLICIT

- Objective：角色想让对方做什么
- Action Verb：角色正在对对方做什么以达到目标

例：
`objective: make_him_stay`
`action_verb: threaten / persuade / block / comfort`

---

## P04 — Spine 与单场 Objective 分开
**类型**：REFERENCE_FACT / DEFAULT  
**来源**：S7 / SOURCE_EXPLICIT

Spine 是更长程驱动力。
Objective 是当前场景的可执行目标。

**AI_ADAPTATION**：
Spine 进入 Character / Entity 层；Objective 进入 Shot / Scene 层。

---

## P05 — Moment 是 Event，不是 Feeling
**类型**：PRINCIPLE / REQUIRED  
**来源**：S7 / SOURCE_EXPLICIT

优先设计：
- win
- loss
- discovery
- choice
- mistake

而不是连续多个镜头只升级“更害怕”。

---

## P06 — Transition 用行为变化表达
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S7 / SOURCE_SYNTHESIS

转折可通过：
- 动作动词改变
- 身体任务变化
- 起身 / 放下物件 / 转头 / 拉开距离
体现。

---

## P07 — Listening / Reaction 关系
**类型**：VALIDATOR / DEFAULT  
**来源**：S7 / SOURCE_EXPLICIT

双人戏不是两个独立角色轮流表演。
一个人的反应应被另一个人的行为影响。

**AI_ADAPTATION**：
检查 gaze / orientation / reaction state / timing 是否形成关系。

---

## P08 — Subtext 与字面台词分开
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S7 / SOURCE_EXPLICIT

相同台词可以承载不同真正意图。
不要机械地让表情复制对白表面情绪。

---

## P09 — Physical Task 让人物脱离摆拍
**类型**：WORKFLOW / DEFAULT  
**来源**：S7 / SOURCE_EXPLICIT

人物表演僵硬时，给一个简单、真实、可完成的身体任务。

**AI_ADAPTATION**：
这是生成自然姿态、手部动作和环境互动的首选修复工具。

---

## P10 — 重要道具必须进入 Physical Life
**类型**：VALIDATOR / REQUIRED  
**来源**：S7 / SOURCE_EXPLICIT

人物不是“拿着道具”就够了。
应存在看、摸、判断、使用、依赖、回避等关系。

---

## P11 — Blocking 与内在状态相连
**类型**：PRINCIPLE / REQUIRED  
**来源**：S7 + S6 / SOURCE_SYNTHESIS

Blocking 应物理化角色关系与场景事件。
和 D05 联合使用。

---

## P12 — 先 Scene Structure，再漂亮镜头
**类型**：ARCHITECTURE / REQUIRED  
**来源**：S6 + S7 / SOURCE_SYNTHESIS

推荐链：
```text
Scene Event
-> Character Objective
-> Action Verb
-> Narrative Beat
-> Blocking
-> Camera Narration
-> Shot
-> Prompt
```

这条是导演层与 Prompt Compiler 的接口。
