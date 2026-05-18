#!/usr/bin/env python3
import os
import ast
from typing import TypedDict, Annotated
import operator
import traceback

print(">>> 0. 开始导入...")
from deepagents.graph import create_deep_agent
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
print(">>> 导入完成")

print(">>> 1. 创建 agent...")
agent = create_deep_agent(
    model=ChatOpenAI(
        model="deepseek-chat",
        base_url="https://api.deepseek.com/v1",
        api_key="sk-8180e5ff3724496e904c229f6e8dd099",
        temperature=0.2
    )
)
print(">>> 2. agent 创建成功")

class State(TypedDict):
    messages: Annotated[list, operator.add]
    code: str
    retry: int

def coder(state: State):
    print(f">>> coder 被调用")
    result = agent.invoke({"messages": state["messages"]})
    last_msg = result["messages"][-1]
    reply = last_msg.content
    print(f">>> 收到回复: {reply[:80]}...")
    
    code = ""
    if "```python" in reply:
        code = reply.split("```python")[1].split("```")[0].strip()
    elif "```" in reply:
        code = reply.split("```")[1].split("```")[0].strip()
    
    return {"messages": [{"role": "assistant", "content": reply}], "code": code}

def checker(state: State):
    print(f">>> checker 被调用")
    try:
        ast.parse(state["code"])
        return {"messages": [{"role": "assistant", "content": "✅ 语法通过"}]}
    except SyntaxError as e:
        return {"messages": [{"role": "assistant", "content": f"❌ 语法错误: {e}"}], "retry": 1}

def router(state: State):
    retry = state.get("retry", 0)
    last = str(state["messages"][-1]["content"])
    print(f">>> router: retry={retry}, last={last[:30]}")
    if retry >= 3:
        return "giveup"
    if "✅" in last:
        return "ok"
    return "retry"

builder = StateGraph(State)
builder.add_node("coder", coder)
builder.add_node("checker", checker)
builder.add_edge(START, "coder")
builder.add_edge("coder", "checker")
builder.add_conditional_edges("checker", router, {"ok": END, "retry": "coder", "giveup": END})
graph = builder.compile()
print(">>> 3. 图编译完成")

print(">>> 4. 开始调用 graph.invoke...")
result = graph.invoke({
    "messages": [{"role": "user", "content": "生成一个 pytest 测试函数，测试 numpy 矩阵乘法 1024x1024"}],
    "code": "", "retry": 0
})

print(">>> 5. 调用完成")
for msg in result["messages"]:
    role = "👤" if msg["role"] == "user" else "🤖"
    print(f"{role} {msg['content'][:80]}...")
print(f"\n代码:\n{result['code'][:300]}")
print(f"重试: {result['retry']}")
