# Tool Use 层设计

## 1. 背景

`Test Case Agent` 的目标是根据自然语言需求，自动生成、维护、执行和修复 AMD ROCm / AI Model 测试用例。

**Tool Use（Function Calling）层**要解决的问题是：把 Agent 在做"规划→生成→执行→修复"决策时需要的动作拆成稳定、可审计、可组合的工具。

这些工具由 LLM Agent 在推理循环中主动调用，**不是测试脚本运行时的能力**。

### 和 Test Utility 的边界

| 维度 | Agent Tool Use | Test Utility（独立文档） |
|------|----------------|--------------------------|
| 调用者 | LLM Agent 推理循环 | pytest / shell 测试脚本 |
| 触发时机 | 生成代码之前/之后 | 测试执行期间 |
| 返回值消费方 | Agent 的 Memory/State | 测试断言 `assert` |
| 典型用途 | 搜索已有用例、生成脚本、校验语法、调用 AIDevOps、判断入库 | 查询 GPU、下载模型、运行 benchmark、解析日志 |

> 对应 Test Utility 设计详见 [`test_utility测试工具库设计.md`](./test_utility测试工具库设计.md)

---

## 2. 设计边界

### 2.1 `test_case` 的角色

`test_case` 是测试用例仓库和执行框架。

它提供：

- suite / case 发现能力。
- `test_controller.py` 统一执行入口。
- `suites/lib.sh` 公共测试函数。
- `shunit2` 测试框架。
- JUnit XML 和日志产物。
- Docker 运行路径。
- Artifactory 测试产物上传逻辑。

Agent 基于这些能力进行用例生成前的信息检索、脚本生成、执行委托和结果判定。

### 2.2 `rocm-on-radeon` 的角色

`rocm-on-radeon` 是被测 workload 来源。

它提供：

- `model-scripts/` 下大量 AI model 脚本。
- `run.sh` / `run.py` / `inference.py` / `train.py`。
- `requirements.txt`。
- Hugging Face 模型和数据集来源。
- AMD Artifactory 模型、数据集、wheel、工具脚本来源。
- Dockerfile 和 Docker 运行场景。
- ROCm / MIGraphX / vLLM / llama.cpp / ComfyUI 等典型运行模式。

Agent 通过 read/discover 类工具阅读理解这些 workload，再将其映射到 test_case 用例计划。

### 2.3 安全边界

以下动作 Agent 不能直接调用，必须生成代码后由测试脚本或人工执行：

- 下载大模型或全量数据集。
- 访问 gated Hugging Face model。
- 安装系统包。
- 安装或升级 ROCm driver。
- 修改当前 Python 环境。
- clone 外部仓库到项目目录。
- Docker build / Docker run。
- 源码编译。
- overnight benchmark。
- 多 GPU 大模型测试。
- 使用 token、私钥、`.env`、`hf.txt`。

Agent 可以做的是：**生成包含这些操作的代码**，并在生成前检查条件是否满足；**实际执行留给 Test Utility 或人工**。

---

## 3. Agent Tool 总览

### 3.1 发现类工具

| 工具名 | 中文描述 | 主要来源 |
|--------|----------|----------|
| `list_test_suites` | 列出 `test_case` 中所有 suite | `test_case/test_controller.py` |
| `list_test_cases` | 列出某个 suite 下所有测试用例 | `test_case/test_controller.py` |
| `search_existing_cases` | 搜索已有用例，找相似实现 | `test_case/suites/` |
| `read_suite_docs` | 读取 suite README 或测试说明 | `test_case/suites/*/README.md` |
| `discover_rocm_workloads` | 扫描 `rocm-on-radeon` 可测试 workload | `rocm-on-radeon/model-scripts/` |
| `read_workload_spec` | 读取 workload 的 README、参数、依赖、结果模式 | `run.sh`、`README.md`、`constants.py` |
| `detect_workload_entrypoint` | 判断 workload 入口是 `run.sh`、`run.py`、`inference.py` 还是 `train.py` | `rocm-on-radeon` |

