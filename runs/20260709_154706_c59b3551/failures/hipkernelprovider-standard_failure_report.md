# hipkernelprovider-standard 失败报告

> 本报告按 `docs_this_project/问题模板.md` 的单组件问题模板自动生成。
> 模板路径：`/home/zs/TheRock/docs_this_project/问题模板.md`

## 问题标题

hipkernelprovider standard # Discovering available test labels...

## 问题时间

2026-07-09T16:10:29+08:00

## 组件与测试信息

| 字段 | 内容 |
|------|------|
| 组件 | `hipkernelprovider` |
| 测试类型 | `standard` |
| 测试框架 | TheRock test script / CTest / pytest / GoogleTest |
| 测试脚本 | `python3 /home/zs/TheRock/build_tools/github_actions/test_executable_scripts/test_runner.py` |
| 测试命令 | `python3 /home/zs/TheRock/build_tools/github_actions/test_executable_scripts/test_runner.py` |
| 单用例复现命令 | 暂未缩小到单用例 |
| 测试配置文件 | `/home/zs/TheRock/docs_this_project/component_sort_order.json` |
| 超时配置 | 使用 TheRock 测试脚本默认值 |
| 并发配置 | 使用 TheRock 测试脚本默认值 |
| 返回码 / 信号 | `1` |
| 执行耗时 | `0.032s` |
| 日志路径 | stdout: `/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stdout.log`<br>stderr: `/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stderr.log` |

## 问题具体描述

# Discovering available test labels...

## 原始失败结果

| 项目 | 内容 |
|------|------|
| 原始测试结果 | `fail`, rc=`1` |
| 失败用例数量 | 暂未解析 |
| 失败用例名称 | 暂未解析 |
| 原始判断 | 自动分类待补充 |
| 来源位置 | `/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stderr.log` |
| 是否历史失败 | 不确定 |
| 是否本次新增失败 | 不确定 |
| 是否影响 CI 阻塞 | 是 |

## 测试环境

| 项目 | 值 |
|------|----|
| 测试执行人 | OpenCode / 手动触发 |
| 问题发生主机 | 自动采集待补充 |
| OS / Kernel | 自动采集待补充 |
| GPU / 架构 | `gfx1151` |
| ROCm 版本 | `/home/zs/TheRock/output-linux-portable/build/dist/rocm` |
| Python 版本 | 自动采集待补充 |
| `AMDGPU_FAMILIES` | `gfx1151` |
| 关键环境变量 | `ROCM_PATH=/home/zs/TheRock/output-linux-portable/build/dist/rocm` |
| 权限 | sudo_policy=`none` |
| 是否单 GPU | 不确定 |
| 是否发生 GPU reset / ring timeout | 需检查 stderr / dmesg |

## 代码与构建版本

| 项目 | 值 |
|------|----|
| TheRock 仓库路径 | `/home/zs/TheRock` |
| TheRock branch | 自动采集待补充 |
| TheRock commit | 自动采集待补充 |
| TheRock 工作区状态 | 自动采集待补充 |
| 构建目录 | `/home/zs/TheRock/output-linux-portable/build` |
| 安装 / 分发目录 | `/home/zs/TheRock/output-linux-portable/build/dist/rocm` |
| 构建目标架构 | `gfx1151` |

## 复现 / 复测步骤

1. 进入 TheRock 仓库目录。
2. 确认 artifacts 路径：`/home/zs/TheRock/output-linux-portable/build`。
3. 执行命令：`python3 /home/zs/TheRock/build_tools/github_actions/test_executable_scripts/test_runner.py`。
4. 查看 stdout：`/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stdout.log`。
5. 查看 stderr：`/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stderr.log`。

## 复测结果

| 项目 | 结果 |
|------|------|
| 是否复现原问题 | 是 |
| 复测返回码 / 信号 | `1` |
| 复测用例结果 | 暂未解析 |
| 与原结果对比 | 当前为自动复测结果 |
| 复测结论 | `fail` |
| 复测次数 | 见 `global_state.json` loop 记录 |
| 结果稳定性 | 需结合多轮 loop 判断 |

