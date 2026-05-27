"""执行计划节点 —— 生成详细的测试执行计划

根据 guide/02_架构与工具设计.md 设计：
- 输入：测试计划（case_plan）
- 输出：执行计划（execution_plan）

执行计划包括：
- 执行环境：本地/AIDevOps/Docker
- 前置条件检查
- 执行步骤
- 断言验证
- 清理动作
- Skip 条件
- 风险等级
"""

from typing import Any
from langgraph.runtime import Runtime

from ..state import AgentState, AgentContext
from ..memory_manager import MemoryManager
from .utils import _invoke_llm


def _build_execution_plan_prompt(case_plan: str, context: dict) -> str:
    """构建执行计划提示词"""
    return f"""你是一个测试执行计划专家。请根据测试计划生成详细的执行计划。

## 测试计划
{case_plan}

## 上下文信息
- 参考根目录: {context.get('reference_roots', [])}
- 检索到的文档数: {context.get('retrieved_count', 0)}

## 输出要求
请生成一个 YAML 格式的执行计划，包含以下字段：

```yaml
execution_plan:
  # 执行环境
  environment:
    type: "local" | "docker" | "aidevops"  # 执行环境类型
    image: "rocm/dev-ubuntu-22.04:6.0"     # Docker 镜像（如果 type=docker）
    timeout: 120                            # 超时时间（秒）
    
  # 前置条件检查
  preconditions:
    - name: "检查 ROCm 安装"
      command: "rocm-smi"
      expected: "exit_code == 0"
    - name: "检查 GPU 可见"
      command: "rocminfo | grep -c 'gfx'"
      expected: "output > 0"
      
  # 执行步骤
  steps:
    - name: "环境准备"
      action: "setup"
      commands:
        - "pip install pytest"
    - name: "执行测试"
      action: "run"
      commands:
        - "pytest test_generated.py -v"
      
  # 断言验证
  assertions:
    - name: "测试通过"
      condition: "exit_code == 0"
    - name: "无错误日志"
      condition: "stderr == ''"
      
  # 清理动作
  cleanup:
    - name: "删除临时文件"
      command: "rm -f /tmp/test_*.log"
      
  # Skip 条件
  skip_conditions:
    - name: "无 GPU"
      condition: "rocminfo 不可用"
      reason: "需要 GPU 环境"
      
  # 风险等级
  risk_level: "safe" | "network" | "heavy" | "system"
  
  # 人工确认
  human_confirm_required: false
```

请只输出 YAML 格式的执行计划，不要包含其他说明文字。
"""


def execution_planner(state: AgentState, runtime: Runtime[AgentContext], agent: Any) -> dict:
    """生成详细的测试执行计划。
    
    输入：
    - case_plan: 测试计划（来自 planner 节点）
    - context: RAG 检索上下文
    
    输出：
    - execution_plan: 结构化执行计划
    """
    memory = MemoryManager(runtime)
    
    print(f"\n{'=' * 60}")
    print("[execution_planner] 生成执行计划...")
    print(f"[execution_planner] case_plan 长度: {len(state.get('case_plan', ''))} 字符")
    
    # 检查是否有测试计划
    case_plan = state.get("case_plan", "")
    if not case_plan:
        print("[execution_planner] ⚠️ 没有测试计划，跳过执行计划生成")
        return {
            "execution_plan": {
                "status": "skipped",
                "reason": "没有测试计划",
            },
            "messages": [
                {"role": "assistant", "content": "跳过执行计划生成（没有测试计划）"}
            ],
        }
    
    # 检索相关记忆
    memories = memory.search("execution_plans", query=case_plan, limit=2)
    memory_hints = memory.format_hints(memories)
    
    # 构建提示词
    prompt = _build_execution_plan_prompt(
        case_plan=case_plan,
        context=state.get("context", {}),
    )
    
    # 调用 LLM 生成执行计划
    execution_plan_yaml = _invoke_llm(agent, prompt, node_name="execution_planner")
    
    # 解析 YAML（简单解析，提取关键字段）
    execution_plan = {
        "raw_yaml": execution_plan_yaml,
        "status": "generated",
    }
    
    # 尝试解析 YAML
    try:
        import yaml
        parsed = yaml.safe_load(execution_plan_yaml)
        if parsed and "execution_plan" in parsed:
            execution_plan.update(parsed["execution_plan"])
            execution_plan["status"] = "parsed"
            print(f"[execution_planner] ✅ YAML 解析成功")
    except Exception as e:
        print(f"[execution_planner] ⚠️ YAML 解析失败: {e}")
        execution_plan["parse_error"] = str(e)
    
    # 保存记忆
    memory_key = memory.put(
        namespace="execution_plans",
        key=f"plan_{hash(case_plan) % 10000}",
        data={
            "data": execution_plan_yaml,
            "case_plan_summary": case_plan[:200],
        },
    )
    
    print(f"[execution_planner] ✅ 执行计划已生成")
    print(f"[execution_planner] 记忆已保存: {memory_key}")
    print(f"{'=' * 60}\n")
    
    return {
        "execution_plan": execution_plan,
        "messages": [
            {"role": "assistant", "content": f"执行计划已生成。\n{execution_plan_yaml[:500]}"}
        ],
    }
