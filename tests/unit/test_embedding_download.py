"""测试 embedding 模型下载与加载功能。

验证 node_context_retriever.py 中 _get_embeddings() 的行为：
1. 模型能否成功下载/加载
2. 加载后能否正常生成向量
3. 重试机制是否生效
4. 缓存机制是否正常（第二次加载走缓存）
"""

import pytest
import numpy as np
from unittest.mock import patch, MagicMock

from src.agent.nodes import node_context_retriever as rag


@pytest.fixture(autouse=True)
def reset_global_state():
    """每个测试前重置模块级全局变量，确保测试隔离。"""
    rag._embeddings = None
    rag._vectorstore = None
    rag._load_error = None
    yield
    rag._embeddings = None
    rag._vectorstore = None
    rag._load_error = None


class TestEmbeddingDownload:
    """测试 embedding 模型的下载和加载。"""

    @pytest.mark.slow
    def test_embedding_model_loads_successfully(self):
        """验证 sentence-transformers/all-MiniLM-L6-v2 模型可以成功加载。

        注意：首次运行会从 HuggingFace 下载模型（约 80MB），后续走本地缓存。
        """
        embeddings = rag._get_embeddings()
        assert embeddings is not None

    @pytest.mark.slow
    def test_embedding_generates_vector(self):
        """验证加载的模型能正确生成向量。"""
        embeddings = rag._get_embeddings()

        # 测试单文本嵌入
        vector = embeddings.embed_query("rocm-smi 温度监控测试")
        assert isinstance(vector, list)
        assert len(vector) > 0
        # all-MiniLM-L6-v2 输出 384 维向量
        assert len(vector) == 384
        # 向量值应为浮点数
        assert all(isinstance(v, float) for v in vector)

    @pytest.mark.slow
    def test_embedding_batch_documents(self):
        """验证批量文档嵌入功能。"""
        embeddings = rag._get_embeddings()

        docs = [
            "ROCm 安装验证",
            "GPU 性能测试",
            "Docker 镜像构建",
        ]
        vectors = embeddings.embed_documents(docs)
        assert len(vectors) == 3
        assert all(len(v) == 384 for v in vectors)

    @pytest.mark.slow
    def test_embedding_normalization(self):
        """验证向量已归一化（encode_kwargs 中设置了 normalize_embeddings=True）。"""
        embeddings = rag._get_embeddings()

        vector = embeddings.embed_query("测试文本")
        # L2 范数应接近 1.0（归一化后）
        norm = np.linalg.norm(vector)
        assert abs(norm - 1.0) < 1e-5, f"向量 L2 范数 = {norm}，期望接近 1.0"

    @pytest.mark.slow
    def test_embedding_cached_on_second_call(self):
        """验证第二次调用 _get_embeddings() 返回缓存实例（不重新加载）。"""
        first = rag._get_embeddings()
        second = rag._get_embeddings()
        # 应该是同一个对象（缓存命中）
        assert first is second

    @pytest.mark.slow
    def test_similar_texts_have_high_cosine_similarity(self):
        """验证语义相近的文本生成的向量余弦相似度高。"""
        embeddings = rag._get_embeddings()

        v1 = np.array(embeddings.embed_query("ROCm GPU 测试"))
        v2 = np.array(embeddings.embed_query("AMD GPU 验证"))
        v3 = np.array(embeddings.embed_query("今天天气不错"))

        # 余弦相似度
        sim_related = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        sim_unrelated = np.dot(v1, v3) / (np.linalg.norm(v1) * np.linalg.norm(v3))

        # 相关文本的相似度应明显高于无关文本
        assert sim_related > sim_unrelated, (
            f"相关文本相似度 ({sim_related:.4f}) 应高于无关文本 ({sim_unrelated:.4f})"
        )


class TestEmbeddingRetryMechanism:
    """测试 embedding 加载的重试机制。"""

    def test_retry_on_first_failure_then_success(self):
        """验证首次加载失败后会重试，第二次成功则正常返回。"""
        mock_embeddings = MagicMock()
        call_count = {"n": 0}

        def mock_hf_embeddings(*args, **kwargs):
            call_count["n"] += 1
            if call_count["n"] == 1:
                raise ConnectionError("模拟网络超时")
            return mock_embeddings

        with patch(
            "src.agent.nodes.node_context_retriever.HuggingFaceEmbeddings",
            side_effect=mock_hf_embeddings,
        ) as mock_cls:
            # 需要先 patch import
            import src.agent.nodes.node_context_retriever as module
            # 手动注入 HuggingFaceEmbeddings 到模块
            with patch.dict("sys.modules", {"langchain_huggingface": MagicMock(HuggingFaceEmbeddings=mock_hf_embeddings)}):
                with patch("src.agent.nodes.node_context_retriever.HuggingFaceEmbeddings", side_effect=mock_hf_embeddings, create=True):
                    # 直接测试重试逻辑
                    rag._embeddings = None
                    try:
                        from langchain_huggingface import HuggingFaceEmbeddings as RealHF
                        with patch("langchain_huggingface.HuggingFaceEmbeddings", side_effect=mock_hf_embeddings):
                            result = rag._get_embeddings()
                            assert result is mock_embeddings
                            assert call_count["n"] == 2
                    except ImportError:
                        pytest.skip("langchain_huggingface 未安装")

    def test_raises_after_max_retries_exhausted(self):
        """验证达到最大重试次数后抛出 RuntimeError。"""
        def always_fail(*args, **kwargs):
            raise ConnectionError("持续网络错误")

        with patch("langchain_huggingface.HuggingFaceEmbeddings", side_effect=always_fail):
            with pytest.raises(RuntimeError, match="embedding 加载失败"):
                rag._get_embeddings()

    def test_global_state_reset_on_failure(self):
        """验证加载失败后全局状态被正确重置，允许后续重试。"""
        def fail_once(*args, **kwargs):
            raise OSError("磁盘空间不足")

        with patch("langchain_huggingface.HuggingFaceEmbeddings", side_effect=fail_once):
            with pytest.raises(RuntimeError):
                rag._get_embeddings()

        # 失败后全局缓存应为 None，允许下次重试
        assert rag._embeddings is None
        assert rag._load_error is not None


class TestEmbeddingMissingDependency:
    """测试缺少依赖时的错误处理。"""

    def test_import_error_raises_runtime_error(self):
        """验证缺少 langchain_huggingface 时抛出明确错误信息。"""
        with patch.dict("sys.modules", {"langchain_huggingface": None}):
            with patch("builtins.__import__", side_effect=ImportError("No module named 'langchain_huggingface'")):
                rag._embeddings = None
                with pytest.raises((RuntimeError, ImportError)):
                    rag._get_embeddings()
