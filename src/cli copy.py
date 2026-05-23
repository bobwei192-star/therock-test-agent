"""CLI 入口 —— 只做参数解析和调用 cli_runner
放置位置: src/agent/cli/cli.py
"""

import typer
from rich.console import Console
from .cli_runner import CLIRunner, print_final_result

app = typer.Typer(help="TestCaseAgent CLI — 终端调试工具")
console = Console()


@app.command()
def run(
    prompt: str = typer.Argument(..., help="测试需求，自然语言"),
    provider: str = typer.Option("deepseek", "--provider", "-p", help="模型提供商"),
    thread_id: str = typer.Option(
        "cli-default", "--thread", "-t", help="对话线程 ID（复用记忆）"
    ),
    hitl: bool = typer.Option(True, "--hitl/--no-hitl", help="启用人工确认"),
):
    """单次执行：输入需求 → Agent 输出 pytest 用例。"""
    runner = CLIRunner(provider=provider, thread_id=thread_id)
    result = runner.run(prompt, hitl=hitl)
    print_final_result(result)


if __name__ == "__main__":
    app()
