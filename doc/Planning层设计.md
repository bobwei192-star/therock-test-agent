# Planning 层设计

## 1. 目标

Test Case Agent 不应该只负责"写几行断言"。它的核心价值是把一个模糊的测试目标，规划成可执行、可评审、可追溯、可维护的工业级测试用例。

Planning 层负责：

- 理解用户需求：搞清楚测什么、为什么测、验收标准是什么。
- 识别测试对象：ROCm 组件、GPU 环境、图形能力、AI model workload、Docker workload、AIDevOps 远端任务等。
- 拆解测试点：正常路径、边界条件、异常路径、依赖条件、风险点。
- 选择测试类型：功能、集成、系统、回归、性能、稳定性、兼容性。
- 形成测试步骤：前置条件、环境准备、执行动作、观测点、断言、清理动作。
- 输出工程交付物：测试需求矩阵、用例计划、用例脚本草案、执行计划、归档信息。

最终目标是让任何工程师看到 Planning 输出后，都能判断：

- 这个用例是否值得写。
- 这个用例覆盖了哪个需求。
- 这个用例是否可重复执行。
- 这个用例是否有明确可观测的通过/失败标准。
- 这个用例是否能进入 test_case 用例库。

## 2. 规划层在智能体中的位置

原始需求中定义了核心流程：

```
用户需求 -> 规划器 -> 生成器 -> 验证器 -> 执行用例 -> 失败修复 -> 完成
```

其中 Planning 层对应"规划器"，它位于代码生成之前。

Planning 层不能直接跳到写代码。它必须先输出结构化计划，然后交给 Generator 生成 test_\*.sh、辅助 Python 脚本或测试计划 YAML。

推荐节点拆分：

| 节点 | 职责 | 输入 | 输出 |
|------|------|------|------|
| requirement_analyzer | 需求分析 | 用户自然语言、PRD、README、已有 case | 测试目标、范围、约束 |
| context_retriever | 检索上下文 | test_case、rocm-on-radeon、RAG | 参考用例、workload 规格、规范 |
| risk_classifier | 风险分类 | 需求和上下文 | 风险等级、人工确认点 |
| test_point_designer | 测试点设计 | 需求和风险 | 正常/异常/边界/性能测试点 |
| case_planner | 用例步骤规划 | 测试点 | 用例 ID、步骤、断言、清理 |
| execution_planner | 执行计划 | 用例计划 | 本地执行/AIDevOps/Docker/skip 条件 |
| review_gate | 评审门禁 | 完整计划 | 是否允许进入生成阶段 |

## 3. 基于当前仓库的落地约束

### 3.1 test_case 的真实用例格式

原始需求中写的是"pytest 格式"。但当前 /home/zx/CICD/test_case 的主流执行框架是：



### 3.2 rocm-on-radeon 的真实 workload 形态

rocm-on-radeon 不是统一框架，而是一组自包含 workload：

- model-scripts/\*
- semi-automated-scripts/\*
- in-development/\*
- component_units/\*
- performance_benchmarks/\*

它的规划价值在于：

- 提供模型脚本入口：run.sh、run.py、inference.py、train.py
- 提供参数规范：--model-name、--precision、--devices、--batch-size
- 提供依赖来源：requirements.txt、Dockerfile、Hugging Face、Artifactory
- 提供结果模式：BEGIN RESULTS / END RESULTS、throughput、latency、inference time
- 提供命名规则：F_A_M_E(\_O)



## 4. Planning 输入

Planning 层的输入可以来自多个来源。

### 4.1 用户自然语言

示例：

- "为 vLLM 上运行的 Llama-3.1-8B 生成推理性能测试"
- "生成一个 PRIME offload 的 OpenGL 测试"
- "给 ROCm rocBLAS 增加一个 smoke test"
- "维护失败的 text_generation/test_vllm.sh，根据日志修复"

### 4.2 项目上下文

来自 test_case：



### 4.3 环境上下文

Planning 阶段应收集但不一定执行：

- OS / WSL / bare metal
- GPU 拓扑：APU、dGPU、多 GPU、Navi、MI300 等
- ROCm 是否安装
- rocminfo、rocm-smi、lspci 是否可用
- Docker 是否可用
- 网络是否能访问 Hugging Face / GitHub / Artifactory
- 磁盘是否足够
- 是否有 HF token 或内部 token

