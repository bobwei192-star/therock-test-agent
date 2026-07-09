# TheRock Test Agent

这是一个面向 TheRock ROCm 测试的 OpenCode 项目级 overlay。

核心分工：

- OpenCode 负责接收指令、调用命令、解释结果。
- `.opencode/tools/therock_agent.sh` 负责确定性执行、状态落盘、日志和报告。
- `docs_this_project/` 提供组件排序、需求、汇总报告模板和单组件问题模板。

## 1. 安装到 TheRock 目录

在本项目目录执行：

```bash
cd /home/zx/TheRock_CI测试流程/therock-test-agent
./install.sh /home/zx/TheRock_CI测试流程/TheRock
```

安装内容：

- `.opencode/`
- `docs_this_project/`
- `.env_example`
- 如果目标目录没有 `.env`，会创建 `.env`

OpenCode 会自动发现当前工作目录下的 `.opencode/`，不需要修改或 clone OpenCode 源码。

## 2. sudo 策略

不要把 sudo 密码写入 `.env`。

可选策略：

```bash
THEROCK_SUDO_POLICY=none
THEROCK_SUDO_POLICY=cache
THEROCK_SUDO_POLICY=ask
```

如果使用 `cache`：

```bash
cd /home/zx/TheRock_CI测试流程/TheRock
sudo -v
opencode
```

runner 只会检查 `sudo -n true`，不会读取或保存 sudo 密码。

## 3. OpenCode 常用运行方式

进入 TheRock 目录：

```bash
cd /home/zx/TheRock_CI测试流程/TheRock
opencode
```

先跑一个轻量组件：

```text
/therock-run /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build gfx1151 hiprand quick
```

跑全部组件的 `quick`：

```text
/therock-run /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build gfx1151 all quick
```

跑全部组件、全部测试类型：

```text
/therock-run /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build gfx1151 all
```

参数含义：

- 第 1 个参数：`ARTIFACTS_PATH`
- 第 2 个参数：`THEROCK_AMDGPU_FAMILIES` / `AMDGPU_FAMILIES`
- 第 3 个参数：组件列表，可选，逗号分隔；传 `all` 表示全部组件
- 第 4 个参数：测试类型，可选，例如 `quick`；不传则使用 `quick,standard,comprehensive,full`
- 第 5 个参数：GPU risk 策略，可选，默认 `skip`

高风险 GPU reset 任务默认跳过，也就是默认等价于：

```text
/therock-run /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build gfx1151 all quick skip
```

如果确实要执行高风险任务，需要显式传第 5 个参数。

直接混入执行：

```text
/therock-run /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build gfx1151 all quick include
```

更推荐隔离执行：

```text
/therock-run /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build gfx1151 all quick quarantine
```

`quarantine` 的含义是：普通任务先跑，高风险任务排到最后单独跑。

## 4. 直接调用 runner 验证

如果想绕过 OpenCode，先验证 shell runner：

```bash
cd /home/zx/TheRock_CI测试流程/TheRock
.opencode/tools/therock_agent.sh init \
  --artifacts /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build \
  --amdgpu-families gfx1151 \
  --components hiprand \
  --test-types quick
```

全部组件 quick：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "$(pwd)" \
  --artifacts /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build \
  --amdgpu-families gfx1151 \
  --components all \
  --test-types quick
```

全部组件、全部测试类型：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "$(pwd)" \
  --artifacts /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build \
  --amdgpu-families gfx1151 \
  --components all
```

真正执行：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "$(pwd)" \
  --artifacts /home/zx/TheRock_CI测试流程/TheRock/output-linux-portable/build \
  --amdgpu-families gfx1151 \
  --components hiprand \
  --test-types quick
```

## 5. 查看日志和报告

如果 runner 成功创建 run，输出在：

```text
runs/<run_id>/
```

常看文件：

```text
runs/<run_id>/global_state.json
runs/<run_id>/agent_activity.jsonl
runs/<run_id>/tool_calls.jsonl
runs/<run_id>/environment_summary.json
runs/<run_id>/summary_report.md
runs/<run_id>/logs/
runs/<run_id>/failures/
```

单任务日志示例：

```text
runs/<run_id>/logs/hiprand-quick.round1.stdout.log
runs/<run_id>/logs/hiprand-quick.round1.stderr.log
```

如果连 run 都没创建，例如 artifacts 路径错误，也看全局调用审计：

```text
runs/_audit/agent_invocations.jsonl
```

这个文件记录 OpenCode / runner 何时被调用、参数、cwd、环境摘要、成功或失败原因。

## 6. 恢复中断 run

OpenCode 内：

```text
/therock-resume <run_id>
```

或直接调用：

```bash
.opencode/tools/therock_agent.sh resume <run_id>
```

恢复依赖：

- `runs/<run_id>/global_state.json`
- `runs/<run_id>/logs/`
- `runs/<run_id>/agent_activity.jsonl`

如果 GPU reset 后机器状态不健康，先处理系统状态，再恢复。

## 7. 重新生成报告

OpenCode 内：

```text
/therock-report <run_id>
```

或直接调用：

```bash
.opencode/tools/therock_agent.sh report <run_id>
```

报告模板来源：

- 汇总报告：`docs_this_project/汇总测试报告.md`
- 单组件失败报告：`docs_this_project/问题模板.md`

## 8. 常见问题

### artifacts 路径不存在

错误表现：没有生成 `runs/<run_id>/`，或 `_audit` 里记录 artifacts 校验失败。

确认路径里有：

```text
dist/rocm/
```

支持的路径形态：

```text
/output-linux-portable/build
/output/build
/path/to/build/dist/rocm
```

### OpenCode 要求 shell 权限

这是正常行为。首次执行 `.opencode/tools/therock_agent.sh` 时可以选 `Allow once`。确认命令可信后，再按需选择 `Allow always`。

### sudo cache 不可用

如果 `.env` 里是：

```bash
THEROCK_SUDO_POLICY=cache
```

需要先执行：

```bash
sudo -v
```

否则 runner 会失败并在 `_audit` 中记录原因。

### 任务被 skipped

常见原因：

- `component_sort_order.json` 中 `status=exclude`
- `gpu_hang_risk=true` 且默认 `--gpu-risk skip`

## 9. 本地自测

在 agent 项目目录执行：

```bash
cd /home/zx/TheRock_CI测试流程/therock-test-agent
tests/test_install_overlay.sh
tests/test_therock_agent.sh
```

这两个测试不依赖真实 GPU，用 mock artifacts 和 mock runner 验证安装、状态、日志、报告、resume 和高风险 skip。