## 问题关键 log

- stdout log：`/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stdout.log`
- stderr log：`/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stderr.log`
- 失败摘要：# Discovering available test labels...

## 问题原因解释

自动初步结论：待人工结合日志、GPU 状态和已知 gfx1151 / ROCm issue 继续分类。

## CI 处理建议

- 保留该任务的 stdout / stderr 日志。
- 如果是环境或 artifacts 缺失，先标记 blocked，不归为组件失败。
- 如果多轮稳定失败，纳入顽固失败集合并生成上游 issue / CI skip 建议。

## 附件与证据

- `global_state.json`: `/home/zs/TheRock/runs/20260709_154706_c59b3551/global_state.json`
- `summary_report.md`: `/home/zs/TheRock/runs/20260709_154706_c59b3551/summary_report.md`
- stdout: `/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stdout.log`
- stderr: `/home/zs/TheRock/runs/20260709_154706_c59b3551/logs/hipkernelprovider-standard.round1.stderr.log`

## 原始模板参考

> 使用方式：本模板只记录一个组件在一次测试类型中的失败、复测和调试过程。
> 如果同一组件在 quick / standard / comprehensive / full 中都有失败，建议分别填写一份。

## 问题标题

（格式建议：`组件名 + 测试类型 + 主要失败现象`，例如 `rocblas comprehensive f16 dot batched kernel abort`）

## 问题时间

（问题发生或复测日期，格式建议：YYYY-MM-DD HH:MM）

## 组件与测试信息

| 字段 | 内容 |
|------|------|
| 组件 | （组件名） |
| 测试类型 | quick / standard / comprehensive / full |
| 测试框架 | CTest / GTest / pytest / dedicated script |
| 测试脚本 | （脚本路径） |
| 测试命令 | （完整命令） |
| 单用例复现命令 | （如 `--gtest_filter=...`、`ctest -R ...`、`pytest path::case`） |
| 测试配置文件 | （test matrix / CTestTestfile / pytest config / 组件配置路径） |
| 超时配置 | （timeout 秒数 / CI timeout / 是否手动放宽） |
| 并发配置 | （CTest `-j`、pytest-xdist、是否串行） |
| 返回码 / 信号 | （rc / signal，例如 rc=1、rc=8、SIGKILL） |
| 执行耗时 | （秒 / 分钟） |
| 日志路径 | （stdout / stderr / CTest log / JSON 结果路径） |

## 问题具体描述

（详细描述该组件的失败现象、失败范围和影响。需要说明是全部失败、部分用例失败、超时、abort、SIGKILL、pytest collection 阻塞，还是架构/环境限制。）

## 原始失败结果

| 项目 | 内容 |
|------|------|
| 原始测试结果 | （例如 `rc=1, 78/670 FAIL`） |
| 失败用例数量 | （PASS / FAIL / SKIP 数量） |
| 失败用例名称 | （列出关键失败用例） |
| 原始判断 | （数值失败 / 超时 / 脚本错误 / 环境问题 / 架构不支持 / flaky 等） |
| 来源位置 | （来源报告章节或原始日志路径） |
| 是否历史失败 | 是 / 否 / 不确定 |
| 是否本次新增失败 | 是 / 否 / 不确定 |
| 是否影响 CI 阻塞 | 是 / 否 |

## 测试环境

| 项目 | 值 |
|------|----|
| 测试执行人 | （CI 执行 / 手动执行 / 执行人姓名） |
| 问题发生主机 | （机器名 / IP） |
| OS / Kernel | （系统和内核版本） |
| GPU / 架构 | （例如 gfx1151） |
| ROCm 版本 | （版本号或安装路径） |
| Python 版本 | （例如 Python 3.14） |
| `AMDGPU_FAMILIES` | （例如 gfx1151） |
| 关键环境变量 | `ROCM_PATH`、`LD_LIBRARY_PATH`、`OUTPUT_ARTIFACTS_DIR` 等 |
| 权限 | root / 普通用户 / sudo |
| 是否单 GPU | 是 / 否 |
| 是否发生 GPU reset / ring timeout | 是 / 否 / 不确定 |
| 测试前系统负载 | （CPU / 内存 / GPU 使用情况，可选） |

