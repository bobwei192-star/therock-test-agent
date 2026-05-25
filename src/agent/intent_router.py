"""意图路由模块 - 根据用户输入判断意图（规则匹配）

根据 guide/09_promot优化.md 设计：
- 支持 9 种意图：GENERATE, APPEND, UPDATE, REFACTOR, EXECUTE_EXTERNAL, DIAGNOSE, COVERAGE, PROBE, ENV_BUILD
- 规则匹配优先 ENV_BUILD（关键词匹配）
- 无需 LLM 判断，纯规则匹配，低延迟
"""

from typing import Literal

IntentType = Literal[
    "GENERATE",
    "APPEND",
    "UPDATE",
    "REFACTOR",
    "EXECUTE_EXTERNAL",
    "DIAGNOSE",
    "COVERAGE",
    "PROBE",
    "ENV_BUILD",
]


def route_intent(raw_requirement: str) -> IntentType:
    """意图路由：规则匹配 9 选 1

    Args:
        raw_requirement: 用户原始输入需求

    Returns:
        匹配的意图类型
    """
    text = raw_requirement.lower()

    # ENV_BUILD 优先级最高（必须放在最前面）
    env_keywords = [
        "docker", "镜像", "image", "编译环境", "build image",
        "rocm+pytorch", "llvm编译", "基础镜像", "dockerfile",
        "环境准备", "容器化", "镜像构建", "构建镜像"
    ]
    if any(k in text for k in env_keywords):
        return "ENV_BUILD"

    # 修改类
    if any(k in text for k in ["修复", "报错", "失败", "error", "fix"]):
        return "REFACTOR" if "重构" in text else "UPDATE"

    # 创建类（追加）
    if any(k in text for k in ["追加", "添加", "补充", "append", "add"]):
        return "APPEND"

    # 查询诊断类
    if any(k in text for k in ["诊断", "分析日志", "为什么失败", "diagnose"]):
        return "DIAGNOSE"
    if any(k in text for k in ["覆盖度", "覆盖率", "coverage"]):
        return "COVERAGE"
    if any(k in text for k in ["探测", "环境", "probe", "环境能力"]):
        return "PROBE"

    # 外部执行类
    if any(k in text for k in ["igt", "外部套件", "第三方", "external"]):
        return "EXECUTE_EXTERNAL"

    # 默认：创建新测试
    return "GENERATE"


def get_intent_cluster(intent: IntentType) -> Literal["create", "modify", "query", "external", "build"]:
    """获取意图所属聚类

    Args:
        intent: 意图类型

    Returns:
        聚类名称：create/modify/query/external/build
    """
    cluster_map: dict[IntentType, Literal["create", "modify", "query", "external", "build"]] = {
        "GENERATE": "create",
        "APPEND": "create",
        "UPDATE": "modify",
        "REFACTOR": "modify",
        "DIAGNOSE": "query",
        "COVERAGE": "query",
        "PROBE": "query",
        "EXECUTE_EXTERNAL": "external",
        "ENV_BUILD": "build",
    }
    return cluster_map[intent]


def get_template_name(intent: IntentType) -> str:
    """获取意图对应的提示词模板名称

    Args:
        intent: 意图类型

    Returns:
        模板名称：create_intent/update_intent/query_intent/external_intent/build_intent
    """
    template_map: dict[IntentType, str] = {
        "GENERATE": "create_intent",
        "APPEND": "create_intent",
        "UPDATE": "update_intent",
        "REFACTOR": "update_intent",
        "DIAGNOSE": "query_intent",
        "COVERAGE": "query_intent",
        "PROBE": "query_intent",
        "EXECUTE_EXTERNAL": "external_intent",
        "ENV_BUILD": "build_intent",
    }
    return template_map[intent]