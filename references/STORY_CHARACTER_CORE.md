# STORY_CHARACTER_CORE.md

> 作用：把“故事怎么成立”和“人物为什么会这样行动”接到现有导演 / 分镜 / 摄影流程之前。
>
> 本文件只保留适合 runtime 的规则；原书不作为 runtime dependency。

## Sources

- S8 — David Corbett, *The Art of Character: Creating Memorable Characters for Fiction, Film, and TV*（用户提供 EPUB）
- S9 — John Truby, *The Anatomy of Story: 22 Steps to Becoming a Master Storyteller*（用户提供 PDF）

标记：
- `SOURCE_EXPLICIT`：书中明确提出
- `SOURCE_SYNTHESIS`：同一书多个段落综合
- `AI_ADAPTATION`：为了 AI 漫画 / 动画 / 视频工作流而做的工程翻译

---

# A. Character Construction — David Corbett

## C01 — 人物不能靠标签堆出来
**类型**：PRINCIPLE / REQUIRED  
**来源**：S8 / SOURCE_EXPLICIT

“冷酷、傲娇、聪明、善良”只能是标签，不能单独构成人物。人物必须通过欲望、受阻、选择、行为与关系被看见。

**AI_ADAPTATION**：
角色卡至少要能回答：`want -> obstacle -> adjustment/action -> consequence`。

---

## C02 — 五个角色支点
**类型**：ARCHITECTURE / DEFAULT  
**来源**：S8 / SOURCE_EXPLICIT

Corbett 的五个核心支点：
1. desire / need / want
2. frustration / difficulty getting it
3. contradiction
4. vulnerability / wound
5. secret / hidden layer

它们是检查点，不是机械打勾模板。

---

## C03 — Desire puts character in motion
**类型**：PRINCIPLE / REQUIRED（剧情人物）  
**来源**：S8 / SOURCE_EXPLICIT

人物必须想要什么。欲望越重要，受阻后越容易逼出真实选择、适应和变化。

**AI_ADAPTATION**：
区分：
- life_desire：长程想要什么
- story_desire：本故事主要追求什么
- scene_objective：当前场景想让谁发生什么变化

---

## C04 — 受阻后的应对方式定义人物
**类型**：PRINCIPLE / REQUIRED  
**来源**：S8 / SOURCE_SYNTHESIS

人物真正有个性的地方不是“他想要什么”，而是**得不到时他怎么调整**。

优先记录：
- persuade
- hide
- attack
- bargain
- withdraw
- joke
- obey outwardly / resist inwardly
- protect while denying care

---

## C05 — Contradiction 不是随机反差萌
**类型**：VALIDATOR / REQUIRED  
**来源**：S8 / SOURCE_EXPLICIT

人物可以矛盾，但矛盾应该和经历、欲望、社会身份、恐惧或防御有关。

禁止：为了“复杂”随机拼接互相矛盾的性格词。

---

## C06 — Wound / Vulnerability 必须影响现在
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S8 / SOURCE_EXPLICIT

创伤或脆弱点只有在它改变当前选择、关系或防御方式时才值得进入角色 Bible。

**AI_ADAPTATION**：
不默认给所有人物塞悲惨童年。

---

## C07 — Secret 产生隐藏层与 Subtext
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S8 / SOURCE_EXPLICIT

人物隐藏的事实、欲望、羞耻或自我欺骗，会让公开行为和真实动机之间形成张力。

---

## C08 — Biography 用“发生过的场景”而非信息表堆砌
**类型**：WORKFLOW / DEFAULT  
**来源**：S8 / SOURCE_EXPLICIT

与其填几十个履历字段，不如构造少数真正改变人物的过去事件，并写清这些事件如何形成今天的行为习惯。

---

## C09 — Physical / Psychological / Sociological 只保留有行为后果的部分
**类型**：FILTER / REQUIRED  
**来源**：S8 / SOURCE_SYNTHESIS

身体、心理与社会背景都能塑造人物，但若一个信息既不影响选择、关系、语言，也不影响视觉身份，则默认降级为 P3 / reference-only。

---

## C10 — Quirk / Tic / Habit 是识别符，不是装饰品
**类型**：DECISION_GUIDE / OPTIONAL  
**来源**：S8 / SOURCE_EXPLICIT

习惯动作、口头禅、特殊小动作可以增强角色识别度，但必须克制，最好与人物内部逻辑有关。

