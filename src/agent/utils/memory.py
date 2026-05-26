"""记忆管理工具模块 - 提供基础的内存存储和记忆管理功能。

本模块提供:
- InMemoryStore: 简单的内存文档存储实现
- MemoryManager: 高层记忆管理器，封装存储操作
"""

from typing import Any, List, Dict, Optional
from langchain_core.documents import Document


class InMemoryStore:
    """简单的内存文档存储实现。
    
    提供基本的文档 CRUD 操作和搜索功能。
    """

    def __init__(self):
        """初始化内存存储。"""
        self._documents = {}

    def upsert(self, documents: List[Document]) -> List[str]:
        """插入或更新文档。
        
        参数:
            documents: 文档列表，每个文档应有 id 属性
            
        返回:
            插入的文档 ID 列表
        """
        ids = []
        for doc in documents:
            doc_id = getattr(doc, 'id', None) or getattr(doc, 'metadata', {}).get('id')
            if not doc_id:
                import uuid
                doc_id = str(uuid.uuid4())
            self._documents[doc_id] = doc
            ids.append(doc_id)
        return ids

    def get(self, ids: List[str]) -> List[Document]:
        """通过ID获取文档。
        
        参数:
            ids: 要获取的文档 ID 列表
            
        返回:
            文档列表
        """
        return [self._documents.get(doc_id) for doc_id in ids if doc_id in self._documents]

    def search(self, query: str, limit: int = 10) -> List[Document]:
        """简单搜索文档。
        
        参数:
            query: 搜索查询文本
            limit: 返回结果数量限制
            
        返回:
            匹配的文档列表
        """
        results = []
        for doc in self._documents.values():
            content = getattr(doc, 'page_content', '')
            if query.lower() in content.lower():
                results.append(doc)
                if len(results) >= limit:
                    break
        return results


class MemoryManager:
    """记忆管理器 - 封装记忆的保存和检索操作。"""

    def __init__(self, store=None):
        """初始化记忆管理器。
        
        参数:
            store: 存储后端，默认为 InMemoryStore
        """
        self._store = store or InMemoryStore()

    def save_memory(self, key: str, memory_type: str, content: str, metadata: Dict = None) -> str:
        """保存一条记忆。
        
        参数:
            key: 记忆的唯一标识
            memory_type: 记忆类型
            content: 记忆内容
            metadata: 附加元数据
            
        返回:
            保存的文档 ID
        """
        metadata = metadata or {}
        doc = Document(
            page_content=content,
            id=key,
            metadata={**metadata, 'memory_type': memory_type}
        )
        results = self._store.upsert([doc])
        return results[0] if results else None

    def get_relevant_memories(self, query: str, memory_types: List[str] = None, limit: int = 5) -> List[Any]:
        """获取相关记忆。
        
        参数:
            query: 搜索查询
            memory_types: 记忆类型过滤列表
            limit: 返回数量限制
            
        返回:
            匹配的记忆列表
        """
        if not query:
            return []
        
        results = self._store.search(query, limit=limit)
        
        if memory_types:
            results = [
                r for r in results 
                if r.metadata.get('memory_type') in memory_types
            ]
        
        return results[:limit]