**Agent 调用场景**：用户说"为 vLLM 生成测试"，Agent 调用 `discover_rocm_workloads` 找到 vLLM workload，再调用 `read_workload_spec` 获取参数和依赖信息，然后决定生成什么用例。

### 3.x 外部数据采集类工具

| 工具名 | 中文描述 | 主要来源 |
|--------|----------|----------|
| `fetch_rocm_issues` | 从 `ROCm/ROCm` GitHub 仓库拉取所有 Issues，按标签/状态分类保存到本地 | `GitHub API` |

**Agent 调用场景**：用户问"ROCm 最近有什么已知问题"，Agent 调用 `fetch_rocm_issues` 拉取最新的 Issues 列表，结合 RAG 知识分析哪些 Issue 与当前测试需求相关，用于指导用例生成时的边界条件和异常路径设计。

### 3.2 用例生成和维护类工具

| 工具名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `plan_test_case` | 根据用户需求和 workload 生成测试计划 | `requirement`、`workload_spec` |
| `map_workload_to_suite` | 把 workload 映射到合适的 test_case suite | `workload_id` |
| `generate_test_case_script` | 生成 `test_*.sh` 用例脚本 | `suite`、`case_name`、`steps` |
| `generate_helper_script` | 生成 `scripts/*.py` 或 `scripts/*.sh` 辅助脚本 | `suite`、`script_name` |
| `update_test_case_script` | 修改已有 `test_*.sh` | `path`、`change_request` |
| `generate_test_plan_yaml` | 生成 CI test plan YAML 片段 | `suite`、`case`、`params` |
| `validate_case_structure` | 校验用例结构是否符合 `test_case` 约定 | `case_file` |
| `validate_shell_syntax` | 校验 shell 语法和 ShellCheck 问题 | `case_file` |
| `validate_python_syntax` | 校验辅助 Python 脚本 AST / import | `script_file` |
| `validate_dynamic_vars` | 校验动态变量是否支持默认值和 CLI 覆盖 | `case_file` |

**生成规则**（Agent 生成时必须遵守）：

- 用例文件放在 `test_case/suites/<suite>/test_<case>.sh`。
- 用例名在 CLI 中不带 `test_` 和 `.sh`。
- shell 用例应使用 `suites/lib.sh` 和 `shunit2`。
- 动态变量使用默认值模式，方便 `test_controller.py run -d KEY=VALUE` 覆盖。
- 复杂逻辑放 `suites/<suite>/scripts/`，用 `test_*.sh` 调用。
- 生成前必须搜索已有相似用例，避免重复。

### 3.3 结果分析类工具（Agent 专用）

| 工具名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `classify_failure` | 将失败归类为环境、网络、用例 bug、依赖缺失等 | `logs`、`exit_code` |
| `summarize_execution` | 汇总 pass/fail/skip、日志和关键指标 | `junit`、`logs` |

**Agent 调用场景**：AIDevOps 返回执行失败，Agent 调用 `classify_failure` 判断失败类型，如果是用例 bug 则进入自动修复循环，如果是环境问题则标记 Blocked。

### 3.4 RAG 和知识库类工具

| 工具名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `rag_search_docs` | 从知识库检索 ROCm、vLLM、测试规范 | `query`、`top_k` |
| `rag_index_repo_docs` | 索引 README、doc、现有用例 | `repo_path`、`include_globs` |
| `rag_refresh_upstream` | 定期拉取上游文档并更新索引 | `source`、`schedule` |
| `retrieve_case_examples` | 检索相似测试用例作为生成参考 | `query`、`suite` |
| `retrieve_failure_knowledge` | 检索历史失败和修复经验 | `error_signature` |

**知识来源**：

- `test_case/doc/`
- `test_case/suites/*/README.md`
- `test_case/suites/*/test_*.sh`
- `rocm-on-radeon/README.md`
- `rocm-on-radeon/**/README.md`
- ROCm 官方文档
- vLLM 文档
- Hugging Face /模型脚本文档

### 3.5 A2A / AIDevOps 对接类工具