---

## C11 — 同一个人在不同关系里可以完全不同
**类型**：PRINCIPLE / REQUIRED（群像 / 对话）  
**来源**：S8 / SOURCE_SYNTHESIS

不要让人物对朋友、上级、陌生人、敌人、晚辈都用同一套态度。

**AI_ADAPTATION**：
Character Bible 保存 `relational_modes`，对不同关系可覆写语气和行为策略。

---

## C12 — Voice 由态度、欲望与背景共同产生
**类型**：PRINCIPLE / REQUIRED（有对白）  
**来源**：S8 / SOURCE_EXPLICIT

人物声音不是“加口头禅”这么简单。用词、句长、节奏、直接程度、回避方式与攻击方式应由其欲望、教育、阶层、职业、地区、关系和当下情绪共同形成。

---

## C13 — Dialogue is action
**类型**：PRINCIPLE / REQUIRED  
**来源**：S8 / SOURCE_EXPLICIT

台词不是资料交换。每句主要台词最好能解释为一个动作：诱导、拒绝、试探、挑衅、遮掩、哄骗、施压、求和、转移。

---

## C14 — Scene Test：压力中验证人物
**类型**：VALIDATOR / DEFAULT  
**来源**：S8 / SOURCE_SYNTHESIS

检查角色在以下情境是否产生可区分行为：
- 被拒绝
- 被羞辱
- 失败
- 危险
- 诱惑
- 被夸奖
- 面对弱者
- 面对权威

如果所有角色反应都可互换，人物还没有立住。

---

# B. Story Construction — John Truby

## S01 — Story 是有机系统，不是把公式压上去
**类型**：PRINCIPLE / REQUIRED  
**来源**：S9 / SOURCE_EXPLICIT

人物、结构、主题、世界、象征、情节与场景应该互相定义；不要把外部“三幕模板”机械套在任何故事上。

**AI_ADAPTATION**：
结构工具用于发现内在逻辑，不作为固定镜头数量或固定时长公式。

---

## S02 — Premise 先压成一句话
**类型**：WORKFLOW / REQUIRED（从零写故事）  
**来源**：S9 / SOURCE_EXPLICIT

Premise 是角色 + 启动事件 / 行动 + 故事方向的最短表达。它是后续人物、情节、主题和世界设计的共同起点。

---

## S03 — 找 Designing Principle
**类型**：ARCHITECTURE / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

Premise 说明“发生什么”；Designing Principle 说明“这个故事以什么独特内部逻辑展开”。

可来自：
- journey / transformation process
- time structure
- storyteller device
- recurring comparison
- central metaphor / symbol

不要先选套路，再逼故事去撞模板 beat。

---

## S04 — 在正式写前识别 Promise 与 Story Challenge
**类型**：WORKFLOW / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

每个 premise 都天然承诺一些观众期待，也带有独特难题。先列出：
- 观众因为这个点子最想看到什么？
- 这个点子最容易在哪里失真、无聊、重复或断裂？

---

## S05 — 七个最小结构步骤
**类型**：ARCHITECTURE / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

最小结构：
1. weakness / need
2. desire
3. opponent
4. plan
5. battle
6. self-revelation
7. new equilibrium

**AI_ADAPTATION**：
短片、漫画短篇、10–20 秒概念视频可压缩或隐含部分步骤；不要为了齐七步塞无意义镜头。

---

## S06 — 从 Self-Revelation 反推 Need
**类型**：WORKFLOW / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

当故事有角色变化时，可以先确定结尾人物真正意识到什么，再反推开头的 weakness / need，使变化有方向。

---

## S07 — Need 与 Desire 必须分开
**类型**：VALIDATOR / REQUIRED  
**来源**：S9 / SOURCE_EXPLICIT

- Need：人物内部必须克服 / 学会的东西，通常不在表层
- Desire：人物外部追求的具体目标，推动行动线

两者不能混成一个字段。

---

## S08 — Psychological Need 与 Moral Need 分开
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

- psychological：主要伤害 / 限制人物自己
- moral：人物的弱点会伤害其他人

不是每个轻量故事都需要强 moral arc，但如果存在，就要通过行动表现，而不是演讲。

---

## S09 — Opponent 必须是“必要的对手”
**类型**：PRINCIPLE / REQUIRED（冲突故事）  
**来源**：S9 / SOURCE_EXPLICIT