### 4.4 历史执行上下文

用于自动修复和质量评估：

- 上次执行日志
- JUnit XML
- AIDevOps 返回结果
- 失败栈
- 失败机器信息
- 已知问题归档

## 5. Planning 输出

Planning 层输出的是结构化用例计划，而不是最终代码。

建议输出字段：

| 字段 | 说明 |
|------|------|
| case_id | 用例 ID，如 TC-APU-DGPU-PRIME-OGL-001 |
| case_title | 一句话说明测什么 |
| suite | 目标 suite |
| case_name | test\_\<case_name\>.sh 中的 \<case_name\> |
| requirement_refs | 需求来源、README、用户需求 |
| test_object | 被测对象，如 PRIME offload、vLLM、ROCm SMI |
| test_type | 功能、集成、系统、性能、回归、兼容性 |
| priority | P0/P1/P2/P3 |
| preconditions | 前置条件 |
| test_data | 测试数据、模型、参数、设备 |
| steps | 可执行步骤 |
| expected_results | 每步可验证预期 |
| observability | 需要采集的日志、命令输出、metrics |
| cleanup | 清理动作 |
| skip_conditions | 不满足条件时跳过原因 |
| risk_level | safe/network/heavy/system |
| human_confirm_required | 是否需要人工确认 |
| review_checklist | 评审检查项 |
| execution_plan | 本地执行或 AIDevOps 执行 |
| archive_plan | 结果归档路径和指标 |

## 6. 工业级测试用例规划流程

### 6.1 阶段一：需求分析

目标：搞清楚"测什么"。

Planner 要回答：

- 这个功能要解决什么问题？
- 正常流程是什么？
- 输入是什么？
- 输出是什么？
- 依赖哪些硬件、驱动、软件、模型或服务？
- 有哪些边界条件？
- 有哪些异常场景？
- 成功标准是否可观测？
- 失败时能否定位问题？

交付物：测试需求矩阵 RTM。

RTM 建议字段：

| 字段 | 说明 |
|------|------|
| requirement_id | 需求 ID |
| requirement_desc | 需求描述 |
| test_point | 测试点 |
| case_id | 对应用例 |
| coverage_type | 正常/边界/异常/性能/兼容 |
| priority | P0/P1/P2/P3 |
| evidence | 来源文档或已有用例 |

### 6.2 阶段二：上下文检索

目标：避免凭空生成，必须基于资产。

Planner 要检索：

- 同 suite 下已有类似用例。
- lib.sh 中可复用函数。
- suite README。
- rocm-on-radeon 中相似 workload。
- 历史失败记录。
- 官方文档或 RAG 知识。

输出：

- 可复用代码模式。
- 可复用命令模式。
- 可复用断言模式。
- 不能复用或需要人工确认的点。

### 6.3 阶段三：测试点设计

目标：确定"怎么测"。

Planner 应使用以下方法拆解测试点：

| 方法 | 在 ROCm / AI Model 测试中的应用 |
|------|--------------------------------|
| 等价类划分 | 不同模型、不同 precision、不同 backend |
| 边界值分析 | GPU 数量 0/1/N、batch size 1/最大值、prompt 数 1/大量 |
| 状态转换 | 服务启动、模型加载、推理、停止、重启 |
| 场景法 | 环境准备 -> workload 执行 -> 结果解析 -> 清理 |
| 错误推测 | 缺模型、缺 token、GPU 不可见、Docker 不可用、X 未启动 |
| 正交实验 | 框架 x backend x model x precision x devices 组合 |
| 回归分析 | 改动后验证原有核心 smoke case 不失败 |

### 6.4 阶段四：测试类型选择

一个需求可能映射多个测试类型。

| 类型 | 适用场景 | 示例 |
|------|----------|------|
| 功能测试 | 验证功能是否可用 | PRIME offload 后 GL_RENDERER 指向 dGPU |
| 集成测试 | 多模块协同 | X server + DRI_PRIME + OpenGL app |
| 系统测试 | 端到端场景 | 安装依赖 -> 启动 X -> 跑 benchmark -> 验证日志 |
| 回归测试 | 防止旧能力坏掉 | ROCm 升级后重复运行关键用例 |
| 性能测试 | 验证吞吐/延迟 | vLLM throughput / latency |
| 稳定性测试 | 长时间运行 | overnight benchmark、stress test |
| 兼容性测试 | 不同 GPU/OS/ROCm | APU+dGPU、WSL、Navi、MI300 |
| 安全/合规 | 密钥、token、权限 | 确保 token 不入库 |