## 代码与构建版本

| 项目 | 值 |
|------|----|
| TheRock 仓库路径 | （例如 `/home/zs/TheRock`） |
| TheRock branch | （分支名） |
| TheRock commit | （commit SHA） |
| TheRock 工作区状态 | clean / dirty / 有本地修改 |
| TheRock 本地修改摘要 | （如有本地 patch，说明改了哪些文件） |
| 组件源码版本 | （组件仓库 commit / tag / 子模块版本，如可获取） |
| 测试脚本版本 | （脚本路径、commit、是否本地修改） |
| 构建目录 | （build 目录路径） |
| 安装 / 分发目录 | （ROCm install/dist 目录，例如 `/build/dist/rocm`） |
| 构建类型 | Debug / Release / RelWithDebInfo |
| 构建目标架构 | （例如 gfx1151） |
| 构建产物时间 | （artifact 生成时间） |
| 构建产物 ID | （CI build id / artifact id / 本地构建批次） |
| 编译器版本 | （clang / gcc / hipcc 版本） |
| CMake / Ninja 版本 | （版本号） |
| 依赖锁定信息 | （requirements 文件、pip freeze、系统包版本等） |

## 运行时版本与硬件信息

| 项目 | 值 |
|------|----|
| `rocminfo` 摘要 | （GPU agent、ISA、memory pool 等关键信息） |
| `rocm-smi` 摘要 | （温度、功耗、显存、GPU busy、driver 状态） |
| amdgpu 驱动版本 | （如可获取） |
| HSA runtime 版本 | （如可获取） |
| HIP runtime 版本 | （如可获取） |
| 固件 / BIOS 版本 | （如相关） |
| 内存容量 | （系统内存和可用内存） |
| Swap | 启用 / 未启用，容量 |

## 复现 / 复测步骤

1. （准备环境，例如加载 ROCm 环境变量）
2. （安装依赖，例如 `pip install -r requirements.txt`）
3. （执行测试命令）
4. （收集 stdout、stderr、CTest log、JSON 结果）

## 复测结果

| 项目 | 结果 |
|------|------|
| 是否复现原问题 | 是 / 否 / 部分复现 |
| 复测返回码 / 信号 | （rc / signal） |
| 复测用例结果 | （PASS / FAIL / SKIP 数量） |
| 与原结果对比 | 一致 / 改善 / 新增失败 / 未复现 |
| 复测结论 | PASS / FAIL / SKIP / BLOCKED / FLAKY |
| 复测次数 | （例如 1 次 / 3 次） |
| 结果稳定性 | 稳定复现 / 偶发 / 未复现 / 需要更多样本 |
| 最小复现范围 | 全量组件 / 单 suite / 单 case / 无法缩小 |

## 对照验证

| 对照项 | 结果 |
|--------|------|
| quick 对照 | PASS / FAIL / 未执行 / 不适用 |
| standard 对照 | PASS / FAIL / 未执行 / 不适用 |
| comprehensive 对照 | PASS / FAIL / 未执行 / 不适用 |
| full 对照 | PASS / FAIL / 未执行 / 不适用 |
| 单用例单独运行 | PASS / FAIL / 未执行 / 不适用 |
| 重启后复测 | PASS / FAIL / 未执行 / 不适用 |
| 清理缓存后复测 | PASS / FAIL / 未执行 / 不适用 |
| 换环境 / 换机器验证 | PASS / FAIL / 未执行 / 不适用 |
| 与已知通过组件对比 | （如 hipblas vs rocblas、hipsparse vs rocsparse） |

