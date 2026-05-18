# step4_memory.py
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver  # 核心：内存级记忆
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    test_code: str
    retry_count: int
    user_request: str

def planner(state: AgentState):
    return {"messages": [{"role": "assistant", "content": "📋 计划：执行用户请求"}]}

def generator(state: AgentState):
    return {
        "messages": [{"role": "assistant", "content": "📝 代码已生成"}],
        "test_code": "def test(): pass"
    }

# 建图
builder = StateGraph(AgentState)
builder.add_node("planner", planner)
builder.add_node("generator", generator)
builder.add_edge(START, "planner")
builder.add_edge("planner", "generator")
builder.add_edge("generator", END)

# ========== 核心：加 Memory ==========
checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# ========== 多轮对话演示 ==========
if __name__ == "__main__":
    # 同一个 thread_id = "session_001"，代表同一个用户的同一次会话
    config = {"configurable": {"thread_id": "session_001"}}
    
    # ========== 第一轮 ==========
    print(">>> 第一轮调用")
    result1 = graph.invoke(
        {
            "messages": [{"role": "user", "content": "生成 sgemm 测试"}],
            "test_code": "",
            "retry_count": 0,
            "user_request": "生成 sgemm 测试"
        },
        config=config
    )
    print(f"消息数: {len(result1['messages'])}")
    
    # ========== 第二轮（同一个 thread_id）==========
    print("\n>>> 第二轮调用（Agent 应该记得上一轮）")
    result2 = graph.invoke(
        {
            "messages": [{"role": "user", "content": "改成 2048x2048 的"}],
            # 注意：这里只传了 messages，其他字段不传！
            # 但 LangGraph 会自动从 Memory 中恢复之前的 test_code 和 retry_count
        },
        config=config
    )
    print(f"消息数: {len(result2['messages'])}")
    
    print("\n=== 完整消息历史（Agent 的记忆）===")
    for i, msg in enumerate(result2["messages"], 1):
        prefix = "👤" if msg["role"] == "user" else "🤖"
        print(f"{i}. {prefix} {msg['content']}")


