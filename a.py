from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 准备示例文本（实际项目中可换成文件读取）
raw_text = """
LangChain 是一个用于开发大语言模型应用的框架。
它提供了链式调用、提示词管理、向量存储等核心能力。
Chroma 是一个轻量级的向量数据库，适合本地开发和原型验证。
Sentence Transformers 可以将文本转换为高维向量，用于语义搜索。
"""

# 2. 文本分割（按字符递归分割，每块500字符，重叠50字符）
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", "。", "，", " ", ""]
)
docs = splitter.create_documents([raw_text])
print(f"分割为 {len(docs)} 个文档块")

# 3. 初始化 Embedding 模型（首次会自动下载模型到本地缓存）
# 模型约 400MB，使用 CPU 推理
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

# 4. 存入 Chroma 向量数据库（自动持久化到 ./chroma_db 目录）
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db",  # 数据保存路径
    collection_name="test_docs"
)

# 5. 相似性搜索
query = "什么是向量数据库？"
results = vectorstore.similarity_search(query, k=2)

print(f"\n🔍 查询: {query}")
print("-" * 40)
for i, doc in enumerate(results, 1):
    print(f"{i}. {doc.page_content}")
