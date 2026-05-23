"""RAG 上下文检索节点 —— 官方 LangChain 模式（InMemoryVectorStore + 模块级创建）

与官方 guide/06_官方rag.md 对齐：
- 向量库在模块级创建（非 lazy global）
- 从 chroma_db 一次性加载到内存后，Chroma client 即关闭
- 所有查询走 InMemoryVectorStore，不存在连接断开问题
"""

import os
from pathlib import Path

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from langchain_core.documents import Document  # noqa: E402
from langchain_core.vectorstores import InMemoryVectorStore  # noqa: E402
from langchain_huggingface import HuggingFaceEmbeddings  # noqa: E402
from ..state import AgentState  # noqa: E402

_CHROMA_DIR = Path("./chroma_db")

_embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)

_vectorstore: InMemoryVectorStore | None = None
_load_error: str | None = None


def _init_vectorstore() -> InMemoryVectorStore:
    """模块级初始化：从 chroma_db 一次性加载到 InMemoryVectorStore。

    之后所有查询走内存，不再依赖 Chroma client 连接。
    """
    global _vectorstore, _load_error

    if _vectorstore is not None:
        return _vectorstore

    vs = InMemoryVectorStore(_embeddings)

    if not _CHROMA_DIR.exists():
        _load_error = f"向量库 {_CHROMA_DIR} 不存在。请先运行: python index_docs.py"
        print(f"[RAG] ⚠️ {_load_error}")
        _vectorstore = vs
        return vs

    try:
        import chromadb
        from langchain_chroma import Chroma

        client = chromadb.PersistentClient(path=str(_CHROMA_DIR))
        chroma_vs = Chroma(
            client=client, collection_name="docs",
            embedding_function=_embeddings,
        )
        collection = chroma_vs._collection
        count = collection.count()
        print(f"[RAG] 从 chroma_db 读取 {count} 个文本块...")

        if count > 0:
            result = collection.get(include=["documents", "metadatas"])
            docs: list[Document] = []
            for i in range(count):
                doc_id = result["ids"][i]
                page_content = result["documents"][i] or ""
                metadata = result["metadatas"][i] or {}
                metadata["id"] = doc_id
                docs.append(Document(page_content=page_content, metadata=metadata))
            vs.add_documents(docs)
            print(f"[RAG] ✅ 已加载到 InMemoryVectorStore，共 {count} 个文本块")
        else:
            _load_error = "chroma_db 为空，请先运行 python index_docs.py"
            print(f"[RAG] ⚠️ {_load_error}")

        del chroma_vs
        del client
        import gc
        gc.collect()
    except Exception as exc:
        _load_error = f"{type(exc).__name__}: {exc}"
        print(f"[RAG] ❌ 加载 chroma_db 失败: {_load_error}")

    _vectorstore = vs
    return vs


def _get_requirement(state: AgentState) -> str:
    req = state.get("requirement", "")
    if req and req.strip():
        return req.strip()

    for msg in reversed(state.get("messages", [])):
        content = ""
        if isinstance(msg, dict) and msg.get("role") == "user":
            content = msg.get("content", "")
        elif hasattr(msg, "type") and msg.type == "human":
            content = getattr(msg, "content", "")
        if content and content.strip():
            return content.strip()
    return ""


def context_retriever(state: AgentState) -> dict:
    print(f"\n{'='*60}")
    print("[RAG DIAGNOSTIC] context_retriever 开始执行")

    requirement = _get_requirement(state)
    print(f"[RAG] 提取到的 requirement: '{requirement[:80]}...' (长度: {len(requirement)})")

    docs: list = []
    rag_error: str | None = None

    try:
        store = _init_vectorstore()
        print(f"[RAG] 正在执行 similarity_search(query='{requirement[:60]}...', k=4)")
        docs = store.similarity_search(requirement, k=4)
        if docs:
            print(f"[RAG] 检索完成，召回 {len(docs)} 条结果")
            for i, d in enumerate(docs):
                src = d.metadata.get("source", "unknown")
                preview = d.page_content[:60].replace('\n', ' ')
                print(f"       [{i+1}] 来源: {src} | 内容: {preview}...")
        else:
            rag_error = _load_error or "检索结果为空"
    except Exception as exc:
        rag_error = f"{type(exc).__name__}: {exc}"
        print(f"[RAG] ❌ 意外异常: {rag_error}")
        import traceback
        traceback.print_exc()

    if docs:
        retrieved_text = "\n\n---\n\n".join([
            f"【来源: {d.metadata.get('source', 'unknown')}】\n{d.page_content}"
            for d in docs
        ])
        context = {
            "phase": "rag_enabled",
            "requirement": requirement,
            "retrieved_knowledge": retrieved_text,
            "retrieved_sources": [d.metadata.get("source") for d in docs],
            "retrieved_count": len(docs),
            "reference_roots": ["/home/zx/CICD/test_case", "/home/zx/CICD/rocm-on-radeon"],
            "case_format": "test_case/suites/<suite>/test_<name>.sh or pytest draft",
            "execution_mode": "dry_run_only",
        }
        assistant_msg = f"已从知识库检索到 {len(docs)} 篇相关文档。"
        print(f"[RAG] ✅ 进入 RAG 模式，retrieved_knowledge 长度: {len(retrieved_text)} 字符")
    else:
        context = {
            "phase": "phase_one_placeholder",
            "requirement": requirement,
            "reference_roots": ["/home/zx/CICD/test_case", "/home/zx/CICD/rocm-on-radeon"],
            "case_format": "test_case/suites/<suite>/test_<name>.sh or pytest draft",
            "execution_mode": "dry_run_only",
            "todo": "RAG 未检索到文档。",
        }
        if rag_error:
            context["rag_error"] = rag_error
        assistant_msg = f"知识库未就绪（{rag_error}），使用默认上下文。" if rag_error else "未检索到相关文档，使用默认上下文。"
        print(f"[RAG] ⚠️ 进入降级模式，原因: {rag_error or '检索结果为空'}")

    print(f"{'='*60}\n")

    return {
        "context": context,
        "messages": [{"role": "assistant", "content": assistant_msg}],
    }
