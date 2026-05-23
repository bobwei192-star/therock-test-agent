import uuid
from typing import Any
from langgraph.runtime import Runtime
from ..state import AgentState, AgentContext
from .utils import _invoke_llm, _last_user_message, _memory_namespace


def requirement_parser(
    state: AgentState, runtime: Runtime[AgentContext], agent: Any
) -> dict:
    raw_requirement = state.get("requirement") or _last_user_message(state)

    prompt = (
            "你是 ROCm 测试需求解析专家。首先识别用户意图，然后输出结构化的测试规格（Test Spec），"
            "供下游节点做执行编排和代码生成。不要输出执行步骤、时间安排或工程部署细节。\n\n"
            f"用户需求: {raw_requirement}\n\n"
            "## 意图识别（必选其一）\n"
            "分析用户输入，判断属于以下哪种意图：\n"
            "- GENERATE: 从零创建新测试用例\n"
            "- APPEND: 在现有测试文件上追加新测试函数/场景\n"
            "- UPDATE: 修复已有测试的错误或适配新版本\n"
            "- REFACTOR: 优化代码结构，不改测试逻辑与断言目标\n"
            "- EXECUTE_EXTERNAL: 下载/编译/运行第三方测试套件（如 igt-gpu-tools）\n"
            "- DIAGNOSE: 分析测试失败日志，定位根因\n"
            "- COVERAGE: 分析现有测试集的等价类/边界值覆盖度\n"
            "- PROBE: 探测当前 ROCm 环境能力，输出报告\n\n"
            "意图: <GENERATE|APPEND|UPDATE|REFACTOR|EXECUTE_EXTERNAL|DIAGNOSE|COVERAGE|PROBE>\n\n"
            "## 测试规格输出（仅 GENERATE/APPEND/UPDATE/REFACTOR 意图需完整输出以下章节；"
            "其他意图按对应简化模板输出）\n"
            "1. 测试目标: <一句话描述被测功能>\n"
            "2. ROCm 组件: <命令/库名，如 rocm-smi/rocminfo/rocBLAS/kfd>\n"
            "3. 测试点清单:\n"
            "   - <测试点1>: <等价类:有效/无效/边界> | <AAAC简要:Arrange做什么→Act执行什么→Assert验证什么→Cleanup是否需清理>\n"
            "   - <测试点2>: ...\n"
            "4. 等价类划分:\n"
            "   - 有效等价类: <正常输入/正常环境/正常输出场景>\n"
            "   - 无效等价类: <命令缺失/无GPU/权限不足/异常参数，预期 pytest.skip 或非零返回码>\n"
            "   - 边界等价类: <数值边界/单多GPU边界/空输出边界>\n"
            "5. AAAC 四阶段设计原则:\n"
            "   - Arrange: <环境检查命令存在性、数据准备、fixture 依赖初始化>\n"
            "   - Act: <执行被测命令或调用被测函数的具体方式>\n"
            "   - Assert: <验证返回码、输出关键词存在性、数值范围，不写精确字符串或具体数值>\n"
            "   - Cleanup: <副作用清理动作；只读操作写'无'>\n"
            "6. 断言策略:\n"
            "   - 应断言: <返回码为0、数值在合理范围、输出包含关键词、失败时暴露诊断信息>\n"
            "   - 禁断言: <精确字符串匹配、具体数值等于、输出长度固定、mock/fake 数据>\n"
            "   - 诊断要求: <assert 失败时必须输出 returncode、stderr[:500]、stdout[:500]>\n"
            "7. 降级条件: <命令不在PATH时skip、无AMD GPU时skip、ROCm版本不兼容时skip>\n"
            "8. Fixture 需求: <命令执行器fixture(scope=module)/GPU计数fixture/临时文件fixture/无>\n"
            "9. 历史代码约束（仅APPEND/UPDATE/REFACTOR）: <必须保留的函数、禁止修改的断言目标、允许调整的结构>\n"
        )

    llm_result = _invoke_llm(agent, prompt, node_name="requirement_parser")

    if hasattr(llm_result, "content"):
        content = llm_result.content
    else:
        content = str(llm_result)

    ns = _memory_namespace(runtime, "requirements")
    memory_key = f"req_{uuid.uuid4().hex[:8]}"
    runtime.store.put(
        ns,
        memory_key,
        {
            "raw": raw_requirement,
            "parsed": content,
        },
    )

    msg = {"role": "assistant", "content": content}

    return {
        "requirement": raw_requirement,
        "parsed_requirement": content,
        "messages": [msg],
    }