### 6.5 阶段五：用例步骤规划

工业级步骤必须满足：

- **可重复**：任何人按步骤执行结果一致。
- **可验证**：每一步有明确观测点。
- **可独立**：不依赖其他用例先执行。
- **可清理**：执行后恢复环境。
- **可追溯**：能对应需求、代码、日志和 bug。

标准步骤结构：

| 步骤类型 | 说明 |
|----------|------|
| 前置检查 | 检查环境、硬件、依赖、网络、磁盘 |
| 环境准备 | 安装包、启动服务、下载资产、设置变量 |
| 执行动作 | 调用 workload 或命令 |
| 结果采集 | 保存日志、XML、metrics、命令输出 |
| 断言验证 | 判断 pass/fail/blocked/skip |
| 清理动作 | 停止服务、删除临时文件、恢复状态 |

### 6.6 阶段六：评审门禁

Planning 输出进入生成阶段前必须检查：

- 用例目标是否单一。
- 预期结果是否量化或可观测。
- 前置条件是否完整。
- 是否有 skip 条件。
- 是否有清理动作。
- 是否会安装系统包、下载大文件、运行 Docker。
- 是否可能修改系统状态。
- 是否有 secret 风险。
- 是否已有重复用例。


不满足门禁时，Planner 应返回"需要补充信息"或"需要人工确认"，而不是继续生成。

## 7. Case 示例：test_prime_offload_ogl.sh

### 7.1 用例定位

路径：

```
/home/zx/CICD/test_case/suites/apu_dgpu/test_prime_offload_ogl.sh
```

当前用例目标：

验证 APU + dGPU 场景下，OpenGL 应用可以通过 PRIME offload 方式在 dGPU 上渲染，并且 GL_RENDERER 能显示 dGPU/Navi 相关信息。

这个用例不是简单的命令测试，它覆盖了：

- 多 GPU 拓扑识别。
- X server 启动。
- OpenGL benchmark 执行。
- PRIME offload 环境变量。
- 渲染设备结果验证。
- 图形栈和驱动集成。

### 7.2 RTM 示例

| requirement_id | 需求描述 | 测试点 | 对应用例 | 覆盖类型 | 优先级 |
|----------------|----------|--------|----------|----------|--------|
| REQ-APU-DGPU-001 | APU+dGPU 平台可识别 dGPU | 解析 lspci 找到 AMD GPU | test_prime_offload_ogl | 前置/功能 | P0 |
| REQ-APU-DGPU-002 | OpenGL 应用可启动 | 安装并运行 glmark2 | test_prime_offload_ogl | 集成 | P0 |
| REQ-APU-DGPU-003 | PRIME offload 可将渲染转移到 dGPU | 使用 DRI_PRIME 运行 glmark2 | test_prime_offload_ogl | 系统 | P0 |
| REQ-APU-DGPU-004 | 渲染结果可验证 | 日志中 GL_RENDERER 包含 Navi | test_prime_offload_ogl | 断言 | P0 |
| REQ-APU-DGPU-005 | 执行后环境恢复 | 停止 X server | test_prime_offload_ogl | 清理 | P1 |

### 7.3 测试点拆解

#### 正常路径

1. 机器存在 APU + dGPU。
2. lspci 能识别 AMD VGA/Display controller。
3. glmark2 安装成功。
4. X server 启动成功。
5. 使用 DRI_PRIME 执行 glmark2。
6. 日志中出现 GL_RENDERER。
7. GL_RENDERER 包含 Navi。
8. 停止 X server。

#### 异常路径

1. 没有 dGPU。
2. lspci 没有 AMD 设备。
3. glmark2 安装失败。
4. X server 启动失败。
5. DRI_PRIME 设置不正确。
6. glmark2 执行失败。
7. 日志中没有 GL_RENDERER。
8. GL_RENDERER 指向 iGPU 或 llvmpipe。
9. 清理阶段 stop_x 失败。

