from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .audit import append_activity
from .audit import now_iso
from .config import read_optional_text


def summarize_counts(state: dict[str, Any]) -> dict[str, int]:
    counts = {"pass": 0, "fail": 0, "skip": 0, "blocked": 0, "timeout": 0, "flaky": 0, "interrupted": 0}
    for result in state["results"]["task_results"].values():
        status = result.get("status", "blocked")
        counts[status] = counts.get(status, 0) + 1
    return counts


def generate_reports(state: dict[str, Any], project_root: Path, summary_template: Path) -> None:
    output_dir = Path(state["meta"]["output_dir"])
    counts = summarize_counts(state)
    history = state["loop"]["failed_task_history"]
    total_tasks = len(state["schedule"]["task_queue"]) + len(state["schedule"]["skipped_tasks"])
    final_failures = [
        result
        for result in state["results"]["task_results"].values()
        if result.get("status") in {"fail", "blocked", "timeout", "interrupted"}
    ]
    skipped_risk = [
        result["task_id"]
        for result in state["results"]["task_results"].values()
        if result.get("status") == "skip" and result.get("gpu_hang_risk")
    ]
    path_hardcode_results = [
        result
        for result in state["results"]["task_results"].values()
        if result.get("path_hardcode_detection", {}).get("detected")
    ]

    lines = [
        f"# TheRock Test Summary - {state['run_id']}",
        "",
        f"> 本报告按 `docs_this_project/汇总测试报告.md` 的汇总报告要求自动生成。",
        f"> 模板路径：`{summary_template}`",
        "",
        "## 基本信息",
        "",
        f"- 状态：`{state['final_status']}`",
        f"- AMDGPU_FAMILIES：`{state['meta'].get('amdgpu_families', state['meta'].get('gpu_model', ''))}`",
        f"- THEROCK_AMDGPU_TARGETS：`{state['meta'].get('amdgpu_targets', '')}`",
        f"- artifacts：`{state['meta']['artifacts_path']}`",
        f"- build_root：`{state['meta']['build_root']}`",
        f"- rocm_dist：`{state['meta']['rocm_dist']}`",
        f"- sudo_policy：`{state['meta'].get('sudo_policy', 'none')}`",
        f"- official_exclude：`{state['meta'].get('official_exclude', '')}`",
        f"- 开始时间：`{state['start_time']}`",
        f"- 结束时间：`{state.get('end_time')}`",
        "",
        "## 模板字段覆盖",
        "",
        f"- 总任务数：`{total_tasks}`",
        f"- 通过数：`{counts.get('pass', 0)}`",
        f"- 失败数：`{counts.get('fail', 0)}`",
        f"- 跳过数：`{counts.get('skip', 0)}`",
        f"- blocked 数：`{counts.get('blocked', 0)}`",
        f"- flaky 数：`{counts.get('flaky', 0)}`",
        f"- loop 轮次：`{len(history)}`",
        f"- 最终顽固失败任务数：`{len(final_failures)}`",
        "",
        "## 结果统计",
        "",
        "| 状态 | 数量 |",
        "|------|:----:|",
    ]
    for key in ("pass", "fail", "skip", "blocked", "timeout", "flaky", "interrupted"):
        lines.append(f"| {key} | {counts.get(key, 0)} |")

    lines.extend(["", "## Loop 收敛记录", ""])
    for item in history:
        failed = ", ".join(item["failed_tasks"]) if item["failed_tasks"] else "无"
        lines.append(f"- Round {item['round']}: {failed}")

    lines.extend(["", "## GPU reset 高风险跳过任务", ""])
    if skipped_risk:
        lines.extend(f"- `{task_id}`" for task_id in skipped_risk)
    else:
        lines.append("- 无")

    lines.extend(["", "## 硬编码路径检测", ""])
    if path_hardcode_results:
        for result in path_hardcode_results:
            categories = ", ".join(result.get("path_hardcode_detection", {}).get("categories") or [])
            wrapper_path = result.get("wrapper_path") or "无"
            lines.append(f"- `{result['task_id']}`: `{categories}`，wrapper=`{wrapper_path}`")
    else:
        lines.append("- 未检测到硬编码路径特征")

    lines.extend(
        [
            "",
            "## Index 命中规则",
            "",
            "| Task | 入口 | 脚本 | Env profiles | Known issue | Official exclude |",
            "|------|------|------|--------------|-------------|------------------|",
        ]
    )
    for result in sorted(state["results"]["task_results"].values(), key=lambda item: item["task_id"]):
        profiles = ", ".join(result.get("env_profiles") or [])
        official_reason = ""
        if result.get("official_exclude"):
            official_reason = str(result["official_exclude"].get("reason", "official exclude"))
        lines.append(
            "| "
            f"`{result['task_id']}` | "
            f"`{result.get('entrypoint_type', '')}` | "
            f"`{result.get('script', '')}` | "
            f"`{profiles}` | "
            f"`{result.get('known_issue_category') or ''}` | "
            f"`{official_reason}` |"
        )

    lines.extend(["", "## 最终失败 / 阻塞任务", ""])
    if final_failures:
        for result in final_failures:
            lines.append(f"- `{result['task_id']}`: {result.get('failure_summary', '')}")
    else:
        lines.append("- 无")

    lines.extend(
        [
            "",
            "## 报告产物",
            "",
            f"- 状态文件：`{output_dir / 'global_state.json'}`",
            f"- Runner 活动日志：`{output_dir / 'agent_activity.jsonl'}`",
            f"- 环境摘要：`{output_dir / 'environment_summary.json'}`",
            f"- 日志目录：`{output_dir / 'logs'}`",
            f"- Wrapper 目录：`{output_dir / 'wrappers'}`",
            f"- Wrapper 变更日志：`{output_dir / 'wrapper_changes.jsonl'}`",
            f"- 失败报告目录：`{output_dir / 'failures'}`",
            f"- 审计日志：`{output_dir / 'tool_calls.jsonl'}`",
            f"- 全局调用审计：`{project_root / 'runs' / '_audit' / 'agent_invocations.jsonl'}`",
        ]
    )

    (output_dir / "summary_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    append_activity(
        state,
        "report_generated",
        {
            "summary_report": str(output_dir / "summary_report.md"),
            "failure_count": len(final_failures),
        },
    )


