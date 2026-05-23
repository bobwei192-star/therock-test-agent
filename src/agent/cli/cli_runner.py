"""CLI Runner —— 封装 graph.stream + Rich 实时渲染 + HITL"""

import re
from pathlib import Path
from typing import Any, Dict

from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree

from ..runner import build_runnable_graph, create_initial_state
from ..state import AgentContext
from ..input_filter import clean_input, is_meaningful

console = Console()

NODE_NAMES = ["requirement_parser", "context_retriever", "planner", "generator"]

NODE_OUTPUT_KEYS = {
    "requirement_parser": "parsed_requirement",
    "context_retriever": "context",
    "planner": "case_plan",
    "generator": "generated_code",
}

# ✅ 修复 1：取消注释，放到全局作用域
HITL_NODES = {"planner"}

_CODE_PREVIEW_CHARS = 2000
_CODE_SAVE_DIR = "output"


def _extract_code_from_messages(node_output: Dict[str, Any]) -> str:
    msgs = node_output.get("messages", [])
    if not msgs:
        return ""
    last = msgs[-1]
    raw = ""
    if isinstance(last, dict):
        raw = str(last.get("content", ""))
    else:
        raw = str(getattr(last, "content", last))
    m = re.search(r"```python\s*(.*?)\s*```", raw, re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.search(r"```\s*(.*?)\s*```", raw, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def _extract_summary(node_name: str, node_output: Dict[str, Any]) -> str:
    if node_name == "generator":
        code = (
            node_output.get("generated_code")
            or node_output.get("code")
            or _extract_code_from_messages(node_output)
        )
        if code:
            func_count = len(re.findall(r"def test_", code))
            return f"生成代码 {len(code)} chars, {func_count} 个测试函数"
        exp = node_output.get("explanation", "")
        if exp:
            return f"说明: {exp[:200]}"
        msgs = node_output.get("messages", [])
        if msgs:
            last = msgs[-1]
            raw = str(
                last.get("content", "")
                if isinstance(last, dict)
                else getattr(last, "content", last)
            )
            return f"LLM 响应 {len(raw)} chars"
        return "已生成"

    key = NODE_OUTPUT_KEYS.get(node_name)
    if key:
        content = node_output.get(key)
        if isinstance(content, str) and content.strip():
            return content[:300]
        if isinstance(content, dict):
            if node_name == "context_retriever":
                keys = list(content.keys())
                return f"上下文就绪 ({len(keys)} 个字段: {', '.join(keys[:4])})"
            return str(content)[:200]

    msgs = node_output.get("messages", [])
    if msgs:
        for msg in reversed(msgs):
            if isinstance(msg, dict):
                text = str(msg.get("content", ""))
            else:
                text = str(getattr(msg, "content", msg))
            if text.strip():
                return text[:300]
    return ""


# ─── 新增：信息提取函数 ──────────────────────────────

def _extract_rag_info(state: Dict[str, Any]) -> Dict[str, Any]:
    """提取 RAG 检索信息"""
    ctx = state.get("context", {})
    chunks = ctx.get("chunks", [])
    sources = ctx.get("sources", [])
    roots = ctx.get("roots", [])
    total_chars = sum(len(str(c)) for c in chunks) if isinstance(chunks, list) else 0
    return {
        "phase": ctx.get("phase", "unknown"),
        "chunks": total_chars,
        "sources": sources,
        "roots": len(roots) if isinstance(roots, list) else 0,
    }


def _extract_memory_info(state: Dict[str, Any], thread_id: str = "unknown") -> Dict[str, Any]:
    """提取 Memory 状态信息"""
    return {
        "thread_id": thread_id,
        "retry_count": state.get("retry_count", 0),
        "repair_count": state.get("repair_count", 0),
        "plans": bool(state.get("case_plan")),
        "generations": bool(state.get("generated_code")),
        "requirements": bool(state.get("parsed_requirement")),
    }


def _extract_tool_info(state: Dict[str, Any]) -> Dict[str, Any]:
    """提取 Tool Use 信息"""
    validation = state.get("validation_result", {})
    if not isinstance(validation, dict):
        return {}
    status = validation.get("status", "unknown")
    errors = validation.get("errors", [])
    return {
        "save_to_file": "success" if state.get("generated_code") else "unknown",
        "code_validator": status,
        "details": errors,
    }


# ─── 新增：调试信息汇总面板 ────────────────────────────

def print_debug_summary(state: Dict[str, Any], thread_id: str = "unknown"):
    """执行完成后统一展示调试信息"""
    console.print("\n" + "━" * 60)
    console.print("📊 调试信息汇总\n")

    # 🔍 RAG 检索
    rag = _extract_rag_info(state)
    console.print("[bold]🔍 RAG 检索[/bold]")
    console.print(f"  Phase          {rag.get('phase', 'unknown')}")
    console.print(f"  检索字符数     {rag.get('chunks', 0)}")
    console.print(f"  来源文档数     {len(rag.get('sources', []))}")
    console.print(f"  参考根目录     {rag.get('roots', 0)}")
    if rag.get("sources"):
        console.print("  来源文档:")
        for src in rag.get("sources", [])[:5]:
            console.print(f"    - {src}")
    console.print()

    # 💾 Memory 状态
    mem = _extract_memory_info(state, thread_id)
    console.print("[bold]💾 Memory 状态[/bold]")
    console.print(f"  Short Memory (Checkpointer)    thread_id={mem['thread_id']}")
    console.print(f"    - retry_count                {mem['retry_count']}")
    console.print(f"    - repair_count               {mem['repair_count']}")
    console.print("  Long Memory (InMemoryStore)")
    console.print(f"    - plans                      {'✅ 已存储' if mem['plans'] else '❌ 未存储'}")
    console.print(f"    - generations                {'✅ 已存储' if mem['generations'] else '❌ 未存储'}")
    console.print(f"    - requirements               {'✅ 已存储' if mem['requirements'] else '❌ 未存储'}")
    console.print()

    # 🛠️ Tool Use
    tools = _extract_tool_info(state)
    if tools:
        console.print("[bold]🛠️ Tool Use[/bold]")
        console.print(f"  {'工具':<<16} {'状态':<<10} 详情")
        save_status = "✅ success" if tools.get("save_to_file") == "success" else "❌ failed"
        val_status = f"✅ {tools['code_validator']}" if tools.get("code_validator") == "passed" else f"❌ {tools['code_validator']}"
        console.print(f"  {'save_to_file':<<16} {save_status:<10} 代码已生成")
        console.print(f"  {'code_validator':<<16} {val_status:<10} {tools.get('details', [])}")


class CLIRunner:
    def __init__(self, provider: str = None, thread_id: str = "cli", hitl: bool = True):
        self.graph = build_runnable_graph(
            provider=provider,
            enable_checkpoint=True,
            enable_store=True,
        )
        self.config = {"configurable": {"thread_id": thread_id}}
        self.outputs: Dict[str, str] = {}
        self._hitl_enabled = hitl          # ✅ 修复 2：保存 hitl 到实例
        self._thread_id = thread_id

    # ✅ 修复 2：run() 不再接收外部 hitl 参数，统一走 self._hitl_enabled
    def run(self, prompt: str) -> Dict[str, Any]:
        cleaned = clean_input(prompt)
        if not cleaned or not is_meaningful(cleaned):
            console.print("\n[bold red]❌ 输入无效或为空，请重新输入。[/bold red]")
            return {}

        state = create_initial_state(cleaned)
        context = AgentContext(user_id="cli_user")

        tree = Tree("🧪 TestCaseAgent", guide_style="bold cyan")
        node_branches = {}
        for name in NODE_NAMES:
            branch = tree.add(f"[dim]○ {name}[/dim]")
            node_branches[name] = branch

        final_output: Dict[str, Any] = {}

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

                        label = Text()
                        label.append(f"⚡ {node_name}", style="bold yellow")
                        label.append(" 执行中...", style="dim")
                        node_branches[node_name].label = label
                        live.update(tree)

                        summary = _extract_summary(node_name, node_output)
                        self.outputs[node_name] = summary
                        if summary:
                            node_branches[node_name].add(Text(summary, style="dim"))

                        # ✅ 修复 2：用 self._hitl_enabled 替代外部 hitl 变量
                        if self._hitl_enabled and node_name in HITL_NODES:
                            label = Text()
                            label.append(f"⏸️ {node_name}", style="bold magenta")
                            label.append(" 等待确认...", style="dim")
                            node_branches[node_name].label = label
                            live.update(tree)

                            if not self._hitl_confirm(node_name, summary):
                                console.print("\n[red]❌ 用户拒绝，终止执行[/red]")
                                return node_output

                        label = Text()
                        label.append(f"✅ {node_name}", style="bold green")
                        label.append(f" ({len(summary)} chars)", style="dim")
                        node_branches[node_name].label = label
                        live.update(tree)

                        final_output = node_output

            except Exception as e:
                console.print(f"\n[bold red]❌ Graph 执行出错: {e}[/bold red]")
                raise

        try:
            full_state = self.graph.get_state(self.config)
            return full_state.values if full_state else (final_output or {})
        except Exception:
            return final_output or {}

    # ✅ 修复 3：改用 input() 避免 Rich Live 冲突
    def _hitl_confirm(self, node_name: str, content: str) -> bool:
        console.print("\n")
        display = content[:1200] if content else "(无内容)"
        console.print(
            Panel(
                display,
                title=f"[bold yellow]🔍 {node_name} 产出确认[/]",
                border_style="yellow",
            )
        )
        choice = input("\n确认并继续? [Y/n]: ").strip().lower()
        return choice in ("", "y", "yes")


def print_final_result(state: Dict[str, Any]):
    code = state.get("generated_code") or state.get("code") or ""
    plan = state.get("case_plan") or ""
    explanation = state.get("explanation") or ""
    validation = state.get("validation_result", {})

    console.print("\n" + "━" * 60)
    console.print("[bold green]✅ 执行完成[/bold green]\n")

    if plan:
        plan_label = f"📋 测试计划 ({len(plan)} 字符)"
        console.print(Panel(plan[:3000], title=plan_label, border_style="blue"))
    if code:
        code_label = f"🐍 生成代码 ({len(code)} 字符)"
        if len(code) > _CODE_PREVIEW_CHARS:
            code_label += f" — 前 {_CODE_PREVIEW_CHARS} 字符"
        console.print(
            Panel(code[:_CODE_PREVIEW_CHARS], title=code_label, border_style="green")
        )
    if explanation:
        console.print(Panel(explanation[:1500], title="📝 说明", border_style="cyan"))

    if isinstance(validation, dict) and validation.get("status"):
        status = validation.get("status", "unknown")
        errors = validation.get("errors", [])
        color = "green" if status == "passed" else "red"
        console.print(f"\n[bold {color}]🧪 验证结果: {status}[/]")
        if errors:
            for err in errors[:5]:
                console.print(f"  [red]- {err}[/]")

    if code:
        dest = _save_code(code)
        if dest:
            console.print(
                f"\n[bold green]💾 完整代码 ({len(code)} 字符) 已保存到 {dest}[/]"
            )

    # ✅ 新增：调试信息汇总
    print_debug_summary(state)

    console.print("\n[dim]💾 记忆已自动保存[/dim]\n")


def _save_code(code: str) -> str | None:
    if not code or not code.strip():
        return None
    out_dir = Path(_CODE_SAVE_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    from datetime import datetime

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = out_dir / f"test_generated_{ts}.py"
    dest.write_text(code, encoding="utf-8")
    return str(dest)