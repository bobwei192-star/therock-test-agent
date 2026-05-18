# step3_edges.py
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    test_code: str
    retry_count: int
    user_request: str

def planner(state: AgentState):
    return {"messages": [{"role": "assistant", "content": "📋 计划已制定"}]}

def generator(state: AgentState):
    retry = state.get("retry_count", 0)
    if retry == 0:
        code = "def test():  # 故意写错"
    else:
        code = "def test():\n    pass"
    return {
        "messages": [{"role": "assistant", "content": f"📝 第{retry+1}轮生成"}],
        "test_code": code,
        "retry_count": retry  # 保持当前值，validator 会负责加
    }

def validator(state: AgentState):
    import ast
    try:
        ast.parse(state["test_code"])
        return {"messages": [{"role": "assistant", "content": "✅ 通过"}]}
    except SyntaxError as e:
        return {
            "messages": [{"role": "assistant", "content": f"❌ 错误: {e}"}],
            "retry_count": state.get("retry_count", 0) + 1
        }

# ========== 路由函数：条件 Edge 的"交通警察" ==========
def router(state: AgentState):
    """
    这个函数决定 validator 之后去哪里。
    返回值必须是字符串，且要匹配 add_conditional_edges 里的字典 key。
    """
    retry = state.get("retry_count", 0)
    last_msg = str(state["messages"][-1]["content"])
    
    # 规则 1：重试超过 3 次，放弃
    if retry >= 3:
        print(f"[Router] 重试 {retry} 次，决定：放弃")
        return "give_up"
    
    # 规则 2：最新消息包含 ❌，说明语法错误，回 generator 修复
    if "❌" in last_msg:
        print(f"[Router] 检测到错误，决定：回到 generator 重试")
        return "retry"
    
    # 规则 3：通过
    print(f"[Router] 检查通过，决定：结束")
    return "done"

# ========== 建图 ==========
builder = StateGraph(AgentState)

# 注册节点（把函数"挂"到图上）
builder.add_node("planner", planner)
builder.add_node("generator", generator)
builder.add_node("validator", validator)

# 普通 Edge：固定流向
builder.add_edge(START, "planner")      # 图启动后，先去 planner
builder.add_edge("planner", "generator")  # planner 完，必定去 generator
builder.add_edge("generator", "validator")  # generator 完，必定去 validator

# 条件 Edge：validator 之后根据 router 返回值分流
builder.add_conditional_edges(
    "validator",           # 从 validator 节点出发
    router,                # 用 router 函数决定走哪条路
    {
        "retry": "generator",   # 如果 router 返回 "retry"，回到 generator
        "done": END,            # 如果 router 返回 "done"，流程结束
        "give_up": END          # 如果 router 返回 "give_up"，流程结束
    }
)

# 编译图（必须做这步才能运行）
graph = builder.compile()

# ========== 可视化（可选，需要安装额外包）==========
# 如果你装了 graphviz，可以取消下面注释生成图片
# from langgraph.graph import draw_mermaid_png
# with open("workflow.png", "wb") as f:
#     f.write(draw_mermaid_png(graph))

# ========== 运行 ==========
if __name__ == "__main__":
    result = graph.invoke({
        "messages": [{"role": "user", "content": "生成测试"}],
        "test_code": "",
        "retry_count": 0,
        "user_request": "生成测试"
    })
    
    print("\n=== 最终消息流 ===")
    for i, msg in enumerate(result["messages"], 1):
        print(f"{i}. {msg['content']}")
    
    print(f"\n=== 最终代码 ===\n{result['test_code']}")
    print(f"\n=== 最终重试次数 ===\n{result['retry_count']}")