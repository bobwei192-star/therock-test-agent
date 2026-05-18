#!/usr/bin/env python3
import os
import ast
from typing import TypedDict, Annotated
import operator

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END

os.environ.setdefault("OPENAI_API_KEY", "sk-8180e5ff3724496e904c229f6e8dd099")
os.environ.setdefault("OPENAI_BASE_URL", "https://api.deepseek.com/v1")

llm = ChatOpenAI(model="deepseek-chat", temperature=0.2)

class State(TypedDict):
    messages: Annotated[list, operator.add]
    code: str
    retry: int

def coder(state: State):
    lc_msgs = []
    for m in state["messages"]:
        if m["role"] == "user":
            lc_msgs.append(HumanMessage(content=m["content"]))
        else:
            lc_msgs.append(AIMessage(content=m["content"]))
    if state["retry"] > 0:
        lc_msgs.append(HumanMessage(content=(
            f"上次代码有语法错误，请修复后重新输出完整代码块。\n"
            f"错误：{state.get('last_error', '未知')}"
        )))
    response = llm.invoke(lc_msgs)
    content = response.content
    code = ""
    if "```python" in content:
        code = content.split("```python")[1].split("```")[0].strip()
    elif "```" in content:
        code = content.split("```")[1].split("```")[0].strip()
    return {"messages": [{"role": "assistant", "content": content}], "code": code}

def checker(state: State):
    try:
        ast.parse(state["code"])
        return {"messages": [{"role": "assistant", "content": "✅ 语法通过"}]}
    except SyntaxError as e:
        return {"messages": [{"role": "assistant", "content": f"❌ 语法错误: {e}"}], "retry": 1, "last_error": str(e)}

def router(state: State):
    if state["retry"] >= 3:
        return "giveup"
    if "✅" in str(state["messages"][-1]["content"]):
        return "ok"
    return "retry"

builder = StateGraph(State)
builder.add_node("coder", coder)
builder.add_node("checker", checker)
builder.add_edge(START, "coder")
builder.add_edge("coder", "checker")
builder.add_conditional_edges("checker", router, {"ok": END, "retry": "coder", "giveup": END})
graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke({
        "messages": [{"role": "user", "content": "生成一个 pytest 测试函数，测试 numpy 矩阵乘法 1024x1024"}],
        "code": "", "retry": 0
    })
    for msg in result["messages"]:
        role = "👤" if msg["role"] == "user" else "🤖"
        print(f"{role} {msg['content'][:100]}...")
    print(f"\n=== 最终代码 ===\n{result['code'][:500]}")
    print(f"\n重试次数: {result['retry']}")