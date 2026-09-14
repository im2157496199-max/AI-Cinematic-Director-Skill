# Continuity Validator

先读取：
`continuity_mode`

- `conventional`：运行完整检查
- `intentional_discontinuity`：检查断裂是否为设计所需
- `experimental`：只检查用户明确要求的匹配项

## conventional checks

1. **identity continuity**
   - face / hair / species marks
   - body anchors
   - locked costume anchors
   - signature prop anchors
2. costume continuity
3. prop ownership / handoff
4. visible damage / dirt / wetness
5. screen direction
6. action axis / reorientation readability
7. eyeline
8. blocking / position continuity
9. movement / action phase
10. environment state
11. time / light logic
12. literal POV logic
13. editability

只锁定**会被观众看见且影响匹配**的状态。

## State inheritance rule

```text
previous_shot.end_state
        ↓
current_shot.start_state
```

除 `allowed_state_changes` 外，LOCKED identity 与已建立的 visible state 不应无理由改变。

## Identity drift

以下视为高风险：
- 同一角色脸型 / 发型 / 种族标志明显改变
- 服装主色 / 主结构无解释改变
- 标志性配件消失
- reference identity 与新镜头角色不匹配
- 同一地点固定结构突然变化

输出：
- PASS
- WARN
- FAIL
- INTENTIONAL_BREAK


## Video clip continuity
For an I2V sequence also check:
- approved still identity survives the first generated frames
- intended action phase progresses rather than resets mid-clip
- prop does not morph / teleport
- fixed environment geometry does not drift in a way that breaks the cut
- clip end_state remains compatible with the next shot start_state
- camera motion does not accidentally reverse established screen direction unless intended
