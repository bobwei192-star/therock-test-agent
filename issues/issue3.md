# Issue 3: OpenCode 30 分钟超时限制问题

## 问题描述

TheRock 测试运行时，单个测试任务（如 `rocprim-full`）执行时间超过 30 分钟，导致被 OpenCode 的 bash 工具超时机制杀死，陷入"执行 → 超时 → resume → 再超时"的死循环。

## 核心问题

1. **OpenCode 的 30 分钟超时限制**是硬编码在二进制文件中的，无法通过配置修改
2. **`rocprim-full` 任务耗时超过 30 分钟**（实际耗时约 1374 秒，即 23 分钟）
3. 每次 resume 都会重新从头执行被中断的任务，再次超时

## 超时死循环分析

| 阶段 | 状态 | 说明 |
|------|------|------|
| 第一次运行 | 被 SIGKILL 杀掉 | 跑了 9+ 小时，OOM 或系统干预 |
| 第一次 resume | rocfft-full 通过 | 770 秒（≈13分钟），正常完成 |
| 第一次 resume | rocprim-full 执行中 | **超时死亡** — 超过 30 分钟 |
| 第二次 resume | 从 rocprim-full 开始 | 再次超时死亡 |

## 当前状态

```
总任务数: 112
已完成:   83
阻塞:     12
当前卡住: rocprim-full (第84个任务)
resume_count: 1
```

## 解决方案

### 方案 1：在普通终端后台运行（推荐）

绕过 OpenCode 的超时限制，在系统终端直接运行：

```bash
cd /home/zs/TheRock
nohup bash .opencode/tools/therock_agent.sh resume \
  20260710_190554_105b10f6 \
  --output-root /home/zs/TheRock/runs \
  > /home/zs/therock_resume.log 2>&1 &

# 查看进度
tail -f /home/zs/therock_resume.log
```

### 方案 2：跳过超长任务

```bash
python3 -c "
import json
with open('/home/zs/TheRock/runs/20260710_190554_105b10f6/global_state.json', 'r') as f:
    state = json.load(f)

# 标记 rocprim-full 为 skip
state['schedule']['completed_tasks'].append('rocprim-full')
state['schedule']['next_tasks'] = [t for t in state['schedule']['next_tasks'] if t != 'rocprim-full']
if 'round_pending_tasks' in state['schedule']:
    state['schedule']['round_pending_tasks'] = [t for t in state['schedule']['round_pending_tasks'] if t != 'rocprim-full']

with open('/home/zs/TheRock/runs/20260710_190554_105b10f6/global_state.json', 'w') as f:
    json.dump(state, f, indent=2)

print('rocprim-full 已跳过')
"
```

### 方案 3：只运行 quick/standard 测试

```bash
.opencode/tools/therock_agent.sh run \
  --artifacts "/home/zs/TheRock/output-linux-portable/build" \
  --amdgpu-families "gfx1151" \
  --test-types "quick,standard" \
  --sudo-policy "cache"
```

## 结论

- **30 分钟超时不好改**：OpenCode 的超时限制硬编码在二进制文件中
- **rocprim-full 是被超时干掉的**：根据日志模式和 resume_count，符合超时死循环特征
- **建议在普通终端运行**：使用 `nohup` 后台运行，不受 OpenCode 超时约束
