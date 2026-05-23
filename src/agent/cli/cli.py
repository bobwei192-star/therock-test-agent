import typer
from rich.console import Console

from .cli_runner import CLIRunner, print_final_result

app = typer.Typer(help="TestCaseAgent CLI — 终端调试 ROCm 测试用例生成 Agent")
console = Console()


@app.command()
def run(
    prompt: str = typer.Argument(..., help="测试需求，自然语言"),
    provider: str = typer.Option("deepseek", help="模型提供商"),
    thread_id: str = typer.Option("cli-default", help="对话线程 ID (多轮用)"),
    hitl: bool = typer.Option(True, help="启用人工确认 (HITL)"),
):
    runner = CLIRunner(provider=provider, thread_id=thread_id, hitl=hitl)
    # ✅ 修复：run() 不再传 hitl，统一走 self._hitl_enabled
    result = runner.run(prompt)
    print_final_result(result)


@app.command()
def chat(
    provider: str = typer.Option("deepseek"),
    thread_id: str = typer.Option("cli-default"),
    hitl: bool = typer.Option(True, help="启用 HITL"),
):
    console.print("\n🧪 TestCaseAgent CLI — 输入 'exit' 退出\n", style="bold cyan")
    runner = CLIRunner(provider=provider, thread_id=thread_id, hitl=hitl)

    while True:
        try:
            prompt = input("\n🧪 > ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n👋 再见", style="dim")
            break
        if prompt.lower() in ("exit", "quit", "q"):
            break
        if not prompt:
            continue
        try:
            # ✅ 修复：同上
            result = runner.run(prompt)
            print_final_result(result)
        except Exception as exc:
            console.print(f"\n[bold red]❌ 执行失败: {exc}[/bold red]")


@app.command()
def status():
    console.print("🔍 环境检查：\n", style="bold cyan")

    # .env
    from pathlib import Path

    env_path = Path(".env")
    if env_path.exists():
        console.print("  ✅ .env 文件存在", style="green")
    else:
        console.print("  ❌ .env 文件不存在", style="red")

    # .venv
    venv_path = Path(".venv/bin/python")
    if venv_path.exists():
        console.print("  ✅ .venv 虚拟环境存在", style="green")
    else:
        console.print("  ❌ .venv 虚拟环境不存在", style="red")

    # 模型配置
    import os
    from dotenv import load_dotenv

    load_dotenv()
    provider = os.environ.get("TEST_CASE_AGENT_MODEL_PROVIDER", "未设置")
    console.print(f"  📋 Provider: {provider}")

    if provider == "deepseek":
        key = os.environ.get("DEEPSEEK_API_KEY", "")
        console.print(
            f"  🔑 DEEPSEEK_API_KEY: {'✅ ' + key[:8] + '...' if key else '❌ 未设置'}"
        )

    # Langfuse
    lf_host = (
        os.environ.get("LANGFUSE_HOST") or os.environ.get("LANGFUSE_BASE_URL") or ""
    )
    lf_pub = os.environ.get("LANGFUSE_PUBLIC_KEY", "")
    lf_sec = os.environ.get("LANGFUSE_SECRET_KEY", "")
    if lf_host and lf_pub and lf_sec:
        console.print(f"  ✅ Langfuse: {lf_host}", style="green")
    else:
        console.print(f"  ⚠️ Langfuse 未完全配置", style="yellow")

    # Docker 容器
    import subprocess

    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True
        )
        containers = result.stdout.strip().split("\n") if result.stdout.strip() else []
        if containers:
            console.print(f"  🐳 Docker 运行中: {', '.join(containers[:5])}")
        else:
            console.print("  ⚠️ Docker 无运行容器", style="yellow")
    except FileNotFoundError:
        console.print("  ❌ Docker 未安装", style="red")

    console.print(
        '\n[dim]如需调试 Agent，请执行: python -m src.agent.cli run "提示词"[/dim]'
    )


if __name__ == "__main__":
    app()