## 问题关键 log

```text
（只保留能说明问题的关键日志，避免粘贴完整大日志）
```

## 系统关键 log

```text
（如 dmesg、journalctl、GPU reset、ring timeout、OOM killer、amdgpu 报错等）
```

## 调试过程记录

| 步骤 | 操作 | 结果 | 结论 |
|------|------|------|------|
| 1 | （例如单独运行失败用例） | （结果） | （判断） |
| 2 | （例如调整环境变量 / timeout / exclude） | （结果） | （判断） |

## 失败分类

| 分类 | 是否匹配 | 证据 |
|------|:--------:|------|
| 环境配置问题 | 是 / 否 / 不确定 | （缺依赖、路径错误、环境变量缺失等） |
| 测试脚本问题 | 是 / 否 / 不确定 | （脚本路径、测试发现、打包、配置错误等） |
| 组件源码问题 | 是 / 否 / 不确定 | （核心功能或算法稳定失败） |
| 架构 / 硬件限制 | 是 / 否 / 不确定 | （gfx1151 不支持、单 GPU、profiling 计数器限制等） |
| 工具链兼容性 | 是 / 否 / 不确定 | （Python / pytest / CMake / compiler 版本问题） |
| 资源问题 | 是 / 否 / 不确定 | （OOM、超时、SIGKILL、GPU reset、ring timeout） |
| Flaky | 是 / 否 / 不确定 | （多次结果不一致、重跑可过） |

## 问题原因解释

（根因分析。需要明确属于环境配置、测试脚本、组件源码、硬件限制、上游兼容性、资源超时/OOM、GPU reset/ring timeout，还是 flaky。）

## 影响范围

| 项目 | 内容 |
|------|------|
| 影响测试类型 | quick / standard / comprehensive / full |
| 影响用例范围 | 单 case / 单 suite / 多 suite / 全组件 |
| 影响功能范围 | （例如 BLAS1 f16 dot、solver CG、profiling、HIP graph 等） |
| 是否影响其他组件 | 是 / 否 / 不确定 |
| 是否影响发布判断 | 是 / 否 / 不确定 |

## 问题解决办法

（已执行或建议执行的解决方案，例如补环境变量、安装依赖、增加 timeout、排除特定用例、增加 retry、等待上游修复。）

## 修复验证

| 项目 | 结果 |
|------|------|
| 修复内容 | （改了什么配置 / 脚本 / 环境 / 代码） |
| 修复后命令 | （验证命令） |
| 修复后结果 | PASS / FAIL / 部分通过 |
| 是否引入新问题 | 是 / 否 / 不确定 |
| 是否需要回归其他测试类型 | 是 / 否 |

## CI 处理建议

| 项目 | 建议 |
|------|------|
| 是否保留在 CI | 是 / 否 |
| 是否需要 retry | 是 / 否 |
| 是否需要 exclude | 是 / 否 |
| 是否需要调整 timeout | 是 / 否 |
| 是否需要上游修复 | 是 / 否 |
| 是否需要拆分单独 job | 是 / 否 |
| 是否需要串行执行 | 是 / 否 |
| 是否需要 GPU cooldown | 是 / 否 |
| 是否需要收集额外日志 | 是 / 否 |
| 建议处理方式 | 继续测试 / 暂停测试 / 排除该用例 / 排除该组件 / 待观察 |

## 问题状态

（已解决 / 待修复 / 待上游修复 / 待观察 / 已排除）

## 问题解决人

（解决者 / 跟踪者）

## 软件版本

（如上方“代码与构建版本”“运行时版本与硬件信息”已完整填写，本节可只写补充版本信息。）

## 附件与证据

- stdout：
- stderr：
- CTest log：
- JSON 结果：
- 相关脚本：
- dmesg / journalctl：
- rocminfo / rocm-smi：
- core dump / backtrace：
- 构建日志：
- 本地 patch / diff：