| 工具名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `a2a_discover_capabilities` | 查询 AIDevOps Agent 支持的执行能力 | `endpoint` |
| `a2a_submit_test_task` | 向 AIDevOps 提交测试执行任务 | `case_file`、`suite`、`params` |
| `a2a_get_task_status` | 查询远端执行状态 | `task_id` |
| `a2a_stream_logs` | 流式接收远端执行日志 | `task_id` |
| `a2a_fetch_result` | 获取执行结果、日志、性能数据 | `task_id` |
| `a2a_cancel_task` | 取消远端执行任务 | `task_id` |

**与本地工具的关系**：

- P0 可以只生成本地用例，不依赖 AIDevOps。
- P1 开始对接 AIDevOps 执行。
- P2 使用 AIDevOps 返回日志进入自动修复循环。

### 3.6 Git、状态和入库类工具

| 工具名 | 中文描述 | 典型输入 |
|--------|----------|----------|
| `git_status` | 查看工作区变更 | `repo_path` |
| `git_diff` | 查看用例变更 diff | `repo_path`、`paths` |
| `scan_secrets` | 扫描 token、密钥、`.env`、`hf.txt` | `paths` |
| `write_agent_state` | 写 `.agent_state/test.json` | `state` |
| `make_merge_verdict` | 判断用例是否可入库 | `validation`、`execution` |
| `collect_artifacts` | 收集 XML、log、metrics、生成文件 | `paths` |
| `upload_artifacts` | 上传测试产物 | `build_branch`、`build_id` |

**必须扫描的敏感信息**：

- `HF_TOKEN`
- `HUGGINGFACE_TOKEN`
- `AMD_LLM_SUBSCRIPTION_KEY`
- `Ocp-Apim-Subscription-Key`
- `.env`
- `hf.txt`
- `credentials`
- `token=`
- 私钥和证书

---

## 4. 推荐 Function Schema 草案

### 4.1 `make_merge_verdict`

中文描述：基于静态校验、执行结果、secret 扫描和 diff 判断是否可入库。

输入字段：

- `validation_results`
- `execution_results`
- `secret_scan`
- `diff_summary`

输出字段：

- `can_merge`
- `reason`
- `blocked_cases`
- `required_fixes`

> 其余工具的 Function Schema 见 [`test_utility测试工具库设计.md`](./test_utility测试工具库设计.md)

---

## 5. 工具和项目来源映射

### 5.1 来自 `test_case` 的 Agent 工具能力

| 来源 | 可抽象 Agent 工具 |
|------|-------------------|
| `test_controller.py list` | `list_test_suites`、`list_test_cases` |
| `pipeline_prepare.py` | `prepare_pipeline` |
| `suites/lib.sh` | `generate_test_case_script` 规范来源 |
| `suites/shunit2` | `validate_case_structure` |
| `doc/`、`suites/*/README.md` | RAG 知识源 |

### 5.2 来自 `rocm-on-radeon` 的 Agent 工具能力

| 来源 | 可抽象 Agent 工具 |
|------|-------------------|
| 根 `README.md` 的 `F_A_M_E(_O)` 命名 | `discover_rocm_workloads`、`map_workload_to_suite` |
| `model-scripts/**/run.sh` | `read_workload_spec` |
| 内部文档 | RAG 知识源 |

---

## 6. MVP 工具优先级

### P0：先做，能形成闭环

- `list_test_suites`
- `list_test_cases`
- `search_existing_cases`
- `discover_rocm_workloads`
- `read_workload_spec`
- `plan_test_case`
- `generate_test_case_script`
- `validate_case_structure`
- `validate_shell_syntax`
- `scan_secrets`
- `make_merge_verdict`
- `write_agent_state`

### P1：提升质量和自动修复能力

- `map_workload_to_suite`
- `classify_failure`
- `generate_test_plan_yaml`
- `update_test_case_script`
- `retrieve_case_examples`
- `retrieve_failure_knowledge`

### P2：接入外部执行和高级能力

- `a2a_submit_test_task`
- `a2a_fetch_result`
- `rag_search_docs`
- `rag_index_repo_docs`

---

## 7. 推荐执行闭环

### 7.1 仅生成用例

