# step2_nodes.py
from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    test_code: str
    retry_count: int
    user_request: str

# ========== Node 1: 规划器（Planner）==========
def planner(state: AgentState):
    """
    职责：理解用户需求，制定执行计划。
    输入：读取 state["user_request"] 和 state["messages"]
    输出：追加一条计划消息到 messages
    """
    plan_msg = {
        "role": "assistant",
        "content": f"📋 计划：针对「{state['user_request']}」，我将生成 rocBLAS sgemm 测试代码"
    }
    return {"messages": [plan_msg]}

# ========== Node 2: 代码生成器（Generator）==========
def generator(state: AgentState):
    """
    职责：写 pytest 测试代码。
    技巧：通过 retry_count 判断是否是修复轮次。
    """
    retry = state.get("retry_count", 0)
    
    if retry == 0:
        # 第一轮：故意写错，演示后面的修复循环
        code = "def test_sgemm_1024():  # 注意：故意缺少右括号"
    else:
        # 第 2 轮及以后：生成正确的代码
        code = """def test_sgemm_1024():
    import rocblas
    import numpy as np
    
    A = np.random.rand(1024, 1024).astype(np.float32)
    B = np.random.rand(1024, 1024).astype(np.float32)
    C = rocblas.sgemm(A, B)
    assert C.shape == (1024, 1024)
"""
    
    gen_msg = {
        "role": "assistant",
        "content": f"📝 第 {retry + 1} 轮代码生成完成"
    }
    
    return {
        "messages": [gen_msg],
        "test_code": code
    }

# ========== Node 3: 验证器（Validator）==========
def validator(state: AgentState):
    """
    职责：用 Python AST 检查代码语法。
    如果语法错误：返回错误消息 + retry_count +1
    如果语法正确：返回通过消息
    """
    import ast
    code = state["test_code"]
    retry = state.get("retry_count", 0)
    
    try:
        ast.parse(code)
        # 语法通过
        return {
            "messages": [{"role": "assistant", "content": "✅ AST 语法检查通过"}]
        }
    except SyntaxError as e:
        # 语法失败，触发重试
        return {
            "messages": [{"role": "assistant", "content": f"❌ 语法错误: {e}"}],
            "retry_count": retry + 1
        }

# ========== 单独测试每个 Node ==========
if __name__ == "__main__":
    # 模拟初始状态
    state = {
        "messages": [{"role": "user", "content": "生成 sgemm 测试"}],
        "test_code": "",
        "retry_count": 0,
        "user_request": "生成 sgemm 测试"
    }
    
    print("=== 测试 Planner ===")
    update = planner(state)
    print("Planner 返回:", update)
    
    # 手动合并到 state（LangGraph 会自动做这件事）
    state["messages"] += update["messages"]
    
    print("\n=== 测试 Generator ===")
    update = generator(state)
    print("Generator 返回:", update)
    state["messages"] += update.get("messages", [])
    state["test_code"] = update["test_code"]
    
    print("\n=== 测试 Validator ===")
    update = validator(state)
    print("Validator 返回:", update)