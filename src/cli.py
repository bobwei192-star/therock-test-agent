"""CLI Runner —— 封装 graph.stream + Rich 实时渲染
设计原则：
  1. 零 Graph 修改：不改任何节点代码
  2. 捕获节点 print 输出：通过重定向 stdout 收集调试信息
  3. 最终汇总展示：执行完成后统一打印 RAG/Memory/Tool 信息
  4. HITL 用 input() 避免 Rich Live 冲突刷屏
  5. generator 元信息提取：行数/测试函数/类/import/字符数
  6. 代码自动保存 + 总耗时统计

放置位置: src/agent/cli/cli_runner.py
"""
import sys
import time
import io
import re
from typing import Dict, Any
from contextlib import redirect_stdout
from rich.console import Console
from rich.live import Live
from rich.tree import Tree
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from ..runner import build_runnable_graph, create_initial_state
from ..state import AgentContext

console = Console()

# 节点执行顺序
NODE_NAMES = ["requirement_parser", "context_retriever", "planner", "generator"]

# 节点 -> 状态字段映射
NODE_OUTPUT_KEYS = {
    "requirement_parser": "parsed_requirement",
    "context_retriever": "context",
    "planner": "case_plan",
    "generator": "generated_code",
}

# HITL 节点配置
HITL_NODES = {"planner"}


def _is_valid_text(content) -> bool:
    """判断内容是否为有效文本。"""
    if content is None or isinstance(content, type(None)):
        return False
    if not isinstance(content, str):
        return True
    stripped = content.strip()
    return bool(stripped) and stripped.lower() not in ("none", "null", "")


