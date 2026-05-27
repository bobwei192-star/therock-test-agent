#!/usr/bin/env python3
"""官方标准写法：使用 Chroma.persist_directory，不手动管理 client"""

from pathlib import Path
from uuid import uuid4
import os

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DOCS_DIR = Path("./docs")
CHROMA_DIR = Path(
    os.environ.get("TEST_CASE_AGENT_CHROMA_DIR", "./chroma_langchain_db")
)

# 本地模型缓存目录（优先使用 HOME 目录下的项目路径）
_LOCAL_MODEL_DIR = Path(os.environ.get(
    "TEST_CASE_AGENT_MODEL_DIR",
    str(Path.home() / "TestCaseAgent" / "llm_model")
))


def main():
    if not DOCS_DIR.exists():
        print(f"❌ 文档目录不存在: {DOCS_DIR}")
        return

    # 1. 加载
    docs = []
    for pattern in ["**/*.md", "**/*.txt", "**/*.rst", "**/*.py"]:
        loader = DirectoryLoader(
            str(DOCS_DIR),
            glob=pattern,
            loader_cls=TextLoader,
            show_progress=True,
            use_multithreading=True,
        )
        loaded = loader.load()
        print(f"  📄 {pattern}: {len(loaded)} 个文件")
        docs.extend(loaded)

    if not docs:
        print("❌ 没有文档")
        return

    print(f"\n📦 共加载 {len(docs)} 个文件")

    # 2. 切分
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", "。", ". ", " ", ""],
    )
    chunks = splitter.split_documents(docs)
    print(f"✂️  切分为 {len(chunks)} 个文本块")

    # 3. 嵌入模型
    print("🔮 加载 Embedding 模型...")
    
    # 定义模型名称和本地路径
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    local_model_path = _LOCAL_MODEL_DIR / "all-MiniLM-L6-v2"
    
    # 检查本地是否已存在模型
    if local_model_path.exists() and local_model_path.is_dir():
        # 检查是否有必要的模型文件
        required_files = ["config.json", "pytorch_model.bin", "tokenizer.json"]
        if all((local_model_path / f).exists() for f in required_files):
            print(f"[INFO] 使用本地模型: {local_model_path}")
            model_to_use = str(local_model_path)
        else:
            print(f"[INFO] 本地模型目录不完整，将从 HuggingFace 下载")
            model_to_use = model_name
    else:
        print(f"[INFO] 本地模型目录不存在，将从 HuggingFace 下载")
        model_to_use = model_name
    
    embeddings = HuggingFaceEmbeddings(
        model_name=model_to_use,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

    # 4. ✅ 官方标准：直接用 Chroma.from_documents + persist_directory
    # 不需要 import chromadb，不需要 PersistentClient
    print("📊 构建 Chroma 索引...")
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)

    # 如果旧数据存在，先清空重建（避免 ID 冲突）
    vector_store = Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
        collection_name="docs",
    )
    # 清空旧 collection（如果有）
    try:
        vector_store.delete_collection()
        print("⚠️  已删除旧 collection，重建中...")
    except Exception:
        pass

    # 重新初始化并添加文档
    vector_store = Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
        collection_name="docs",
    )

    # 官方推荐：显式生成 UUID 作为文档 ID
    uuids = [str(uuid4()) for _ in range(len(chunks))]
    vector_store.add_documents(documents=chunks, ids=uuids)

    print(f"\n{'='*50}")
    print(f"✅ 索引建立完成！")
    print(f"   文档数: {len(docs)}")
    print(f"   文本块: {len(chunks)}")
    print(f"   存储路径: {CHROMA_DIR.resolve()}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()