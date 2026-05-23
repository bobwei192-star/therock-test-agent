"""Test Case Agent 工具集"""

import asyncio
from concurrent.futures import ThreadPoolExecutor

from langchain_core.tools import StructuredTool

# 原生工具
from .savetofile import save_to_file
from .readfile import read_file


# 模块级线程池，供“在事件循环内起新线程跑 asyncio”时使用
_MCP_TOOL_THREAD_POOL = ThreadPoolExecutor(
    max_workers=4, thread_name_prefix="mcp_sync_"
)


def _safe_async_run(coro):
    """安全运行一个异步协程，兼容“已有/没有事件循环”两种场景。"""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # 没有事件循环，直接用 asyncio.run
        return asyncio.run(coro)
    else:
        # 已在事件循环中（LangGraph 内部），必须在新线程里跑新事件循环
        future = _MCP_TOOL_THREAD_POOL.submit(asyncio.run, coro)
        return future.result()


def _load_hf_mcp_tools():
    """动态加载 HuggingFace 官方 MCP 工具，并包装为"调用时新建连接"的同步版本。"""
    import os

    try:
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client
        from langchain_mcp_adapters.tools import load_mcp_tools
    except ImportError:
        return []

    token = os.environ.get("HF_TOKEN")
    if not token:
        return []

    import subprocess

    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "mcp-remote", "https://huggingface.co/mcp"],
        env={"HF_TOKEN": token},
        stderr=subprocess.DEVNULL,
    )

    # ── 第 1 步：只连一次，获取工具定义（name / description / args_schema）──
    async def _fetch_definitions():
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await load_mcp_tools(session)

    try:
        original_tools = _safe_async_run(_fetch_definitions())
    except Exception:
        return []

    # ── 第 2 步：为每个工具创建“调用时重新建连”的同步包装器 ──
    wrapped_tools = []
    for orig in original_tools:
        if not isinstance(orig, StructuredTool):
            continue

        name = orig.name
        description = orig.description
        args_schema = orig.args_schema

        # 闭包工厂：捕获当前工具的 name / server_params
        def _make_sync_func(tool_name: str, params: StdioServerParameters):
            def sync_func(**kwargs):
                async def _execute():
                    async with stdio_client(params) as (read, write):
                        async with ClientSession(read, write) as session:
                            await session.initialize()
                            result = await session.call_tool(
                                tool_name, arguments=kwargs
                            )
                            print(
                                f"\n[MCP TOOL RESULT] {tool_name}({kwargs}) -> {result}"
                            )
                            # 把 MCP 结果转成字符串（模仿 langchain_mcp_adapters）
                            texts = []
                            for item in result.content:
                                if hasattr(item, "text"):
                                    texts.append(item.text)
                                else:
                                    texts.append(str(item))
                            return "\n".join(texts) if texts else str(result)

                return _safe_async_run(_execute())

            return sync_func

        new_tool = StructuredTool(
            name=name,
            description=description,
            args_schema=args_schema,
            func=_make_sync_func(name, server_params),
            coroutine=None,  # 不提供 async 版本，避免 LangGraph 误用
            return_direct=False,
        )
        wrapped_tools.append(new_tool)

    return wrapped_tools


TOOLS = [
    save_to_file,
    read_file,
    *_load_hf_mcp_tools(),
]

__all__ = [
    "TOOLS",
    "save_to_file",
    "read_file",
]