def _extract_summary(node_name: str, node_output: Dict[str, Any]) -> str:
    """从节点输出中提取可读摘要。"""

    if node_name == "generator":
        code = node_output.get("generated_code") or node_output.get("code", "")
        if not code:
            msgs = node_output.get("messages", [])
            if msgs:
                last = msgs[-1]
                if isinstance(last, dict):
                    code = str(last.get("content", ""))
                else:
                    code = str(getattr(last, "content", last))
        if _is_valid_text(code):
            lines = code.split("
")
            test_funcs = [l for l in lines if l.strip().startswith("def test_")]
            test_classes = [l for l in lines if l.strip().startswith("class Test")]
            imports = [l for l in lines if l.strip().startswith("import ") or l.strip().startswith("from ")]
            return (
                f"{len(lines)} 行 | {len(test_funcs)} 个测试函数 | "
                f"{len(test_classes)} 个测试类 | {len(imports)} 个 import | {len(code)} 字符"
            )
        return "无代码"

    key = NODE_OUTPUT_KEYS.get(node_name)
    content = node_output.get(key) if key else None

    if _is_valid_text(content):
        if isinstance(content, dict):
            if node_name == "context_retriever":
                phase = content.get("phase", "")
                roots = content.get("reference_roots", [])
                return f"phase={phase}, roots={len(roots)} dirs"
            return str(content)[:200]
        if isinstance(content, str):
            txt = content.strip()
            if len(txt) > 300:
                return txt[:300] + "..."
            return txt
        return str(content)[:300]

    msgs = node_output.get("messages", [])
    if msgs:
        last = msgs[-1]
        if isinstance(last, dict):
            txt = str(last.get("content", ""))
        else:
            txt = str(getattr(last, "content", last))
        if _is_valid_text(txt):
            txt = txt.strip()
            if len(txt) > 300:
                return txt[:300] + "..."
            return txt

    return ""


class CLIRunner:
    def __init__(self, provider: str = None, thread_id: str = "cli", hitl: bool = True):
        self.graph = build_runnable_graph(
            provider=provider,
            enable_checkpoint=True,
            enable_store=True,
        )
        self.config = {"configurable": {"thread_id": thread_id}}
        self.hitl_enabled = hitl
        self.outputs: Dict[str, str] = {}
        # 收集各节点的调试输出
        self.debug_logs: Dict[str, list] = {name: [] for name in NODE_NAMES}

    def run(self, prompt: str) -> Dict[str, Any]:
        """单次执行：输入需求 -> 实时展示节点树 -> 返回完整状态。"""
        state = create_initial_state(prompt)
        context = AgentContext(user_id="cli_user")
        total_start = time.time()

        # Rich 实时树
        tree = Tree("🧪 TestCaseAgent", guide_style="bold cyan")
        node_branches = {}
        for name in NODE_NAMES:
            branch = tree.add(f"[dim]○ {name}[/dim]")
            node_branches[name] = branch

        final_output = None

        with Live(tree, console=console, refresh_per_second=4) as live:
            try:
                for chunk in self.graph.stream(
                    state,
                    config=self.config,
                    context=context,
                    stream_mode="updates",
                ):
                    for node_name, node_output in chunk.items():
                        if node_name not in node_branches:
                            continue

                        start_time = time.time()

                        # 1. 标记执行中
                        label = Text()
                        label.append(f"⚡ {node_name}", style="bold yellow")
                        label.append(" 执行中...", style="dim")
                        node_branches[node_name].label = label
                        live.update(tree)

                        # 2. 提取摘要
                        summary = _extract_summary(node_name, node_output)
                        self.outputs[node_name] = summary
                        if summary:
                            node_branches[node_name].add(Text(summary, style="dim"))

                        # 3. HITL：关键节点暂停
                        if self.hitl_enabled and node_name in HITL_NODES:
                            label = Text()
                            label.append(f"⏸️ {node_name}", style="bold magenta")
                            label.append(" 等待确认...", style="dim")
                            node_branches[node_name].label = label
                            live.update(tree)

                            # 暂停 Live，避免与 input() 冲突
                            live.stop()
                            approved = self._hitl_confirm(node_name, summary)

                            if not approved:
                                console.print("
[red]❌ 用户拒绝，终止执行[/red]")
                                return node_output

                            # 恢复 Live
                            live.start()
                            elapsed = time.time() - start_time
                            label = Text()
                            label.append(f"✅ {node_name}", style="bold green")
                            label.append(f" ({len(summary)} chars, {elapsed:.1f}s)", style="dim")
                            node_branches[node_name].label = label
                            live.update(tree)
                        else:
                            # 非 HITL 节点，直接完成
                            elapsed = time.time() - start_time
                            label = Text()
                            label.append(f"✅ {node_name}", style="bold green")
                            label.append(f" ({len(summary)} chars, {elapsed:.1f}s)", style="dim")
                            node_branches[node_name].label = label
                            live.update(tree)

                        final_output = node_output

            except Exception as e:
                console.print(f"
[bold red]❌ Graph 执行出错: {e}[/bold red]")
                raise

        total_elapsed = time.time() - total_start
        console.print(f"
[dim]⏱️ 总耗时: {total_elapsed:.1f}s[/dim]")

        # 获取完整状态
        try:
            full_state = self.graph.get_state(self.config)
            result = full_state.values if full_state else (final_output or {})
        except Exception:
            result = final_output or {}

        return result

    def _hitl_confirm(self, node_name: str, content: str) -> bool:
        """终端阻塞 HITL —— 使用 input() 避免 Rich 冲突。"""
        console.print("
")
        display = content[:1200] if content else "(无内容)"
        console.print(Panel(
            display,
            title=f"[bold yellow]🔍 {node_name} 产出确认[/]",
            border_style="yellow"
        ))
        # 用原始 input 代替 Confirm.ask，避免 Rich Live 冲突
        choice = input("
确认并继续? [Y/n]: ").strip().lower()
        return choice in ("", "y", "yes")


def _extract_rag_info(state: Dict[str, Any]) -> Dict[str, Any]:
    """从 state 中提取 RAG 信息。"""
    context = state.get("context", {})
    if not isinstance(context, dict):
        return {}

    return {
        "phase": context.get("phase", "unknown"),
        "chunks": len(context.get("retrieved_knowledge", "")) if isinstance(context.get("retrieved_knowledge"), str) else 0,
        "sources": context.get("retrieved_sources", []),
        "roots": context.get("reference_roots", []),
    }


def _extract_memory_info(state: Dict[str, Any]) -> Dict[str, Any]:
    """从 state 中提取 Memory 信息。"""
    # Short Memory: Checkpointer 管理的 thread 状态
    short_mem = {
        "thread_id": state.get("thread_id", "cli-default"),
        "retry_count": state.get("retry", 0),
        "repair_count": state.get("repair_count", 0),
    }

    # Long Memory: Store 中的记忆（通过节点 DEBUG 输出获取）
    # 这里只能从 state 中推断
    long_mem = {
        "plans_stored": bool(state.get("case_plan")),
        "generations_stored": bool(state.get("generated_code")),
        "requirements_stored": bool(state.get("parsed_requirement")),
    }

    return {"short": short_mem, "long": long_mem}


def _extract_tool_info(state: Dict[str, Any]) -> list:
    """从 state 中提取 Tool Use 信息。"""
    tools = []

    # 检查是否有文件保存
    if state.get("generated_code") or state.get("code"):
        tools.append({"name": "save_to_file", "status": "success", "detail": "代码已生成"})

    # 检查 validation_result 中是否有工具调用痕迹
    validation = state.get("validation_result", {})
    if isinstance(validation, dict) and validation.get("status"):
        tools.append({"name": "code_validator", "status": validation["status"], "detail": str(validation.get("errors", []))[:100]})

    return tools


def print_debug_summary(state: Dict[str, Any]):
    """打印调试信息汇总面板。"""
    console.print("
" + "━" * 60)
    console.print("[bold cyan]📊 调试信息汇总[/bold cyan]
")

    # ====== RAG 信息 ======
    rag = _extract_rag_info(state)
    if rag:
        console.print("[bold blue]🔍 RAG 检索[/bold blue]")
        rag_table = Table(show_header=False, box=None, padding=(0, 2))
        rag_table.add_row("Phase", str(rag.get("phase", "unknown")))
        rag_table.add_row("检索字符数", str(rag.get("chunks", 0)))
        rag_table.add_row("来源文档数", str(len(rag.get("sources", []))))
        rag_table.add_row("参考根目录", str(len(rag.get("roots", []))))
        console.print(rag_table)

        sources = rag.get("sources", [])
        if sources:
            console.print("[dim]  来源文档:[/dim]")
            for src in sources[:5]:
                console.print(f"    - {src}")
            if len(sources) > 5:
                console.print(f"    ... 共 {len(sources)} 个来源")
        console.print()

    # ====== Memory 信息 ======
    mem = _extract_memory_info(state)
    console.print("[bold blue]💾 Memory 状态[/bold blue]")
    mem_table = Table(show_header=False, box=None, padding=(0, 2))

    short = mem.get("short", {})
    mem_table.add_row("Short Memory (Checkpointer)", f"thread_id={short.get('thread_id', 'n/a')}")
    mem_table.add_row("  - retry_count", str(short.get("retry_count", 0)))
    mem_table.add_row("  - repair_count", str(short.get("repair_count", 0)))

    long = mem.get("long", {})
    mem_table.add_row("Long Memory (InMemoryStore)", "")
    mem_table.add_row("  - plans", "✅ 已存储" if long.get("plans_stored") else "❌ 未存储")
    mem_table.add_row("  - generations", "✅ 已存储" if long.get("generations_stored") else "❌ 未存储")
    mem_table.add_row("  - requirements", "✅ 已存储" if long.get("requirements_stored") else "❌ 未存储")

    console.print(mem_table)
    console.print()

    # ====== Tool Use 信息 ======
    tools = _extract_tool_info(state)
    if tools:
        console.print("[bold blue]🛠️ Tool Use[/bold blue]")
        tool_table = Table(show_header=True, box=None, padding=(0, 2))
        tool_table.add_column("工具", style="cyan")
        tool_table.add_column("状态", style="green")
        tool_table.add_column("详情", style="dim")

        for tool in tools:
            status_color = "green" if tool["status"] == "success" or tool["status"] == "passed" else "red"
            tool_table.add_row(
                tool["name"],
                f"[{status_color}]{tool['status']}[/]",
                tool["detail"]
            )
        console.print(tool_table)
    else:
        console.print("[bold blue]🛠️ Tool Use[/bold blue]")
        console.print("  [dim]无工具调用记录[/dim]")

    console.print()


def print_final_result(state: Dict[str, Any]):
    """打印最终结果面板。"""
    code = state.get("generated_code") or state.get("code", "")
    plan = state.get("case_plan", "")
    explanation = state.get("explanation", "")
    validation = state.get("validation_result", {})

    console.print("
" + "━" * 60)
    console.print("[bold green]✅ 执行完成[/bold green]
")

    if plan:
        console.print(Panel(plan[:2000], title="📋 测试计划", border_style="blue"))

    if code:
        if len(code) > 3000:
            from pathlib import Path
            from datetime import datetime
            out_dir = Path("output")
            out_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_file = out_dir / f"test_generated_{timestamp}.py"
            out_file.write_text(code, encoding="utf-8")
            console.print(Panel(
                code[:3000],
                title="🐍 生成代码 (前 3000 字符)",
                border_style="green"
            ))
            console.print(
                f"[bold yellow]💾 完整代码 ({len(code)} 字符) 已保存到 {out_file}[/bold yellow]"
            )
        else:
            console.print(Panel(code, title="🐍 生成代码", border_style="green"))

    if explanation:
        console.print(Panel(explanation[:1500], title="📝 说明", border_style="cyan"))

    if isinstance(validation, dict) and validation.get("status"):
        status = validation.get("status", "unknown")
        errors = validation.get("errors", [])
        color = "green" if status == "passed" else "red"
        console.print(f"
[bold {color}]🧪 验证结果: {status}[/]")
        if errors:
            for err in errors[:5]:
                console.print(f"  [red]- {err}[/]")

    # 打印调试信息汇总
    print_debug_summary(state)

    console.print("[dim]💾 记忆已自动保存 (由 Agent 层 MemorySaver 管理)[/dim]
")