#### 边界条件

- 只有一张 AMD GPU。
- 多张 dGPU，设备 ID 选择逻辑是否稳定。
- 非 Navi GPU，断言不能只写死 Navi。
- Wayland 环境和 X11 环境差异。
- WSL 或无显示环境。

### 7.4 当前用例的工业化评价

#### 优点

- 使用 set -o pipefail。
- 引入 lib.sh。
- 有 setUp、run、tearDown、shunit2 结构。
- 使用 install_pkg 和 start_x 复用公共能力。
- 执行后调用 stop_x 清理环境。
- 有明确日志 /tmp/glmark.log。
- 有明确断言：GL_RENDERER 必须出现且包含 Navi。

#### 需要 Planner 在生成新用例时改进的点

- 前置条件需要更明确：必须是 APU+dGPU，且目标 dGPU 应支持 OpenGL。
- dGPU 选择逻辑不应只依赖最大 device ID；应规划更可靠的设备选择策略。
- DRI_PRIME 通常使用 provider index 或设备选择，不一定等于 1002:\<device_id\>；需要规划验证方式。
- 预期结果不应只绑定 navi，应允许通过平台 metadata 配置期望 renderer。
- 日志路径 /tmp/glmark.log 可能被并发用例覆盖，建议规划为 suite logs 下唯一文件。
- run_glmark2 注释说 5 分钟，但命令没有限制运行时间；需要规划 timeout。
- 缺少 skip 逻辑：无 dGPU、无 X、无 glmark2 源、非图形环境应 Blocked/Skipped。
- 缺少性能指标采集：如果是 benchmark，应提取 score；如果只是功能，应明确不关注 score。
- 清理动作应保证失败也执行。

### 7.5 该 case 的规划输出示例

| 字段 | 内容 |
|------|------|
| case_id | TC-APU-DGPU-PRIME-OGL-001 |
| case_title | 验证 APU+dGPU 平台 OpenGL PRIME offload 渲染到 dGPU |
| suite | apu_dgpu |
| case_name | prime_offload_ogl |
| test_type | 系统测试 / 集成测试 / 回归测试 |
| priority | P0 |
| preconditions | APU+dGPU 平台；可启动 X；可安装或已安装 glmark2 |
| test_data | DRI_PRIME 目标设备；期望 renderer 关键字 |
| main_steps | 识别 GPU -> 启动 X -> 运行 glmark2 -> 解析 GL_RENDERER -> 清理 |
| expected_result | glmark2 返回成功，日志中 renderer 指向目标 dGPU |
| skip_conditions | 无 dGPU、无 display controller、X 不可用、glmark2 不可安装 |
| logs | suite logs 下 glmark2 日志 |
| cleanup | stop_x、清理临时日志 |

### 7.6 该 case 规划出的标准步骤

#### 环境识别

1. 查询 lspci。
2. 识别 AMD VGA/Display controller。
3. 判断是否存在至少两个 GPU 或满足 APU+dGPU 条件。

#### 前置依赖

1. 检查 glmark2 是否存在。
2. 不存在时通过 install_pkg glmark2 安装。
3. 检查 X server 能否启动。

#### 执行准备

1. 选择目标 dGPU。
2. 设置 DRI_PRIME。
3. 设置唯一日志路径。
4. 设置超时时间。

#### 执行

1. 运行 glmark2。
2. 保存 stdout/stderr。
3. 记录 exit code。

#### 断言

1. exit code 为 0。
2. 日志包含 GL_RENDERER。
3. renderer 符合目标 dGPU 预期。
4. 如果采集 score，则 score 是数字且大于 0。

#### 清理

1. 停止 X server。
2. 释放后台进程。
3. 保留日志用于归档。

## 8. AI Model 用例规划模板



### 8.1 需求分析

必须明确：

- 测试框架：PyTorch、ONNXRuntime、JAX、TensorFlow、vLLM、llama.cpp。
- 后端：ROCm、MIGraphX、CUDA、CPU。
- 模型：Llama、Qwen、ResNet、Whisper、Stable Diffusion 等。
- 执行类型：inference 或 training。
- 精度：fp32、fp16、int8、int4、fp8。
- 设备：单 GPU 或多 GPU。
- 目标：功能正确、性能指标、稳定性、兼容性。

