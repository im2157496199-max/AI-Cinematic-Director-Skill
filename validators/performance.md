# Performance Validator

目标：检查角色是否在“执行行为”，而不是只摆出结果式情绪。

## Checks

1. **Objective clarity**
   - 角色当前想让谁做什么？
2. **Action target**
   - action verb 是否有对象？
3. **Playable behavior**
   - 是否存在姿态 / 手部 / 视线 /移动 / 接触 / 道具任务？
4. **Result-direction risk**
   - 是否只写 angry / scared / seductive / mysterious 等形容词？
5. **Physical task**
   - 当表演僵硬时，是否可加入真实身体任务？
6. **Prop physical life**
   - 重要道具是否被角色实际使用，而非展示？
7. **Subtext**
   - 台词字面与可见意图是否允许存在差异？
8. **Moment-to-moment**
   - 连续镜头是否有真正事件 / beat 变化，而非同一情绪重复？
9. **Blocking motivation**
   - 人物移动是否有故事 / 心理动机？
10. **Reaction timing**
   - 反应是否来自当前刺激，而不是提前摆好反应？

## Output

- PASS
- WARN
- FAIL

失败时优先修正：
`objective -> action verb -> physical task -> blocking -> visible behavior`

不要直接追加更多情绪形容词。
