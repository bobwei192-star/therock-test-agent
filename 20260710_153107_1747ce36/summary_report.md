# TheRock Test Summary - 20260710_153107_1747ce36

> 本报告按 `docs_this_project/汇总测试报告.md` 的汇总报告要求自动生成。
> 模板路径：`/home/zs/TheRock/docs_this_project/汇总测试报告.md`

## 基本信息

- 状态：`failed`
- AMDGPU_FAMILIES：`gfx1151`
- THEROCK_AMDGPU_TARGETS：`gfx1151`
- artifacts：`/home/zs/TheRock/output-linux-portable/build`
- build_root：`/home/zs/TheRock/output-linux-portable/build`
- rocm_dist：`/home/zs/TheRock/output-linux-portable/build/dist/rocm`
- sudo_policy：`askpass`
- official_exclude：`/home/zs/TheRock/docs_this_project/official_exclude.json`
- 开始时间：`2026-07-10T15:31:07+08:00`
- 结束时间：`2026-07-10T15:35:59+08:00`

## 模板字段覆盖

- 总任务数：`12`
- 通过数：`4`
- 失败数：`1`
- 跳过数：`6`
- blocked 数：`1`
- flaky 数：`0`
- loop 轮次：`4`
- 最终顽固失败任务数：`2`

## 结果统计

| 状态 | 数量 |
|------|:----:|
| pass | 4 |
| fail | 1 |
| skip | 6 |
| blocked | 1 |
| timeout | 0 |
| flaky | 0 |
| interrupted | 0 |

## Loop 收敛记录

- Round 1: libhipcxx_hiprtc-quick, sanity-quick
- Round 2: libhipcxx_hiprtc-quick, sanity-quick
- Round 3: libhipcxx_hiprtc-quick, sanity-quick
- Round 4: libhipcxx_hiprtc-quick, sanity-quick

## GPU reset 高风险跳过任务

- `rocsparse-quick`
- `rocrtst-quick`
- `hiptests-quick`

## 硬编码路径检测

- `rocfft-quick`: `path_hardcode`，wrapper=`/home/zs/TheRock/runs/20260710_153107_1747ce36/wrappers/rocfft-quick.round1.sh`

## Index 命中规则

| Task | 入口 | 脚本 | Env profiles | Known issue | Official exclude |
|------|------|------|--------------|-------------|------------------|
| `hiprand-quick` | `test_runner` | `test_runner.py` | `test_runner` | `` | `` |
| `hipsparselt-quick` | `dedicated_python` | `test_hipsparselt.py` | `base` | `gfx1151_exclude_family` | `TheRock/上游测试矩阵对 gfx1151 标记 exclude_family，默认不执行。` |
| `hiptests-quick` | `dedicated_python` | `test_hiptests.py` | `base, gpu_reset_sensitive` | `hip_graph_hang` | `` |
| `libhipcxx_hiprtc-quick` | `dedicated_python` | `test_libhipcxx_hiprtc.py` | `base, libhipcxx` | `` | `` |
| `rccl-quick` | `dedicated_python` | `test_rccl.py` | `base` | `` | `` |
| `rocfft-quick` | `dedicated_python` | `test_rocfft.py` | `base` | `flaky_retry_ok` | `` |
| `rocprofiler_compute-quick` | `none` | `test_runner.py` | `base` | `no_independent_entrypoint` | `当前无独立测试入口，runner 不应强行猜测脚本。` |
| `rocroller-quick` | `dedicated_python` | `test_rocroller.py` | `base` | `gfx1151_exclude_family` | `gfx1151 架构枚举不识别且官方 exclude_family，默认不执行。` |
| `rocrtst-quick` | `dedicated_python` | `test_rocrtst.py` | `base, gpu_reset_sensitive` | `sigkill_or_gpu_exclusive` | `` |
| `rocsparse-quick` | `dedicated_python` | `test_rocsparse.py` | `base, gpu_reset_sensitive` | `gpu_ring_timeout_full` | `` |
| `rocthrust-quick` | `test_runner` | `test_runner.py` | `test_runner` | `` | `` |
| `sanity-quick` | `dedicated_python` | `test_sanity.py` | `base` | `` | `` |

## 最终失败 / 阻塞任务

- `libhipcxx_hiprtc-quick`: missing_dependency: lit
- `sanity-quick`: Traceback (most recent call last):

## 报告产物

- 状态文件：`/home/zs/TheRock/runs/20260710_153107_1747ce36/global_state.json`
- Runner 活动日志：`/home/zs/TheRock/runs/20260710_153107_1747ce36/agent_activity.jsonl`
- 环境摘要：`/home/zs/TheRock/runs/20260710_153107_1747ce36/environment_summary.json`
- 日志目录：`/home/zs/TheRock/runs/20260710_153107_1747ce36/logs`
- Wrapper 目录：`/home/zs/TheRock/runs/20260710_153107_1747ce36/wrappers`
- Wrapper 变更日志：`/home/zs/TheRock/runs/20260710_153107_1747ce36/wrapper_changes.jsonl`
- 失败报告目录：`/home/zs/TheRock/runs/20260710_153107_1747ce36/failures`
- 审计日志：`/home/zs/TheRock/runs/20260710_153107_1747ce36/tool_calls.jsonl`
- 全局调用审计：`/home/zs/TheRock/runs/_audit/agent_invocations.jsonl`