### 8.2 Workload 映射



- vllm_rocm_llm_inf -> LLM 推理 -> text_generation
- cpp_rocm_llm_inf -> llama.cpp 推理 -> wsl_cpp_rocm 或 text_generation
- pyt_rocm_resnet50_inf -> PyTorch ROCm 图像推理 -> wsl_pytorch_rocm
- ort_migx_llm_inf -> ONNXRuntime + MIGraphX -> text_generation
- pyt_rocm_whisper_inf -> 语音推理 -> 对应 audio suite 或新建 suite

### 8.3 AI Model 用例步骤

1. 读取 workload README 和参数。
2. 确认模型来源：HF、Artifactory、本地缓存。
3. 确认依赖：requirements、Docker、系统包。
4. 确认硬件：GPU 数量、显存、ROCm 版本。
5. 确认测试 profile：smoke、standard、heavy、overnight。
6. 准备模型和数据。
7. 运行 workload。
8. 提取结果块。
9. 断言功能结果和性能指标。
10. 保存日志和 metrics。
11. 清理临时资源。

### 8.4 AI Model skip / blocked 条件

- HF token 缺失。
- Artifactory 不可访问。
- 模型缓存不存在且不允许下载。
- GPU 数量不足。
- 显存不足。
- ROCm 版本不匹配。
- Docker 不可用。
- 依赖安装需要人工确认。
- workload README 标记不支持当前平台。

## 9. Planning 质量门禁

Planner 生成的计划必须通过以下门禁。

### 9.1 需求门禁

- 是否有明确测试目标。
- 是否能追溯到需求或用户输入。
- 是否明确不测什么。
- 是否能映射到已有 suite 或说明需要新 suite。

### 9.2 工程门禁

- 是否符合 test_case 用例结构。

- 是否有动态变量设计。
- 是否有日志路径设计。
- 是否有清理动作。
- 是否避免污染系统环境。

### 9.3 执行门禁

- 是否列出前置条件。
- 是否有 skip 条件。
- 是否标记需要人工确认的高风险动作。
- 是否有 timeout。
- 是否能采集足够日志。

### 9.4 断言门禁

- 预期结果是否可观测。
- 断言是否量化。
- 是否避免"系统正常"这种不可验证描述。
- 是否能区分 Fail 和 Blocked。

### 9.5 入库门禁

- 是否扫描 secret。
- 是否避免硬编码 token、本地绝对路径、大模型文件。
- 是否有评审记录。
- 是否有执行结果。
- 是否能生成 merge_verdict。

## 10. Planner 与 Function Calling 工具的关系

Planning 层不直接执行高风险动作，而是决定是否需要调用工具。

| Planning 需求 | 对应工具 |
|---------------|----------|
| 找已有 suite/case | list_test_suites、list_test_cases、search_existing_cases |
| 理解 workload | discover_rocm_workloads、read_workload_spec |
| 查询机器环境 | query_rocm_version、query_gpu_info、check_docker_available |
| 估算执行风险 | check_disk_space、check_network_access、estimate_case_cost |
| 下载模型 | download_hf_model、download_artifactory_asset |
| 准备代码仓库 | clone_repo |
| 安装依赖 | install_pip_requirements、install_system_packages |
| 生成用例 | generate_test_case_script、generate_helper_script |
| 执行用例 | run_test_case、a2a_submit_test_task |
| 解析结果 | parse_junit_result、parse_case_log、extract_result_block |
| 失败修复 | classify_failure、retrieve_failure_knowledge、update_test_case_script |
| 入库判断 | scan_secrets、git_diff、make_merge_verdict |

Planner 输出中必须标明：

- 哪些工具要调用。
- 调用顺序是什么。
- 哪些工具只 dry-run。
- 哪些工具需要人工确认。
- 工具失败时如何降级。

## 11. 自动修复规划

当执行失败时，Planner 不应盲目修改代码，而应先分类。

失败分类：

| 类型 | 例子 | 处理策略 |
|------|------|----------|
| 环境问题 | 没有 GPU、X 启动失败、Docker 不可用 | 标记 Blocked 或 Skip |
| 依赖问题 | 缺包、pip install 失败 | 生成依赖修复建议，需要确认 |
| 资产问题 | 模型不存在、HF token 缺失 | 标记 Blocked，提示准备资产 |
| 用例 bug | 变量错误、路径错误、断言错误 | 自动修复用例 |
| 产品/驱动 bug | 命令正确但功能失败 | 生成 Bug 报告，不自动掩盖 |
| 超时问题 | benchmark 太久 | 调整 profile 或 timeout，需评审 |

