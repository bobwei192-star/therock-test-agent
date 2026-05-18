#!/usr/bin/env python3
import os
import ast
from typing import TypedDict, Annotated
import operator
import traceback

from deepagents.graph import create_deep_agent
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

print(">>> 1. 开始创建 agent...")
try:
    agent = create_deep_agent(
        model=ChatOpenAI(
            model="deepseek-chat",
            base_url="https://api.deepseek.com/v1",
            api_key="sk-8180e5ff3724496e904c229f6e8dd099",
            temperature=0.2
        )
    )
    print(">>> 2. agent 创建成功")
except Exception as e:
    print(f">>> agent 创建失败: {e}")
    traceback.print_exc()
    exit(1)

class State(TypedDict):
    messages: Annotated[list, operator.add]
    code: str
    retry: int

def coder(state: State):
    print(f">>> 3. coder 节点被调用，当前 retry={state.get('retry', 0)}")
    print(f">>>    messages 数量: {len(state['messages'])}")
    try:
        print(">>>    正在调用 agent.invoke...")
        result = agent.invoke({"messages": state["messages"]})
        print(f">>>    agent.invoke 返回，messages 数量: {len(result['messages'])}")
        last_msg = result["messages"][-1]
        reply = last_msg.content
        print(f">>>    回复前100字: {reply[:100]}")
        
        code = ""
        if "```python" in reply:
            code = reply.split("```python")[1].split("```")[0].strip()
        elif "```" in reply:
            code = reply.split("```")[1].split("```")[0].strip()
        print(f">>>    提取代码长度: {len(code)}")
        
        return {"messages": [{"role": "assistant", "content": reply}], "code": code}
    except Exception as e:
        print(f">>> coder 出错: {e}")
        traceback.print_exc()
        raise

def checker(state: State):
    print(f">>> 4. checker 节点被调用")
    try:
        ast.parse(state["code"])
        print(">>>    AST 检查通过")
        return {"messages": [{"role": "assistant", "content": "✅ 语法通过"}]}
    except SyntaxError as e:
        print(f">>>    AST 检查失败: {e}")
        return {"messages": [{"role": "assistant", "content": f"❌ 语法错误: {e}"}], "retry": 1, "last_error": str(e)}

def router(state: State):
    retry = state.get("retry", 0)
    last = str(state["messages"][-1]["content"])
    print(f">>> 5. router 被调用，retry={retry}, last_msg={last[:50]}")
    if retry >= 3:
        return "giveup"
    if "✅" in last:
        return "ok"
    return "retry"

print(">>> 6. 开始构建图...")
builder = StateGraph(State)
builder.add_node("coder", coder)
builder.add_node("checker", checker)
builder.add_edge(START, "coder")
builder.add_edge("coder", "checker")
builder.add_conditional_edges("checker", router, {"ok": END, "retry": "coder", "giveup": END})
graph = builder.compile()
print(">>> 7. 图编译完成，开始调用...")

try:
    result = graph.invoke({
        "messages": [{"role": "user", "content": "生成一个 pytest 测试函数，测试 numpy 矩阵乘法 1024x1024"}],
        "code": "", "retry": 0
    })
    print(">>> 8. graph.invoke 返回")
    for msg in result["messages"]:
        role = "👤" if msg["role"] == "user" else "🤖"
        print(f"{role} {msg['content'][:100]}...")
    print(f"\n=== 最终代码 ===\n{result['code'][:500]}")
    print(f"\n重试次数: {result['retry']}")
except Exception as e:
    print(f">>> graph.invoke 失败: {e}")
    traceback.print_exc()