# MONSTER_HUNTER_ROUTER.md

用途：
把怪物猎人案例库变成可直接调用的工作流。

## 路由规则
### A. 用户要“原创怪物 / 原创魔物”
优先调用：
- creature_library/CREATURE_DNA_LEARNINGS.md
- prompt_templates/T01_creature_concept_prompt.md
- validators/V01_creature_quality_checklist.md

### B. 用户要“生态场景 / 生物栖息地 / 可探索地图”
优先调用：
- environment_library/ENVIRONMENT_AND_ECOLOGY_LEARNINGS.md
- prompt_templates/T02_ecology_environment_prompt.md
- validators/V02_environment_quality_checklist.md

### C. 用户要“怪物素材风装备 / 盔甲 / 武器”
优先调用：
- equipment_library/WEAPON_ARMOR_TRANSLATION_RULES.md
- prompt_templates/T03_monster_to_equipment_prompt.md
- validators/V03_equipment_quality_checklist.md

### D. 用户要“像怪猎，但不是直接同款”
先问内部四件事：
1. 生态位是什么
2. 行动方式是什么
3. 攻击方式是什么
4. 装备/阵营/玩家交互是什么
然后再选模板。

## 绝对禁止
- 只写“很帅的龙”“很酷的怪物”这种空提示词
- 只堆尖刺、骨头、发光特效，不解释功能
- 只模仿外观，不建立生态逻辑
