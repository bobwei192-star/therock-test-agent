"""长期记忆管理模块 - 封装 LangGraph Store 的读写操作。

本文件提供 MemoryManager 类，作为各节点与 LangGraph Store（长期记忆存储）
之间的中间层，统一管理记忆的命名空间构建、搜索、写入和格式化。

核心职责：
- 按 user_id / project_id 隔离不同用户/项目的记忆命名空间
- 提供语义搜索接口（基于 Store 的向量检索能力）
- 将记忆格式化为 LLM 提示词片段，注入到各节点的 prompt 中
- 封装常用的记忆写入场景（保存计划、保存生成结果、保存需求解析）

调用的框架/库：
- langgraph.runtime.Runtime: LangGraph 运行时，提供 store 访问入口
- langgraph.store: 底层存储后端（InMemoryStore 或持久化 Store）
- uuid: 生成唯一记忆 key
"""

import uuid
from typing import Any, Optional, List, Dict
from langgraph.runtime import Runtime
from .state import AgentContext


class MemoryManager:
    """LangGraph Store 记忆管理器，简化节点中的记忆读写。

    使用方式：
        在节点函数中通过 runtime 参数创建实例：
        >>> memory = MemoryManager(runtime)
        >>> memories = memory.search("plans", query="rocm-smi")
        >>> memory.save_plan(requirement="...", case_plan="...")
    """

    def __init__(self, runtime: Runtime[AgentContext]):
        """初始化记忆管理器。

        参数:
            runtime: LangGraph 运行时实例，包含 store 和 context
        """
        self._runtime = runtime
        self._user_id = runtime.context.user_id
        self._project_id = runtime.context.project_id

    def _build_namespace(self, suffix: str) -> tuple:
        """构建记忆命名空间元组。

        命名空间结构: (user_id, [project_id,] suffix)
        - 有 project_id 时: ("user1", "proj_a", "plans")
        - 无 project_id 时: ("user1", "plans")

        参数:
            suffix: 命名空间后缀，如 "plans"、"generations"、"requirements"

        返回:
            命名空间元组，用于 store.search / store.put
        """
        parts = [self._user_id]
        if self._project_id:
            parts.append(self._project_id)
        parts.append(suffix)
        return tuple(parts)

    def search(self, namespace: str, query: str, limit: int = 3) -> List[Any]:
        """语义搜索指定命名空间的记忆。

        参数:
            namespace: 命名空间后缀（如 "plans"、"generations"）
            query: 搜索查询文本（用于语义匹配）
            limit: 最多返回的记忆条数

        返回:
            匹配的记忆对象列表，每个对象有 .key 和 .value 属性
        """
        ns = self._build_namespace(namespace)
        return self._runtime.store.search(ns, query=query, limit=limit)

    def put(self, namespace: str, data: Dict[str, Any], key: Optional[str] = None) -> str:
        """写入一条记忆到指定命名空间。

        参数:
            namespace: 命名空间后缀
            data: 要存储的记忆数据字典
            key: 可选的自定义 key；未提供时自动生成（格式: 前缀_随机8位hex）

        返回:
            实际使用的记忆 key
        """
        ns = self._build_namespace(namespace)
        memory_key = key or f"{namespace[:3]}_{uuid.uuid4().hex[:8]}"
        self._runtime.store.put(ns, memory_key, data)
        return memory_key

    def format_hints(self, memories: List[Any]) -> str:
        """将记忆列表格式化为可注入 prompt 的文本片段。

        输出格式：
            ## 历史相关记忆
            - 需求: xxx... | 计划摘要: yyy...
            - 为需求 [zzz...] 最终保留 1200 字符代码

        参数:
            memories: search() 返回的记忆对象列表

        返回:
            格式化后的 Markdown 文本；无记忆时返回空字符串
        """
        if not memories:
            return ""
        lines = ["\n## 历史相关记忆"]
        for m in memories:
            data = m.value.get("data", "") if hasattr(m, "value") else str(m)
            lines.append(f"- {data}")
        return "\n".join(lines)

    def save_plan(self, requirement: str, case_plan: str) -> str:
        """保存测试计划到 "plans" 命名空间。

        参数:
            requirement: 用户原始需求文本
            case_plan: 生成的测试计划全文

        返回:
            写入的记忆 key
        """
        memory_value = {
            "data": f"需求: {requirement[:120]}... | 计划摘要: {case_plan[:200]}...",
            "requirement": requirement,
            "full_plan": case_plan,
        }
        return self.put("plans", memory_value)

    def save_generation(self, requirement: str, code: str, saved_filepath: Optional[str] = None) -> str:
        """保存代码生成结果到 "generations" 命名空间。

        参数:
            requirement: 对应的用户需求
            code: 生成的代码全文
            saved_filepath: 代码保存的文件路径（可选）

        返回:
            写入的记忆 key
        """
        memory_value = {
            "data": f"为需求 [{requirement[:80]}...] 最终保留 {len(code)} 字符代码",
            "code_preview": code[:500] if code else "EXTRACTION_FAILED",
            "saved_filepath": saved_filepath,
        }
        return self.put("generations", memory_value)

    def save_requirement(self, raw_requirement: str, parsed_requirement: str) -> str:
        """保存需求解析结果到 "requirements" 命名空间。

        参数:
            raw_requirement: 用户原始输入
            parsed_requirement: LLM 解析后的结构化需求

        返回:
            写入的记忆 key
        """
        memory_value = {
            "data": f"原始需求: {raw_requirement[:120]}...",
            "raw_requirement": raw_requirement,
            "parsed_requirement": parsed_requirement,
        }
        return self.put("requirements", memory_value)