自动修复循环最多 3 轮。

每轮必须记录：

- 修改了什么。
- 为什么修改。
- 新旧失败是否相同。
- 是否应该停止自动修复。

## 12. 归档与度量

Planning 层必须提前规划归档内容。

### 12.1 归档内容

- 用例计划。
- 生成的 test_\*.sh。
- 辅助脚本。
- 执行命令。
- JUnit XML。
- 日志。
- metrics。
- 失败分类。
- 修复记录。
- merge verdict。

### 12.2 度量指标

| 指标 | 说明 |
|------|------|
| 需求覆盖率 | 每个需求点是否有 case |
| 自动化覆盖率 | P0/P1 中自动化用例占比 |
| 一次通过率 | 生成后首次执行通过比例 |
| 修复成功率 | 自动修复后通过比例 |
| 缺陷发现率 | 用例发现真实问题数量 |
| Blocked 比例 | 环境/资产导致无法执行比例 |
| 平均生成耗时 | 从需求到 case 的时间 |
| 平均验证耗时 | 从 case 到执行结果的时间 |
| token 成本 | 每个 case 的 token 消耗 |

## 13. 建议的 Planner 输出模板

```yaml
case_plan:
  case_id: ""
  title: ""
  suite: ""
  case_name: ""
  priority: "P0|P1|P2|P3"
  test_type: []
  requirement_refs: []
  test_object:
    component: ""
    workload_id: ""
    backend: ""
    devices: ""
  preconditions: []
  test_data: {}
  steps:
    - id: 1
      action: ""
      expected: ""
      evidence: ""
  assertions: []
  skip_conditions: []
  cleanup: []
  observability:
    logs: []
    metrics: []
    junit: true
  tools:
    dry_run: []
    execute: []
    human_confirm_required: []
  risks: []
  review_checklist: []
  execution_plan:
    local_command: ""
    aidevops_task: ""
    timeout_seconds: 0
  archive_plan:
    files: []
    state_json: true
  merge_policy:
    can_auto_merge: false
    required_evidence: []
```

## 14. 最小可用 Planning 流程

P0 阶段可以先实现最小闭环：

1. 接收用户需求。
2. 搜索已有相似用例。
3. 识别目标 suite。
4. 生成 RTM。
5. 生成 case plan。
6. 评审 plan。
7. 生成 test_\*.sh。
8. 静态校验。
9. 本地执行或输出执行命令。
10. 解析结果。
11. 给出 merge verdict。

不要一开始就做全自动下载模型、安装 Docker、远端执行和自动修复。那些属于 P1/P2。

## 15. 结论

Planning 层是 Test Case Agent 的质量核心。

如果没有 Planning，agent 只是一个代码生成器，容易产出不可执行、不可维护、不可追溯的"脚本片段"。

有了 Planning，agent 才能把工业级流程固化下来：

- 需求可追溯。
- 设计可评审。
- 步骤可复现。
- 断言可验证。
- 失败可分类。
- 结果可归档。
- 用例可入库。


## 附录：AI Agent 开发注意事项

第一个大坑是 token 消耗。AI Agent 在处理复杂任务时，会消耗大量的 token，成本很快就上去了。我的解决方案是：

1. 优化 prompt，减少不必要的输出
2. 使用更便宜的模型处理简单任务
3. 实现 token 使用量监控和限制

第二个问题是模型幻觉。有时候 Agent 会给出看起来很合理但实际上错误的信息，这在运维场景下是很危险的。我的应对策略是：

1. 建立知识库，让 Agent 基于已知信息回答问题

第三个问题是稳定性。API 服务偶尔会出现故障或限流，影响 Agent 的正常工作。我的解决方案包括：

1. 配置多个 API 服务作为备份
2. 实现请求重试机制
3. 添加降级处理逻辑

---

**参考链接**：

- <https://github.com/datawhalechina/hello-agents>
- <https://hello-agents.datawhale.cc/#/README.md>
