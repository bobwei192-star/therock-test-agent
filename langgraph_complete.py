#!/usr/bin/env python3
"""
LangGraph 完整演示：Plan → Generate → Validate → (Retry or End)
带 Memory，支持多轮对话。
"""
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
import operator

# ==================== State ====================
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]   # 追加模式：历史消息
    test_code: str                            # 当前代码（覆盖模式）
    retry_count: int                          # 重试次数（覆盖模式）
    user_request: str                         # 原始需求（覆盖模式）

# ==================== Nodes ====================
def planner(state: AgentState):
    """规划节点：理解需求并制定计划"""
    return {
        "messages": [{
            "role": "assistant",
            "content": f"📋 计划：为「{state['user_request']}」生成 rocBLAS sgemm 测试"
        }]
    }

def generator(state: AgentState):
    """生成节点：写 pytest 代码"""
    retry = state.get("retry_count", 0)
    
    # 第一轮故意写错，演示修复循环
    if retry == 0:
        code = "def test_sgemm_1024():  # 故意缺少右括号，演示重试"
    else:
        code = """import pytest
import numpy as np

def test_sgemm_1024():
    # 1024x1024 单精度矩阵乘测试
    A = np.random.rand(1024, 1024).astype(np.float32)
    B = np.random.rand(1024, 1024).astype(np.float32)
    # 假设 rocblas.sgemm 已导入
    assert A.shape == (1024, 1024)
"""
    
    return {
        "messages": [{"role": "assistant", "content": f"📝 第 {retry + 1} 轮代码生成"}],
        "test_code": code
    }

def validator(state: AgentState):
    """验证节点：AST 语法检查"""
    import ast
    try:
        ast.parse(state["test_code"])
        return {"messages": [{"role": "assistant", "content": "✅ AST 语法检查通过，准备保存"}]}
    except SyntaxError as e:
        return {
            "messages": [{"role": "assistant", "content": f"❌ 语法错误: {e}"}],
            "retry_count": state.get("retry_count", 0) + 1
        }

# ==================== Router ====================
def router(state: AgentState):
    """条件路由：决定 validator 之后去哪"""
    retry = state.get("retry_count", 0)
    last_msg = str(state["messages"][-1]["content"])
    
    if retry >= 3:
        return "give_up"
    if "❌" in last_msg:
        return "retry"
    return "done"

# ==================== Build Graph ====================
builder = StateGraph(AgentState)
builder.add_node("planner", planner)
builder.add_node("generator", generator)
builder.add_node("validator", validator)

builder.add_edge(START, "planner")
builder.add_edge("planner", "generator")
builder.add_edge("generator", "validator")
builder.add_conditional_edges("validator", router, {
    "retry": "generator",
    "done": END,
    "give_up": END
})

# 加 Memory
checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# ==================== Run ====================
if __name__ == "__main__":
    config = {"configurable": {"thread_id": "demo_session"}}
    
    print("=" * 50)
    print("第一次调用：生成 sgemm 测试")
    print("=" * 50)
    result = graph.invoke({
        "messages": [{"role": "user", "content": "生成 sgemm 测试"}],
        "test_code": "",
        "retry_count": 0,
        "user_request": "生成 sgemm 测试"
    }, config=config)
    
    for msg in result["messages"]:
        role = "👤" if msg["role"] == "user" else "🤖"
        print(f"{role} {msg['content']}")
    
    print(f"\n最终代码:\n{result['test_code']}")
    print(f"重试次数: {result['retry_count']}")
    
    # 演示 Memory：第二次调用，Agent 记得上下文
    print("\n" + "=" * 50)
    print("第二次调用：同一个 thread_id，Agent 有记忆")
    print("=" * 50)
    result2 = graph.invoke({
        "messages": [{"role": "user", "content": "改成 2048 维度的"}]
    }, config=config)
    
    print(f"总消息数（含记忆）: {len(result2['messages'])}")