最佳对手不是随便挡路的人，而是最能攻击主角核心弱点、并在深层目标上与主角发生直接竞争的人。

对手可以比主角更善良，也可以是朋友、爱人或制度的一部分。

---

## S10 — Character Web：人物通过比较才被定义
**类型**：ARCHITECTURE / REQUIRED（群像）  
**来源**：S9 / SOURCE_EXPLICIT

不要孤立设计主角。比较：
- weakness
- psychological / moral need
- desire
- values
- power / status / ability
- 对中央问题的不同回答

人物差异来自关系和价值冲突，而不是“每人再加两个随机特点”。

---

## S11 — Four-Corner Opposition 用价值观拉开角色
**类型**：DECISION_GUIDE / OPTIONAL  
**来源**：S9 / SOURCE_EXPLICIT

需要强群像时，可选主角、主要对手和两个次要力量形成四角对立。重点不是套 archetype，而是让四者对同一问题给出尽可能不同的价值回答。

---

## S12 — Ally 也应有自己的 Desire
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

配角最快获得“完整人格感”的办法之一，是给他自己的目标，而不是只当主角的说明书。

---

## S13 — Subplot 必须反照并影响 Main Plot
**类型**：VALIDATOR / OPTIONAL  
**来源**：S9 / SOURCE_EXPLICIT

副线最好让另一个人物面对与主角相近的问题、产生不同结果，并最终影响主线。否则它只是第二个故事，拖慢 narrative drive。

---

## S14 — Theme / Moral Argument 主要靠行动结构表达
**类型**：PRINCIPLE / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

不要让角色当作者观点的喇叭。主题通过人物追求目标、伤害 / 帮助别人、做出选择及承担后果体现。

---

## S15 — Story World 是故事结构的可见外壳
**类型**：PRINCIPLE / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

世界不是漂亮背景。自然环境、人工空间、技术与时间可以把人物弱点、对手力量、压迫 / 自由与故事变化物理化。

**AI_ADAPTATION**：
这条直接连接 Production Design / Architecture / Color & Light 模块。

---

## S16 — Visual Seven Steps
**类型**：DECISION_GUIDE / OPTIONAL  
**来源**：S9 / SOURCE_EXPLICIT

需要强视觉变化时，可以给主要结构节点分配不同 subworld：
- weakness world
- desire world
- opponent world
- apparent defeat / temporary freedom
- visit to death
- battle world
- freedom / slavery world

不是每部作品都要七套场景；短片可压缩为 2–4 个视觉状态。

---

## S17 — Symbol Web：少量、成网、重复时变化
**类型**：DECISION_GUIDE / OPTIONAL  
**来源**：S9 / SOURCE_EXPLICIT

象征应从 premise、character web、theme、story world 生长出来。避免给每个人贴一堆符号。

重复符号时应改变细节或语境，使其随故事发展，而不是机械复读。

---

## S18 — 22 Steps 是脚手架，不是公式
**类型**：REFERENCE / OPTIONAL  
**来源**：S9 / SOURCE_EXPLICIT

长篇可使用更细的 22-step plot scaffolding；长度越短越应压缩。不要为了“22步齐全”破坏故事的自然发展。

---

## S19 — Revelation Sequence 单独检查
**类型**：VALIDATOR / DEFAULT（悬疑 / 反转 / 信息驱动）  
**来源**：S9 / SOURCE_EXPLICIT

Reveal 应：
1. 逻辑上可被人物 / 观众获得
2. 总体强度逐渐上升
3. 越靠后密度通常越高

Reversal 是让此前信息整体获得新解释的强 reveal，不应无铺垫硬翻桌。

---

## S20 — Scene Weave 是完整剧本前的最后结构层
**类型**：WORKFLOW / REQUIRED（多场景故事）  
**来源**：S9 / SOURCE_EXPLICIT

先列所有 scene，并标记结构步骤 / plotline / theme / reveal 的落点，再写完整台词和细节。

**AI_ADAPTATION**：
Scene Weave 可以直接转换为 Manga chapter / storyboard sequence / video shot-group 输入。

---

## S21 — Scene 先确定谁的 Desire 在驱动
**类型**：ARCHITECTURE / REQUIRED  
**来源**：S9 / SOURCE_EXPLICIT

