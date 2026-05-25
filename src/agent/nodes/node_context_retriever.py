"""RAG 上下文检索节点 —— 官方 LangChain 模式（InMemoryVectorStore + 懒加载）

与官方 guide/06_官方rag.md 对齐：
- 向量库在首次检索时创建，避免 pytest collection 阶段加载重依赖
- 从 Chroma 持久化目录一次性加载到内存后，Chroma client 即关闭
- 所有查询走 InMemoryVectorStore，不存在连接断开问题
"""

import os
from pathlib import Path
from typing import Any

from langchain_core.documents import Document  # noqa: E402
from langchain_core.vectorstores import InMemoryVectorStore  # noqa: E402
from ..state import AgentState  # noqa: E402

_CHROMA_DIR = Path(
    os.environ.get("TEST_CASE_AGENT_CHROMA_DIR", "./chroma_langchain_db")
)

# 本地模型缓存目录
_LOCAL_MODEL_DIR = Path("/home/zx/TestCaseAgent/llm_model")

_embeddings: Any | None = None
_vectorstore: InMemoryVectorStore | None = None
_load_error: str | None = None


def _get_embeddings() -> Any:
    """懒加载 HuggingFace embeddings，避免模块导入阶段加载 torch。
    
    处理网络错误和客户端关闭问题：
    - 加载失败时重置全局状态，允许下次重试
    - 添加重试机制处理临时网络问题
    - 优先使用本地模型缓存目录
    """
    global _embeddings, _load_error

    if _embeddings is not None:
        return _embeddings

    try:
        from langchain_huggingface import HuggingFaceEmbeddings
    except ImportError as exc:
        _load_error = (
            "缺少 RAG embedding 依赖，请安装: "
            "pip install langchain-huggingface sentence-transformers"
        )
        raise RuntimeError(_load_error) from exc

    # 定义模型名称和本地路径
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    local_model_path = _LOCAL_MODEL_DIR / "all-MiniLM-L6-v2"
    
    # 检查本地是否已存在模型
    if local_model_path.exists() and local_model_path.is_dir():
        # 检查是否有必要的模型文件
        required_files = ["config.json", "pytorch_model.bin", "tokenizer.json"]
        if all((local_model_path / f).exists() for f in required_files):
            print(f"[RAG] 使用本地模型: {local_model_path}")
            model_to_use = str(local_model_path)
        else:
            print(f"[RAG] 本地模型目录不完整，将从 HuggingFace 下载")
            model_to_use = model_name
    else:
        print(f"[RAG] 本地模型目录不存在，将从 HuggingFace 下载")
        model_to_use = model_name

    max_retries = 2
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            _embeddings = HuggingFaceEmbeddings(
                model_name=model_to_use,
                model_kwargs={"device": "cpu"},
                encode_kwargs={"normalize_embeddings": True},
            )
            _load_error = None  # 成功加载，清除之前的错误
            return _embeddings
        except Exception as exc:
            last_exception = exc
            print(f"[RAG] embedding 加载失败 (尝试 {attempt + 1}/{max_retries}): {exc}")
            # 如果是从本地加载失败，尝试从 HuggingFace 下载
            if model_to_use != model_name:
                print(f"[RAG] 本地加载失败，尝试从 HuggingFace 下载...")
                model_to_use = model_name
            # 重置状态，允许下次重试
            _embeddings = None
            if attempt < max_retries - 1:
                import time
                time.sleep(1)  # 等待 1 秒后重试

    _load_error = f"embedding 加载失败 ({max_retries} 次尝试): {last_exception}"
    raise RuntimeError(_load_error) from last_exception


def _init_vectorstore() -> InMemoryVectorStore:
    """首次检索时从 Chroma 持久化目录一次性加载到 InMemoryVectorStore。

    之后所有查询走内存，不再依赖 Chroma client 连接。
    
    处理客户端关闭错误：
    - 加载失败时重置全局状态，允许下次重试
    - 捕获客户端关闭异常并优雅降级
    """
    global _vectorstore, _load_error

    if _vectorstore is not None:
        return _vectorstore

    try:
        embeddings = _get_embeddings()
    except RuntimeError as exc:
        # embedding 加载失败，设置为空，在检索时处理降级逻辑
        _load_error = f"embedding 初始化失败: {exc}"
        print(f"[RAG] ⚠️ {_load_error}")
        _vectorstore = None
        return _vectorstore

    vs = InMemoryVectorStore(embeddings)

    if not _CHROMA_DIR.exists():
        _load_error = (
            f"向量库 {_CHROMA_DIR} 不存在。请先运行: python index_docs_official.py，"
            "或设置 TEST_CASE_AGENT_CHROMA_DIR 指向已有索引。"
        )
        print(f"[RAG] ⚠️ {_load_error}")
        _vectorstore = vs
        return vs

    try:
        import chromadb
        from langchain_chroma import Chroma

        client = chromadb.PersistentClient(path=str(_CHROMA_DIR))
        chroma_vs = Chroma(
            client=client, collection_name="docs",
            embedding_function=embeddings,
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

        # 安全关闭客户端
        try:
            del chroma_vs
            del client
            import gc
            gc.collect()
        except Exception:
            pass  # 忽略清理时的错误

    except RuntimeError as exc:
        # 客户端关闭错误或其他运行时错误，优雅降级
        _load_error = f"客户端错误: {exc}"
        print(f"[RAG] ❌ 加载 chroma_db 失败（客户端错误）: {_load_error}")
        # 返回空的内存向量库，允许后续请求重试
        _vectorstore = InMemoryVectorStore(embeddings)
        return _vectorstore
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
        if store is None:
            # embedding 加载失败，直接进入降级模式
            rag_error = _load_error or "embedding 未初始化"
            print(f"[RAG] ⚠️ embedding 未初始化，跳过检索")
        else:
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
