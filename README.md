# TheRock Test Agent

`therock-test-agent` 是一个面向 ROCm/TheRock 多组件测试的 OpenCode 项目级 overlay。它不修改 OpenCode 源码，不把测试状态放在聊天上下文里，而是把 OpenCode 的交互、权限和解释能力，与一个确定性的本地 Python runner 组合起来，用于执行 TheRock 组件测试、重跑失败集、生成报告和保留全过程审计。

本 README 按 GitHub 对 README 的推荐组织：说明项目做什么、为什么有用、如何开始、主要目录和文件作用、如何运行与排障。

## 目录

- [项目定位](#项目定位)
- [核心特点](#核心特点)
- [项目结构](#项目结构)
- [主要目录与文件](#主要目录与文件)
- [快速开始](#快速开始)
- [运行测试](#运行测试)
- [sudo 策略](#sudo-策略)
- [输出产物](#输出产物)
- [恢复与报告](#恢复与报告)
- [本地自测](#本地自测)
- [常见问题](#常见问题)
- [更多文档](#更多文档)

## 项目定位

TheRock 的组件测试覆盖 CTest、GoogleTest、pytest 和组件专用测试脚本。手动测试时，常见问题是组件入口不统一、环境变量容易遗漏、失败重跑成本高、GPU reset 风险难控、sudo 权限策略不清晰、报告和日志分散。

本项目将这些问题收敛到一个可审计的本地 runner 中：

- OpenCode 负责接收用户指令、选择策略、调用 runner、解释结果。
- Python runner 负责参数解析、任务计划、preflight、执行、状态机、报告和审计。
- TheRock 官方测试脚本仍然是最终测试入口，不重写组件测试逻辑。

典型目标：

- 自动串行执行 TheRock 多组件测试。
- 支持 `quick -> standard -> comprehensive -> full` 分级执行。
- 只重跑失败任务，让失败集逐轮收敛。
- 自动生成汇总报告、失败报告、原始日志和审计记录。
- 对 sudo-sensitive 和 GPU reset 高风险任务提供明确边界。

## 核心特点

- **OpenCode 薄协调，runner 厚执行**：OpenCode 只负责意图、策略和解释；`.opencode/tools/therock_agent/*.py` 承担确定性执行逻辑。
- **配置驱动**：组件顺序、入口脚本、环境 profile、官方排除和风险策略由 JSON 文件控制，避免在 prompt 中猜测。
- **Loop Engineering**：第一轮执行目标任务，后续只重跑失败任务，直到全部通过、失败集稳定或达到最大轮次。
- **状态可恢复**：每次运行生成 `runs/<run_id>/global_state.json`，作为唯一状态源，支持 `/therock-resume`。
- **完整审计**：默认记录 agent 活动、终端命令、tool 调用、wrapper 变更、stdout/stderr、summary 和 failure report，方便审计、复盘和对比人工测试效率。
- **低侵入 wrapper**：默认只生成 `runs/<run_id>/wrappers/*.sh`，不修改 OpenCode、TheRock 源码或 ROCm 构建产物。
- **GPU 风险控制**：默认跳过 `gpu_hang_risk=true` 任务，可通过 `skip/include/quarantine` 显式控制。
- **sudo 安全策略**：支持 `none/cache/askpass`，不把 sudo 密码写入 `.env`、日志或状态文件。
- **鲁棒参数入口**：`/therock-run` 通过 runner 的 `run-kv` 子命令解析 `key=value` 参数，避免 prompt 层误读。
- **内置上游 issue 语料**：随项目维护 TheRock 和 ROCm GitHub issue 资料，方便将测试失败与上游已知问题、硬件限制和构建缺陷做对照。
- **内置 ROCm/AMD 领域词汇**：提供 ROCm、AMD、TheRock 相关专业缩写和组件术语资料，帮助 agent 理解组件含义，提升报告和根因分析的准确性。

## 项目结构

```text
therock-test-agent/
├── .opencode/
│   ├── agents/
│   ├── commands/
│   ├── skills/
│   └── tools/
│       ├── therock_agent.sh
│       └── therock_agent/
├── docs_this_project/
├── scripts/
├── tests/
├── test-results/
├── runs/
├── install.sh
├── .env_example
└── README.md
```

## 主要目录与文件

### `.opencode/`

项目级 OpenCode overlay。安装到 TheRock checkout 后，OpenCode 会自动发现该目录。

| 路径 | 作用 |
|------|------|
| `.opencode/agents/therock-loop.md` | 主协调 agent。解释用户输入、选择 GPU/sudo 策略、调用 runner、总结结果。 |
| `.opencode/agents/therock-executor.md` | 受限执行 agent。校验参数并调用 `.opencode/tools/therock_agent.sh`。 |
| `.opencode/agents/therock-reporter.md` | 报告 agent。读取 `runs/<run_id>/` 产物并总结结果。 |
| `.opencode/commands/therock-run.md` | `/therock-run` 命令定义。使用 `$ARGUMENTS` 调用 `run-kv`。 |
| `.opencode/commands/therock-resume.md` | `/therock-resume` 命令定义。恢复中断 run。 |
| `.opencode/commands/therock-report.md` | `/therock-report` 命令定义。重新生成或读取报告。 |
| `.opencode/skills/therock-testing/SKILL.md` | TheRock 测试领域知识、测试入口、安全边界和风险策略。 |
| `.opencode/tools/therock_agent.sh` | 薄 shell 入口，设置 `PYTHONPATH` 后调用 Python runner。 |

### `.opencode/tools/therock_agent/`

确定性 Python runner。所有状态机和执行逻辑都在这里，不依赖聊天上下文。

| 文件 | 作用 |
|------|------|
| `cli.py` | CLI 编排入口；实现 `init/run/run-kv/init-kv/resume/report`。 |
| `config.py` | 读取 `.env` 和 JSON 配置；拒绝从 `.env` 读取 sudo 密码。 |
| `artifacts.py` | 解析 ROCm artifacts 路径、发现 TheRock repo、检查 sudo 策略。 |
| `planner.py` | 根据组件排序、test type、官方排除和 GPU risk 生成任务队列。 |
| `entrypoint.py` | 解析组件入口、合并 env profile、注入 askpass sudo shim。 |
| `preflight.py` | 执行前检查 artifacts、env、Python 依赖和 sudo 可用性。 |
| `executor.py` | 生成 wrapper、执行任务、写 stdout/stderr、记录 tool calls。 |
| `classifier.py` | 提取失败摘要，检测 hardcoded path 等常见问题。 |
| `reports.py` | 生成 `summary_report.md` 和单组件 failure report。 |
| `state.py` | 读写 `global_state.json`。 |
| `audit.py` | 写入 activity、tool calls、wrapper changes 和全局调用审计。 |

### `docs_this_project/`

项目配置、模板和设计文档。

| 文件 | 作用 |
|------|------|
| `component_sort_order.json` | 决定组件和 test type 的执行顺序、默认状态、GPU hang 风险。 |
| `component_env_script_index.json` | 决定组件测试入口、脚本、环境 profile、依赖和 known issue。 |
| `official_exclude.json` | 记录官方排除、无独立入口或应跳过/阻塞的组件规则。 |
| `汇总测试报告.md` | 汇总报告模板。 |
| `问题模板.md` | 单组件失败报告模板。 |
| `sudo方案.md` | session-scoped sudo askpass 设计。 |
| `需求.md` | 项目需求、状态机、报告和权限边界说明。 |
| `ROCm_TheRock—测试test流程与设计` | TheRock 测试流程和入口背景。 |
| `loop_engineering.md` | 失败集收缩重跑的 loop 设计。 |
| `github_issue_TheRock_repo/` | TheRock 上游 issue 资料，用于比对测试失败和已知问题。 |
| `github_issue_Rocm_repo/` | ROCm 上游 issue 资料，用于比对驱动、runtime、GPU hang、组件缺陷等问题。 |
| `词汇_rocm_all_1000.md` | ROCm/AMD 领域专业缩写词汇资料。 |
| `词汇_rocm_the_rock.md` | TheRock/ROCm 组件术语资料。 |

### `scripts/`

辅助运行脚本。

| 文件 | 作用 |
|------|------|
| `therock-sudo-agent` | session-scoped sudo askpass agent。密码只保存在进程内存中，支持 `start/status/stop/run/askpass`。 |

### `tests/`

本地回归测试，不依赖真实 GPU。

| 文件 | 作用 |
|------|------|
| `test_install_overlay.sh` | 验证安装 overlay、`.env` 安全规则、`run-kv/init-kv` 参数解析、askpass prompt 兼容性。 |
| `test_therock_agent.sh` | 验证任务 loop、resume、官方排除、sudo preflight、wrapper、path hardcode 检测。 |

### `runs/`

运行时输出目录。

| 路径 | 作用 |
|------|------|
| `runs/<run_id>/global_state.json` | 本次 run 的唯一状态源。 |
| `runs/<run_id>/summary_report.md` | 汇总报告。 |
| `runs/<run_id>/logs/` | 每个任务的 stdout/stderr。 |
| `runs/<run_id>/wrappers/` | 每个真实任务生成的执行 wrapper。 |
| `runs/<run_id>/failures/` | 单组件失败报告。 |
| `runs/<run_id>/agent_activity.jsonl` | 任务生命周期和事件记录。 |
| `runs/<run_id>/tool_calls.jsonl` | 命令调用、返回码、耗时和日志路径。 |
| `runs/<run_id>/wrapper_changes.jsonl` | wrapper 和环境变量变更审计。 |
| `runs/_audit/agent_invocations.jsonl` | runner 全局调用审计。 |

### 根目录文件

| 文件 | 作用 |
|------|------|
| `install.sh` | 将 `.opencode/`、`docs_this_project/`、`scripts/` 安装到目标 TheRock checkout。 |
| `.env_example` | 本地环境模板，只允许非敏感配置，不允许 sudo 密码。 |
| `README.md` | 项目入口文档。 |

## 快速开始

### 1. 安装 overlay

在 `therock-test-agent` 项目目录执行：

```bash
cd /home/zx/TheRock_CI测试流程/therock-test-agent
./install.sh /home/zx/TheRock_CI测试流程/TheRock
```

如果需要运行 sudo-sensitive 组件，例如 `amdsmi`，使用 askpass 安装模式：

```bash
./install.sh --setup-sudo-agent /home/zx/TheRock_CI测试流程/TheRock
```

安装后，进入 TheRock checkout：

```bash
cd /home/zx/TheRock_CI测试流程/TheRock
opencode
```

### 2. 运行一个轻量组件

OpenCode 内：

```text
/therock-run artifacts=/home/zx/TheRock_CI测试流程/TheRock/output/build gpu=gfx1151 components=hiprand test_types=quick
```

### 3. 运行 sudo-sensitive 组件

先用 wrapper 启动 OpenCode：

```bash
cd /home/zx/TheRock_CI测试流程/TheRock
./scripts/therock-sudo-agent run -- opencode
```

OpenCode 内：

```text
/therock-run artifacts=/home/zx/TheRock_CI测试流程/TheRock/output/build gpu=gfx1151 components=amdsmi test_types=standard sudo_policy=askpass max_rounds=1 stable_threshold=1
```

## 运行测试

推荐使用 `key=value` 参数。`/therock-run` 会把原始参数交给 runner 的 `run-kv` 子命令做确定性解析。

常用参数：

| 参数 | 说明 |
|------|------|
| `artifacts=<path>` | 必填。ROCm build 目录或 `dist/rocm` 路径。 |
| `gpu=<gfx>` | 必填。例如 `gfx1151`。 |
| `components=<list>` | 可选。逗号分隔；`all` 表示全部组件。 |
| `test_types=<list>` | 可选。默认 `quick,standard,comprehensive,full`。 |
| `gpu_risk=<policy>` | 可选。`skip/include/quarantine`，默认 `skip`。 |
| `sudo_policy=<policy>` | 可选。`none/cache/askpass`，默认读取环境或 `none`。 |
| `max_rounds=<n>` | 可选。最大 loop 轮数。 |
| `stable_threshold=<n>` | 可选。失败集稳定阈值。 |

示例：

```text
/therock-run artifacts=/path/to/output/build gpu=gfx1151 components=all test_types=quick gpu_risk=skip
```

全组件、全 test type，默认跳过 GPU hang 高风险任务：

```text
/therock-run artifacts=/path/to/output/build gpu=gfx1151 components=all test_types=all gpu_risk=skip
```

说明：

- `components=all` 表示按 `component_sort_order.json` 覆盖全部组件。
- `test_types=all` 表示使用默认全集：`quick,standard,comprehensive,full`。不传 `test_types` 也等价于全 test type。
- `gpu_risk=skip` 会跳过 `gpu_hang_risk=true` 的任务，适合日常全量验证；需要覆盖高风险任务时再显式使用 `include` 或 `quarantine`。
- 如果全量测试包含 sudo-sensitive 组件，并且希望获得完整覆盖，可通过 `./scripts/therock-sudo-agent run -- opencode` 启动后追加 `sudo_policy=askpass`。

带 sudo askpass 的全量命令示例：

```text
/therock-run artifacts=/path/to/output/build gpu=gfx1151 components=all test_types=all gpu_risk=skip sudo_policy=askpass
```

直接调用 runner：

```bash
.opencode/tools/therock_agent.sh run-kv \
  artifacts=/path/to/output/build \
  gpu=gfx1151 \
  components=hiprand \
  test_types=quick
```

传统 flags 也可以直接调用：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "$(pwd)" \
  --artifacts /path/to/output/build \
  --amdgpu-families gfx1151 \
  --components hiprand \
  --test-types quick
```

## sudo 策略

不要把 sudo 密码写入 `.env`。

支持三种策略：

| 策略 | 行为 |
|------|------|
| `none` | 默认策略。sudo-sensitive task 直接 `blocked`。 |
| `cache` | 只检查已有 sudo cache，执行 `sudo -n true`。 |
| `askpass` | 使用 session-scoped sudo agent，执行 `sudo -A true` 和临时 sudo shim。 |

`askpass` 模式：

```bash
./install.sh --setup-sudo-agent /home/zx/TheRock_CI测试流程/TheRock
cd /home/zx/TheRock_CI测试流程/TheRock
./scripts/therock-sudo-agent run -- opencode
```

`run -- opencode` 会在启动前提示一次 sudo 密码，OpenCode 退出时自动停止 sudo agent 并执行 `sudo -k`。密码只保存在 `therock-sudo-agent` 进程内存里，不写入 `.env`、日志或状态文件。

## 输出产物

每次运行会生成：

```text
runs/<run_id>/
├── global_state.json
├── environment_summary.json
├── summary_report.md
├── agent_activity.jsonl
├── tool_calls.jsonl
├── wrapper_changes.jsonl
├── logs/
├── wrappers/
├── failures/
└── memory/
```

如果连 run 都没有创建，例如 artifacts 路径错误，查看：

```text
runs/_audit/agent_invocations.jsonl
```

## 恢复与报告

恢复中断 run：

```text
/therock-resume <run_id>
```

直接调用：

```bash
.opencode/tools/therock_agent.sh resume <run_id>
```

重新生成报告：

```text
/therock-report <run_id>
```

直接调用：

```bash
.opencode/tools/therock_agent.sh report <run_id>
```

## 本地自测

在 `therock-test-agent` 项目目录执行：

```bash
cd /home/zx/TheRock_CI测试流程/therock-test-agent
bash tests/test_install_overlay.sh
bash tests/test_therock_agent.sh
python3 -m py_compile .opencode/tools/therock_agent/cli.py scripts/therock-sudo-agent
```

这些测试不依赖真实 GPU，使用 mock artifacts 和 mock command 验证：

- overlay 安装
- Python package 导入
- `run-kv/init-kv` 参数解析
- official exclude
- sudo preflight
- askpass prompt 兼容
- wrapper 审计
- hardcoded path 检测
- resume 和报告生成

## 常见问题

### artifacts 路径不合法

确认路径里有：

```text
dist/rocm/bin
```

支持：

```text
/path/to/output/build
/path/to/output/build/dist/rocm
```

### OpenCode 要求 shell 权限

这是正常行为。首次执行 `.opencode/tools/therock_agent.sh` 时可以选择 `Allow once`。确认命令可信后，再按需选择 `Allow always`。

### sudo askpass agent 不可用

使用 askpass 时推荐从 wrapper 启动 OpenCode：

```bash
./scripts/therock-sudo-agent run -- opencode
```

异常退出时兜底清理：

```bash
./scripts/therock-sudo-agent stop
sudo -k
```

### 任务被 skipped 或 blocked

常见原因：

- `official_exclude.json` 命中官方排除或无入口组件。
- `component_sort_order.json` 中任务状态为 exclude。
- `gpu_hang_risk=true` 且 `gpu_risk=skip`。
- sudo-sensitive task 没有可用 sudo cache 或 askpass agent。
- preflight 发现 artifacts、依赖或必要环境变量缺失。

## 更多文档

- `docs_this_project/需求.md`
- `docs_this_project/ROCm_TheRock—测试test流程与设计`
- `docs_this_project/loop_engineering.md`
- `docs_this_project/sudo方案.md`
- `docs_this_project/汇总测试报告.md`
- `docs_this_project/问题模板.md`
