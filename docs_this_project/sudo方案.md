# TheRock Agent sudo 方案：session-scoped askpass

## 目标

TheRock 的部分组件测试需要 sudo 才能覆盖完整功能，例如 `amdsmi` 的 fan、power、overdrive 等读写能力。OpenCode CLI Agent 可能运行在隔离 shell session 中，普通 `sudo -v` cache 不一定能被 agent 内部命令继承。

本方案提供一个无人值守但不落盘密码的方式：

- `install.sh` 不保存 sudo 密码到 `.env`
- 用户在启动测试前输入一次 sudo 密码
- 密码只保存在当前 `therock-sudo-agent` 进程内存中
- runner 通过 `SUDO_ASKPASS` 调用该进程提供的 askpass helper
- 进程退出或执行 `stop` 后密码消失
- 测试过程中不需要再次人工输入 sudo 密码

## 不采用的方案

不采用 `.env + SUDO_PASSWORD`：

- `.env` 是项目文件，容易被 agent、日志、备份、同步工具或同用户进程读取
- wrapper、环境摘要、调试输出可能意外泄漏环境变量
- `chmod 600` 只能降低误读风险，不能改变“明文密码落盘”的事实

不默认采用全局 sudo cache：

- `timestamp_type=global` 依赖系统 sudoers 配置
- OpenCode 内部 shell、TTY、进程模型可能仍导致 cache 不共享

不默认采用宽泛 `NOPASSWD`：

- allowlist 很难覆盖 TheRock 脚本内部真实 sudo 调用
- 配错后可能扩大免密 sudo 范围

## 方案结构

```text
用户终端
  |
  | ./scripts/therock-sudo-agent start
  | 输入 sudo 密码一次
  v
therock-sudo-agent daemon
  - 用 sudo -S -v 验证密码
  - 密码保存在进程内存
  - 监听 ~/.therock/sudo-agent.sock
  |
  | SUDO_ASKPASS=~/.therock/sudo-askpass.sh
  v
TheRock runner
  - sudo_policy=askpass
  - sudo-sensitive task preflight 执行 sudo -A true
  - task PATH 前置 runs/<run_id>/sudo_askpass_bin/sudo
  |
  v
测试脚本内部 sudo
  - 普通 sudo 命令会先命中临时 sudo shim
  - shim 调用真实 sudo -A
  - sudo 调用 askpass helper
  - helper 通过 Unix socket 向 daemon 请求密码
```

## 安装

在 TheRock 测试目录执行：

```bash
./install.sh --setup-sudo-agent /home/zx/TheRock_CI测试流程/TheRock
```

该命令会：

- 复制 `.opencode/`、`docs_this_project/`、`scripts/`
- 创建 `~/.therock/sudo-askpass.sh`
- 设置 `~/.therock` 权限为 `700`
- 设置 askpass helper 权限为 `700`
- 在目标 `.env` 中写入非敏感配置：

```bash
THEROCK_SUDO_POLICY=askpass
THEROCK_SUDO_ASKPASS=/home/zx/.therock/sudo-askpass.sh
THEROCK_SUDO_AGENT_SOCKET=/home/zx/.therock/sudo-agent.sock
```

`.env` 中不会写入 sudo 密码。

## 使用流程

进入 TheRock 目录：

```bash
cd /home/zx/TheRock_CI测试流程/TheRock
```

推荐用 wrapper 启动 OpenCode：

```bash
./scripts/therock-sudo-agent run -- opencode
```

`run -- opencode` 会：

- 启动本次 sudo session
- 输入 sudo 密码一次
- 为 OpenCode 子进程注入 `THEROCK_SUDO_POLICY=askpass`
- OpenCode 退出时自动停止 sudo agent
- 自动执行 `sudo -k`

如需手动检查 session，可另开终端执行：

```bash
./scripts/therock-sudo-agent status
```

在 OpenCode 中运行 sudo-sensitive task：

```text
/therock-run artifacts=/home/zx/TheRock/output/build gpu=gfx1151 components=amdsmi test_types=standard sudo_policy=askpass max_rounds=1 stable_threshold=1
```

正常情况下不需要手动清理。异常退出时可兜底清理：

```bash
./scripts/therock-sudo-agent stop
sudo -k
```

## runner 行为

只有 task 命中 `sudo_sensitive` env profile 时才触发 sudo preflight。

`sudo_policy=none`：

- sudo-sensitive task 直接 `blocked`
- 非 sudo task 不受影响

`sudo_policy=cache`：

- preflight 执行 `sudo -n true`
- cache 可用则继续
- cache 不可用则 `blocked`

`sudo_policy=askpass`：

- preflight 检查 `SUDO_ASKPASS` 是否存在且可执行
- preflight 执行 `sudo -A true`
- askpass agent 可用则继续
- askpass agent 不可用则 `blocked`
- runner 为该 task 生成临时 sudo shim：

```text
runs/<run_id>/sudo_askpass_bin/sudo
```

该 shim 调用真实 sudo：

```bash
sudo -A "$@"
```

这样 TheRock 测试脚本内部的普通 `sudo ...` 也会走 askpass。

## 安全边界

本方案保证：

- 不在 `.env`、state、wrapper、日志中保存 sudo 密码
- askpass helper 文件不包含密码
- Unix socket 位于 `~/.therock`，目录权限 `700`
- socket 权限 `600`
- daemon 检查 Unix socket peer uid，拒绝其他用户请求
- `stop` 后 daemon 退出，socket 和 pid 文件会删除

本方案不保证：

- 无法防止同一用户权限下的恶意进程调试或读取该用户进程内存
- 无法替代系统级最小权限 sudoers allowlist
- 无法修复测试脚本自身执行破坏性 sudo 命令的风险

因此仍建议：

- 只在可信测试机器上使用
- 只在需要 sudo-sensitive 组件时启用
- 优先用 `./scripts/therock-sudo-agent run -- opencode`，让 wrapper 在 OpenCode 退出时自动清理
- 异常退出时再手动执行 `./scripts/therock-sudo-agent stop && sudo -k` 兜底
- 保留 OpenCode shell 权限审核

## 故障排查

### askpass agent 没启动

现象：

```text
sudo_unavailable: THEROCK_SUDO_POLICY=askpass 但 sudo askpass 验证失败
```

处理：

```bash
./scripts/therock-sudo-agent run -- opencode
```

如果需要手动管理 session，再使用：

```bash
./scripts/therock-sudo-agent start
./scripts/therock-sudo-agent status
```

### helper 路径不对

现象：

```text
SUDO_ASKPASS 不存在或不可执行
```

处理：

```bash
./install.sh --setup-sudo-agent /home/zx/TheRock_CI测试流程/TheRock
grep THEROCK_SUDO_ASKPASS /home/zx/TheRock_CI测试流程/TheRock/.env
```

### 密码输错

`start` 阶段会通过 `sudo -S -v` 验证密码。密码错误时 daemon 不会启动。

重新执行：

```bash
./scripts/therock-sudo-agent start
```

### 清理

```bash
./scripts/therock-sudo-agent stop
sudo -k
rm -f ~/.therock/sudo-agent.log
```

如果要撤销配置：

```bash
rm -rf ~/.therock
```

并把目标 `.env` 中的策略改回：

```bash
THEROCK_SUDO_POLICY=none
```