1. `discover_rocm_workloads`
2. `read_workload_spec`
3. `search_existing_cases`
4. `plan_test_case`
5. `generate_test_case_script`
6. `validate_case_structure`
7. `validate_shell_syntax`
8. `scan_secrets`

### 7.2 生成并本地执行

1. 执行"仅生成用例"流程。
2. 测试脚本执行（调用 Test Utility `run_test_case`）
3. 测试脚本执行（调用 Test Utility `parse_junit_result`）
4. `classify_failure`
5. `make_merge_verdict`
6. `write_agent_state`

### 7.3 生成并委托 AIDevOps 执行

1. 执行"仅生成用例"流程。
2. `a2a_discover_capabilities`
3. `a2a_submit_test_task`
4. `a2a_stream_logs`
5. `a2a_fetch_result`
6. `classify_failure`
7. `make_merge_verdict`
8. `write_agent_state`

### 7.4 失败自动修复

1. `classify_failure`
2. `retrieve_failure_knowledge`
3. `update_test_case_script`
4. `validate_case_structure`
5. `validate_shell_syntax`
6. 重新执行，最多 3 轮。

---

## 8. 设计结论

这个智能体的 Tool Use 层应该以 **Agent 的决策生命周期**为主线：

- **生成前**：发现 suite/case/workload，检索 RAG 知识，读取 workload 规格
- **生成时**：规划用例、生成脚本、校验结构和语法
- **生成后**：委托 AIDevOps 执行、分析失败原因、自动修复、判断入库

与测试脚本运行时的工具函数彻底解耦——那些归入 `test_utility`，由测试脚本 `import` 使用。

Agent Tool 的核心特征是：**由 LLM 驱动调用，消费返回值做推理决策**。

---

## 9. 系统环境层（System Environment Layer）

系统中存在一类工具，既不是 Agent 的 Function Calling，也不是测试脚本的 Utility——它们属于**系统环境层**，透明地存在于执行环境的底层，Agent 和测试脚本都不需要显式调用它们。

### 9.1 典型工具

| 工具 | 定位 | 说明 |
|------|------|------|
| **RTK (Rust Token Killer)** | Shell 命令输出压缩代理 | 透明拦截 `git`/`ls`/`grep`/`pytest` 等命令输出，压缩 token 消耗 60-90% |
| `rocminfo` / `rocm-smi` | ROCm 系统诊断工具 | 系统级 GPU 信息查询，test_utility 底层调用 |
| Shell hook（`.bashrc` / pre-exec） | 命令预处理 | 环境变量、别名、PATH 设置 |
| Docker 守护进程 | 容器运行时 | 系统级容器管理 |

### 9.2 RTK 的工作原理

RTK 通过 hook 机制注入到 Agent 的 shell 执行链路中：

```
无 RTK:
  Agent ──git status──→ Shell ──→ git
    ↑                              │
    └────── ~2000 tokens (原始输出) ─┘

有 RTK:
  Agent ──git status──→ RTK hook ──→ git
    ↑                    │
    └── ~200 tokens (压缩后) ┘
```

### 9.3 在 deepagents 中的集成方式

RTK 的集成不在代码层，而在**环境准备层**：

```bash
# 在 Sandbox / Docker 镜像 / 物理机 预装
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh
rtk init -g  # 安装 hook
```

安装后，Sandbox 中执行的所有 shell 命令输出都会自动被 RTK 压缩，**Agent 代码无需任何修改**。

### 9.4 三层工具体系总结

| 层 | 调用者 | 典型工具 | 示例 |
|----|--------|----------|------|
| **Agent Tool Use** | LLM 推理循环 | 发现、生成、校验、A2A、RAG、入库判断 | `discover_workloads`, `generate_script`, `classify_failure` |
| **Test Utility** | pytest / shell 脚本 | 环境查询、下载、运行、解析 | `query_gpu_info`, `download_hf_model`, `parse_junit` |
| **System Environment** | 操作系统 / Shell | 命令压缩、GPU 诊断、容器运行时 | RTK, `rocminfo`, Docker daemon |

三层之间**互不感知**：Test Utility 不需要知道 RTK 的存在，Agent 也不需要关心执行环境的底层优化。
