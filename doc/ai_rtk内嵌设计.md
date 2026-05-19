# AI-RTK 内嵌设计

## 1. 背景

### 1.1 什么是 RTK

**RTK (Rust Token Killer)** 是一个开源的系统级 CLI 代理，由 [rtk-ai/rtk](https://github.com/rtk-ai/rtk) 社区维护。它的核心功能是：

- **透明拦截** shell 命令（如 `git status` → 自动重写为 `rtk git status`）
- **智能压缩**命令输出，减少 60-90% 的 token 消耗
- **无侵入集成**通过 hook 机制注入 AI 编码助手的执行生命周期

| 操作 | 原始输出 | RTK 压缩后 | 节省 |
|------|----------|-----------|------|
| `ls` / `tree` | 2,000 tokens | 400 tokens | -80% |
| `git status` | 3,000 tokens | 600 tokens | -80% |
| `git diff` | 10,000 tokens | 2,500 tokens | -75% |
| `pytest` | 8,000 tokens | 800 tokens | -90% |
| `cargo test` | 25,000 tokens | 2,500 tokens | -90% |
| **合计（30 分钟会话）** | **~118,000 tokens** | **~23,900 tokens** | **-80%** |

### 1.2 问题

在 `Test Case Agent` 项目中，我们定义了三个工具层级：

1. **Agent Tool Use**（Function Calling）—— LLM 推理循环显式调用的决策工具
2. **Test Utility**（测试工具库）—— pytest / shell 测试脚本 `import` 的共享库
3. **System Environment**（系统环境层）—— 操作系统 / Shell 级别的透明工具

RTK 不属于前两层，它应该被归入第三层——**系统环境层**。本文档详细说明它的定位、工作原理和集成方案。

---

## 2. 三层工具体系

### 2.1 架构总览

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Test Case Agent (LangGraph)                     │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  Agent Tool Use（Function Calling）                           │   │
│  │  ├─ 发现类：list_test_suites, discover_workloads              │   │
│  │  ├─ 生成类：generate_test_case_script, validate_*            │   │
│  │  ├─ RAG 类：rag_search_docs, retrieve_case_examples          │   │
│  │  ├─ A2A 类：a2a_submit_test_task, a2a_fetch_result           │   │
│  │  └─ 入库类：scan_secrets, make_merge_verdict                  │   │
│  │  调用者：LLM 推理循环 · 消费方：Agent Memory/State             │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              │ 生成代码                              │
│                              ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  Test Utility（测试工具库）                                    │   │
│  │  ├─ 环境查询：query_gpu_info, query_rocm_version             │   │
│  │  ├─ 资产下载：download_hf_model, download_artifactory_asset  │   │
│  │  ├─ 依赖安装：install_pip_requirements, install_system_pkg   │   │
│  │  ├─ Docker：docker_run_test_case, docker_pull_image          │   │
│  │  ├─ Workload：run_vllm_benchmark, run_model_inference        │   │
│  │  └─ 解析：parse_junit_result, extract_inference_metrics      │   │
│  │  调用者：pytest / shell 脚本 · 方式：import / source           │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                              │ 执行环境
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  System Environment（系统环境层）←── RTK 在此层                      │
│  ├─ RTK (Rust Token Killer)：透明压缩 shell 命令输出                │
│  ├─ ROCm 系统工具：rocminfo, rocm-smi, hipcc                       │
│  ├─ 容器运行时：Docker daemon, containerd                           │
│  └─ Shell 基础设施：.bashrc, PATH, 环境变量                         │
│  透明存在 · 不需要显式调用 · Agent 和测试脚本都不感知                │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 三层对比

| 维度 | Agent Tool Use | Test Utility | System Environment |
|------|----------------|--------------|-------------------|
| **调用者** | LLM Agent 推理循环 | pytest / shell 测试脚本 | 操作系统 / Shell |
| **调用方式** | Function Calling API | `import rocm_test_utils` | 透明 hook / 系统 PATH |
| **触发时机** | Agent 决策时主动调用 | 测试执行期间 | 每次 shell 命令执行 |
| **返回值消费方** | Agent 的 Memory/State | 测试断言 `assert` | 被压缩后传递给调用者 |
| **是否感知 RTK** | 不感知 | 不感知 | RTK 自身在此层运行 |
| **典型工具** | `discover_workloads`, `generate_script`, `classify_failure` | `query_gpu_info`, `download_hf_model`, `parse_junit` | RTK, `rocminfo`, Docker daemon |

---

## 3. RTK 的工作原理

### 3.1 执行链路对比

```
无 RTK：

  Agent/Script ──"git status"──→ Shell ──→ git
      ↑                                    │
      └────── ~3000 tokens（原始输出）───────┘


有 RTK（通过 PreToolUse Hook 自动重写）：

  Agent/Script ──"git status"──→ RTK Hook ──→ Shell ──→ git
      ↑                            │                       │
      │                            └── 重写为 "rtk git status"
      │                                                    │
      └──────── ~600 tokens（压缩后）────────────────────────┘
```

### 3.2 四种压缩策略

RTK 对不同类型的命令输出采用四种策略：

| 策略 | 说明 | 示例 |
|------|------|------|
| **Smart Filtering** | 移除噪音（注释、空白行、模板代码） | `ls -la` 的权限列、`.` 和 `..` |
| **Grouping** | 聚合相似项（文件按目录分组、错误按类型汇总） | 测试失败只显示 FAILED 汇总 |
| **Truncation** | 保留相关上下文，裁剪冗余 | 长 diff 只保留变更摘要 |
| **Deduplication** | 重复行合并为计数 | 重复日志 → `[×42] same message` |

### 3.3 典型压缩效果

```bash
# git push 原始输出（15 行，~200 tokens）
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.2 KiB | 1.20 MiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/user/repo.git
   abc1234..def5678  main -> main

# rtk git push（1 行，~10 tokens）
ok main
```

```bash
# cargo test 失败输出（200+ 行，~25000 tokens）
running 15 tests
test utils::test_parse ... ok
test utils::test_format ... ok
test utils::test_validate ... ok
test core::test_init ... ok
...

# rtk test cargo test（~20 行，~2500 tokens）
FAILED: 2/15 tests
  test_edge_case: assertion failed at src/lib.rs:42
  test_overflow: panic at src/lib.rs:87
```

---

## 4. RTK 在 deepagents 框架中的集成

### 4.1 集成位置

deepagents 框架中，agent 的 shell 命令通过 **Sandbox** 执行。RTK 应该安装在 **Sandbox 内部**，作为系统环境的一部分。

```
deepagents 架构中的集成点：

  Agent (LangGraph)
       │
       │  Tool Call: Bash(command="git status")
       ▼
  Sandbox (Docker / Daytona / Runloop / 本地)
       │
       │  Sandbox 内部：
       │  ├── ~/.claude/hooks/rtk-rewrite.sh   ← RTK Hook
       │  ├── ~/.local/bin/rtk                 ← RTK 二进制
       │  └── ~/.claude/CLAUDE.md (引用 RTK.md)  ← 指令注入
       │
       ▼
  Shell 实际执行: rtk git status  ← 透明重写
       │
       ▼
  压缩后的输出返回 Agent
```

### 4.2 两种集成方式

#### 方式一：Sandbox 预装（推荐）

在 Sandbox 镜像构建或启动时预装 RTK，使其对 Sandbox 内所有 Agent 会话生效。

```dockerfile
# Dockerfile 示例
FROM rocm/dev-ubuntu:22.04

# 安装 RTK
RUN curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh \
    && rtk init -g \
    && rtk --version
```

```python
# Python Sandbox 启动时安装
sandbox = Sandbox(image="rocm/dev-ubuntu:22.04")
sandbox.exec("curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh")
sandbox.exec("rtk init -g")
# 后续所有 shell 命令输出自动被 RTK 压缩
result = sandbox.exec("git status")  # 实际执行: rtk git status
```

#### 方式二：宿主机级安装（开发者本地使用）

在运行 deepagents CLI 的宿主机上安装 RTK，优化开发者与 Agent 交互时的 token 消耗。

```bash
# 宿主机安装
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh
rtk init -g
```

### 4.3 集成清单

| 步骤 | 命令 | 说明 |
|------|------|------|
| 1. 安装二进制 | `curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh \| sh` | 安装到 `~/.local/bin` |
| 2. 初始化 hook | `rtk init -g` | 安装 PreToolUse hook + RTK.md |
| 3. 验证安装 | `rtk --version && rtk gain` | 确认版本和 token 节省统计 |
| 4. 选择性配置 | `rtk init -g --agent cursor` | 针对特定 AI 工具（可选） |

### 4.4 在 ROCm 环境中的特殊考量

| 场景 | 影响 | 建议 |
|------|------|------|
| `rocm-smi` 输出 | 显示 GPU 状态、温度、功耗 | RTK 可能截断关键指标——配置白名单不过滤 |
| `rocminfo` 输出 | GPU 架构信息，用于测试前置判断 | 保留原始输出，不经过 RTK |
| `pip install` 大量输出 | 安装 ROCm wheel 时日志很长 | RTK 自动压缩，有益 |
| `docker build` | 构建日志量大 | RTK 自动压缩，有益 |
| `pytest` 输出 | 测试结果 | RTK 压缩为失败汇总，有益 |

**配置示例**（`~/.config/rtk/config.toml`）：

```toml
# 对某些命令禁用 RTK 压缩
[hooks]
exclude_commands = ["rocm-smi", "rocminfo"]

# 保留原始输出用于故障排查
[tee]
enabled = true
mode = "failures"  # 失败时保留原始输出到文件
```

---

## 5. 和现有架构的关系

### 5.1 RTK 不是 Agent Tool Use

| Tool Use 的要求 | RTK 的表现 |
|----------------|------------|
| Agent 显式调用 | ❌ RTK 透明拦截，Agent 不知道它的存在 |
| 消费返回值做推理 | ❌ RTK 只是格式转换，不做推理 |
| 属于 LLM 决策循环 | ❌ 不参与决策 |
| 可以通过代码控制开关 | ✅ 但 Agent 不需要控制 |

### 5.2 RTK 不是 Test Utility

| Test Utility 的要求 | RTK 的表现 |
|--------------------|------------|
| 测试脚本 import 使用 | ❌ 测试脚本不需要 import |
| 在测试执行期间运行 | ❌ 在 shell 执行层运行，测试不感知 |
| 返回值用于 assert | ❌ 返回值被压缩后还给调用者 |
| 可以被 Agent 生成到代码中 | ❌ Agent 生成测试脚本时不需要考虑 RTK |

### 5.3 RTK 是 System Environment

| System Environment 的特征 | RTK 的表现 |
|--------------------------|------------|
| 透明存在于执行环境底层 | ✅ Hook 自动拦截所有 shell 命令 |
| 不需要显式调用 | ✅ 安装后自动生效 |
| Agent 和测试脚本都不感知 | ✅ 两者代码都不需要修改 |
| 在 Sandbox / 容器层面配置 | ✅ 镜像构建时一次安装，全局生效 |

---

## 6. 总结

| 维度 | 结论 |
|------|------|
| **定位** | 系统环境层（System Environment Layer） |
| **安装方式** | Sandbox 镜像预装或宿主机级安装，非代码级集成 |
| **对 Agent** | 完全透明——Agent 代码无需任何修改 |
| **对 Test Utility** | 完全透明——测试脚本无需任何修改 |
| **收益** | Shell 命令输出 token 减少 60-90%，降低运行成本 |
| **风险** | 对 `rocm-smi`、`rocminfo` 等诊断命令需配置白名单 |
| **推荐度** | P2 阶段引入（先确保核心功能闭环，再用 RTK 优化成本） |

---

**参考链接**：

- <https://github.com/rtk-ai/rtk>
- <https://www.rtk-ai.app>
- [Tool_use层设计.md](./Tool_use层设计.md) 第 9 章「系统环境层」
- [test_utility测试工具库设计.md](./test_utility测试工具库设计.md)「三层体系总览」
