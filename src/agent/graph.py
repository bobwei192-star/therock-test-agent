# graph.py
from functools import partial
from langgraph.graph import StateGraph, START, END
from .tools import TOOLS

from .state import AgentState, AgentContext
from .nodes import (
    context_retriever,
    generator,
    planner,
    requirement_parser,
)


DEFAULT_SYSTEM_PROMPT = (
    "你是一个测试用例生成专家。"
    "你会先规划测试用例，再生成最小可执行的测试草案。"
    "当涉及外部资源（如 HuggingFace 模型、GitHub 仓库, Docker 镜像，Artifactory ）时，你必须先调用相应工具确认资源存在及最新状态，禁止凭记忆假设"
)


def build_graph(
    model=None,
    tools=None,
    checkpointer=None,
    store=None,
    system_prompt: str | None = None,
):
    agent = None
    if model is not None:
        from deepagents import create_deep_agent

        all_tools = tools if tools is not None else TOOLS
        agent = create_deep_agent(
            model=model,
            tools=all_tools,
            system_prompt=system_prompt or DEFAULT_SYSTEM_PROMPT,
        )

    requirement_parser_with_agent = partial(requirement_parser, agent=agent)
    planner_with_agent = partial(planner, agent=agent)
    generator_with_model = partial(generator, model=model)

    builder = StateGraph(AgentState, context_schema=AgentContext)

    builder.add_node("requirement_parser", requirement_parser_with_agent)
    builder.add_node("context_retriever", context_retriever)
    builder.add_node("planner", planner_with_agent)
    builder.add_node("generator", generator_with_model)


    builder.add_edge(START, "requirement_parser")
    builder.add_edge("requirement_parser", "context_retriever")
    builder.add_edge("context_retriever", "planner")
    builder.add_edge("planner", "generator")
    builder.add_edge("generator", END)

    compile_kwargs = {}
    if checkpointer is not None:
        compile_kwargs["checkpointer"] = checkpointer
    if store is not None:
        compile_kwargs["store"] = store

    return builder.compile(**compile_kwargs)