def write_failure_report(state: dict[str, Any], result: dict[str, Any], failure_template: Path) -> None:
    output_dir = Path(state["meta"]["output_dir"])
    template = read_optional_text(failure_template)
    meta = state["meta"]
    content = [
        f"# {result['task_id']} 失败报告",
        "",
        f"> 本报告按 `docs_this_project/问题模板.md` 的单组件问题模板自动生成。",
        f"> 模板路径：`{failure_template}`",
        "",
        "## 问题标题",
        "",
        f"{result['component']} {result['test_type']} {result.get('failure_summary', '测试失败')}",
        "",
        "## 问题时间",
        "",
        result.get("finished_at", now_iso()),
        "",
        "## 组件与测试信息",
        "",
        "| 字段 | 内容 |",
        "|------|------|",
        f"| 组件 | `{result['component']}` |",
        f"| 测试类型 | `{result['test_type']}` |",
        "| 测试框架 | TheRock test script / CTest / pytest / GoogleTest |",
        f"| 入口类型 | `{result.get('entrypoint_type', '')}` |",
        f"| 入口脚本 | `{result.get('script', '')}` |",
        f"| TEST_COMPONENT | `{result.get('test_component') or ''}` |",
        f"| Env profiles | `{', '.join(result.get('env_profiles') or [])}` |",
        f"| Known issue 分类 | `{result.get('known_issue_category') or ''}` |",
        f"| Official exclude | `{json.dumps(result.get('official_exclude'), ensure_ascii=False) if result.get('official_exclude') else ''}` |",
        f"| Wrapper | `{result.get('wrapper_path') or ''}` |",
        f"| 测试脚本 | `{result.get('command', '')}` |",
        f"| 原始测试命令 | `{result.get('original_command', '')}` |",
        f"| 测试命令 | `{result.get('command', '')}` |",
        "| 单用例复现命令 | 暂未缩小到单用例 |",
        f"| 测试配置文件 | `{meta.get('component_config', '')}` |",
        "| 超时配置 | 使用 TheRock 测试脚本默认值 |",
        "| 并发配置 | 使用 TheRock 测试脚本默认值 |",
        f"| 返回码 / 信号 | `{result.get('return_code')}` |",
        f"| 执行耗时 | `{result.get('duration_seconds')}s` |",
        f"| 日志路径 | stdout: `{result.get('stdout_log')}`<br>stderr: `{result.get('stderr_log')}` |",
        f"| Wrapper 环境变更 | `{', '.join(result.get('wrapper_env_change_keys') or [])}` |",
        "",
        "## 问题具体描述",
        "",
        result.get("failure_summary") or "任务返回非 0 或被标记为 blocked，需要结合日志继续分析。",
        "",
        "## 原始失败结果",
        "",
        "| 项目 | 内容 |",
        "|------|------|",
        f"| 原始测试结果 | `{result.get('status')}`, rc=`{result.get('return_code')}` |",
        "| 失败用例数量 | 暂未解析 |",
        "| 失败用例名称 | 暂未解析 |",
        "| 原始判断 | 自动分类待补充 |",
        f"| 来源位置 | `{result.get('stderr_log')}` |",
        "| 是否历史失败 | 不确定 |",
        "| 是否本次新增失败 | 不确定 |",
        "| 是否影响 CI 阻塞 | 是 |",
        "",
        "## 测试环境",
        "",
        "| 项目 | 值 |",
        "|------|----|",
        "| 测试执行人 | OpenCode / 手动触发 |",
        "| 问题发生主机 | 自动采集待补充 |",
        "| OS / Kernel | 自动采集待补充 |",
        f"| GPU / 架构 | `{meta.get('amdgpu_families', meta.get('gpu_model', ''))}` |",
        f"| ROCm 版本 | `{meta.get('rocm_dist', '')}` |",
        "| Python 版本 | 自动采集待补充 |",
        f"| `AMDGPU_FAMILIES` | `{meta.get('amdgpu_families', '')}` |",
        f"| 关键环境变量 | `ROCM_PATH={meta.get('rocm_dist', '')}`, `OUTPUT_ARTIFACTS_DIR={meta.get('rocm_dist', '')}` |",
        f"| 权限 | sudo_policy=`{meta.get('sudo_policy', 'none')}` |",
        "| 是否单 GPU | 不确定 |",
        "| 是否发生 GPU reset / ring timeout | 需检查 stderr / dmesg |",
        "",
        "## 代码与构建版本",
        "",
        "| 项目 | 值 |",
        "|------|----|",
        f"| TheRock 仓库路径 | `{meta.get('therock_repo_path', '')}` |",
        "| TheRock branch | 自动采集待补充 |",
        "| TheRock commit | 自动采集待补充 |",
        "| TheRock 工作区状态 | 自动采集待补充 |",
        f"| 构建目录 | `{meta.get('build_root', '')}` |",
        f"| 安装 / 分发目录 | `{meta.get('rocm_dist', '')}` |",
        f"| 构建目标架构 | `{meta.get('amdgpu_families', '')}` |",
        f"| 组件运行索引 | `{meta.get('component_env_index', '')}` |",
        f"| 官方排除索引 | `{meta.get('official_exclude', '')}` |",
        "",
        "## 复现 / 复测步骤",
        "",
        "1. 进入 TheRock 仓库目录。",
        f"2. 确认 artifacts 路径：`{meta.get('artifacts_path', '')}`。",
        f"3. 执行命令：`{result.get('command', '')}`。",
        f"4. 查看 stdout：`{result.get('stdout_log')}`。",
        f"5. 查看 stderr：`{result.get('stderr_log')}`。",
        "",
        "## 复测结果",
        "",
        "| 项目 | 结果 |",
        "|------|------|",
        "| 是否复现原问题 | 是 |",
        f"| 复测返回码 / 信号 | `{result.get('return_code')}` |",
        "| 复测用例结果 | 暂未解析 |",
        "| 与原结果对比 | 当前为自动复测结果 |",
        f"| 复测结论 | `{result.get('status')}` |",
        "| 复测次数 | 见 `global_state.json` loop 记录 |",
        "| 结果稳定性 | 需结合多轮 loop 判断 |",
        "",
        "## 问题关键 log",
        "",
        f"- stdout log：`{result.get('stdout_log')}`",
        f"- stderr log：`{result.get('stderr_log')}`",
        f"- 失败摘要：{result.get('failure_summary', '')}",
        "",
        "## 问题原因解释",
        "",
        "自动初步结论：待人工结合日志、GPU 状态和已知 gfx1151 / ROCm issue 继续分类。",
        "",
        "## 硬编码路径检测",
        "",
        json.dumps(result.get("path_hardcode_detection", {}), ensure_ascii=False, indent=2),
        "",
        "## CI 处理建议",
        "",
        "- 保留该任务的 stdout / stderr 日志。",
        "- 如果是环境或 artifacts 缺失，先标记 blocked，不归为组件失败。",
        "- 如果多轮稳定失败，纳入顽固失败集合并生成上游 issue / CI skip 建议。",
        "",
        "## 附件与证据",
        "",
        f"- `global_state.json`: `{output_dir / 'global_state.json'}`",
        f"- `summary_report.md`: `{output_dir / 'summary_report.md'}`",
        f"- stdout: `{result.get('stdout_log')}`",
        f"- stderr: `{result.get('stderr_log')}`",
        f"- wrapper: `{result.get('wrapper_path') or ''}`",
        f"- wrapper changes: `{output_dir / 'wrapper_changes.jsonl'}`",
        "",
        "## 原始模板参考",
        "",
        template or "未找到 docs_this_project/问题模板.md。",
    ]
    (output_dir / "failures" / f"{result['task_id']}_failure_report.md").write_text(
        "\n".join(content) + "\n",
        encoding="utf-8",
    )