每场戏明确：
- character arc position
- scene purpose
- driver
- scene desire / endpoint
- opponent
- plan
- conflict escalation
- twist / reveal（若有）

场景驱动者不一定是整部故事的主角。

---

## S22 — 尽可能晚进入 Scene
**类型**：DECISION_GUIDE / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

不要从无效寒暄和进门坐下开始。只保留让观众理解冲突所必需的最短 setup。

---

## S23 — Subtext 是选择，不是强制高级感
**类型**：VALIDATOR / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

只有当人物因为害怕、疼痛、羞耻、欺骗或策略而不能直说时，subtext 才真正有效。

---

## S24 — 先让 Action 成立，再写 Dialogue
**类型**：WORKFLOW / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

先检查无台词版本是否能看懂人物行动与冲突，再叠加对白。不要让对白承担本该由结构完成的工作。

---

## S25 — Dialogue 分层且 Voice 必须区分人物
**类型**：PRINCIPLE / DEFAULT  
**来源**：S9 / SOURCE_EXPLICIT

Truby 的 dialogue 分层可简化为：
- plot/action layer
- value/moral layer
- recurring key words / images / thematic layer

最终仍必须通过角色独特 voice 表达，而不是所有人都说“作者的台词”。

---

# C. 合并后的最小运行链

```text
USER IDEA
  ↓
PREMISE
  ↓
DESIGNING PRINCIPLE (when useful)
  ↓
STORY CORE
  ├─ weakness / need
  ├─ desire
  ├─ opponent
  ├─ plan
  ├─ battle / decisive conflict
  ├─ self-revelation
  └─ new equilibrium
  ↓
CHARACTER BIBLE
  ├─ desire
  ├─ frustration / defenses
  ├─ contradiction
  ├─ vulnerability / wound
  ├─ secret
  ├─ relational modes
  └─ voice / habits
  ↓
CHARACTER WEB
  ↓
SCENE WEAVE
  ↓
DIRECTOR ANALYSIS
  ↓
PERFORMANCE / STAGING / CAMERA
  ↓
MANGA / SHOT / IMAGE / VIDEO DESIGN
  ↓
PROMPT COMPILER
```

## Runtime discipline

1. 不要求每次任务填满所有字段。
2. 短任务只加载能改变输出的规则。
3. 角色的“具体视觉风格”仍由 project style / reference images 决定，本文件不规定日漫、写实、美漫或任何默认画风。
4. 故事结构与人物心理规则不能直接膨胀进最终 Prompt；它们先生成可见行动、场景与镜头决策。


## McKee Scene / Value-Turn Layer

Use this layer after the premise / character logic exists and before Director Analysis.

### Scene event test
A narrative scene should normally contain:
- a value at stake
- an opening charge/state
- conflict
- a meaningful turn
- a changed closing charge/state

If nothing meaningful changes, the scene needs a different dramatic function or should usually be merged/cut.

### Gap engine
For active characters:

```text
DESIRE
  ↓
ACTION based on expectation
  ↓
REALITY reacts differently / more strongly
  ↓
GAP
  ↓
NEW INFORMATION / PRESSURE
  ↓
NEW DECISION
  ↓
NEW ACTION
```

This is a useful anti-generic engine for AI-written stories because it prevents:
`character decides -> plan works exactly as expected -> next scene`.

### Story movement scale

```text
BEAT
behavior exchange / action-reaction
  ↓
SCENE
meaningful value turn
  ↓
SEQUENCE
several scenes culminating in a stronger turn
  ↓
ACT / LARGE MOVEMENT
major irreversible-or-near-irreversible shift
  ↓
STORY CLIMAX
decisive, final value change
```

Do not automatically map one Beat to one shot or one manga panel.

### Macro pressure
When useful, track:

```text
Inciting Incident
-> Progressive Complications
-> Crisis Dilemma
-> Climax
-> Resolution
```

For short work, these can be compressed or implied.

### True Character test
Characterization is surface identity.
True character is tested by a consequential choice under pressure.

A contradiction creates dimension only when it remains coherent with:
- desire
- values
- fear / vulnerability
- relationship
- current pressure

Randomly adding opposite traits is not character depth.

### Exposition rule
Story information should ride inside:
- conflict
- pursuit
- investigation
- relationship behavior
- visual evidence
- consequence

Do not create a dialogue exchange whose only purpose is to explain facts both characters already know.
