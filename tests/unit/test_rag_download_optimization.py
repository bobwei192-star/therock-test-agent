"""RAG 和模型下载优化测试"""

import pytest
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from typing import Any

# 测试目标模块
from src.agent.tools.download_embedding_model import (
    download_model,
    download_with_snapshot,
    download_model_files_from_source,
    DOWNLOAD_TIMEOUT,
    DOWNLOAD_SOURCES,
)
from src.agent.nodes.node_context_retriever import (
    _download_model_with_fallback,
    _get_embeddings,
    _init_vectorstore,
)


class TestDownloadOptimizer:
    """测试多源阶梯下载优化"""

    def test_download_sources_config(self):
        """测试下载源配置"""
        assert len(DOWNLOAD_SOURCES) >= 2
        assert all("name" in source for source in DOWNLOAD_SOURCES)
        assert all("base_url" in source for source in DOWNLOAD_SOURCES)
        
        # 验证包含主要源
        source_names = [s["name"] for s in DOWNLOAD_SOURCES]
        assert "HuggingFace" in source_names
        assert "HF-Mirror" in source_names

    def test_download_timeout_config(self):
        """测试超时配置"""
        assert DOWNLOAD_TIMEOUT == 30  # 30秒超时

    @patch("src.agent.tools.download_embedding_model.HfApi")
    @patch("src.agent.tools.download_embedding_model.download_file_with_requests")
    def test_download_model_files_from_source_success(
        self, 
        mock_download: Mock,
        mock_api: Mock
    ):
        """测试从指定源下载文件成功"""
        # 模拟 API 返回
        mock_info = Mock()
        mock_info.siblings = [
            Mock(rfilename="config.json"),
            Mock(rfilename="pytorch_model.bin"),
        ]
        mock_api.return_value.model_info.return_value = mock_info
        
        # 模拟下载成功
        mock_download.return_value = True
        
        source = {"name": "HF-Mirror", "base_url": "https://hf-mirror.com"}
        local_dir = Path("/tmp/test_model")
        
        success, files = download_model_files_from_source(
            "test/model",
            local_dir,
            source
        )
        
        assert success is True
        assert len(files) == 2
        mock_download.assert_called()

    @patch("src.agent.tools.download_embedding_model.HfApi")
    def test_download_model_files_from_source_api_error(
        self, 
        mock_api: Mock
    ):
        """测试从指定源下载文件 API 错误"""
        mock_api.side_effect = Exception("API Error")
        
        source = {"name": "HuggingFace", "base_url": "https://huggingface.co"}
        local_dir = Path("/tmp/test_model")
        
        success, files = download_model_files_from_source(
            "test/model",
            local_dir,
            source
        )
        
        assert success is False
        assert len(files) == 0


class TestRAGDownloadIntegration:
    """测试 RAG 下载集成"""

    @patch("src.agent.nodes.node_context_retriever._LOCAL_MODEL_DIR", Path("/tmp/test_model"))
    def test_download_model_with_fallback_no_local(self):
        """测试没有本地模型时的下载"""
        # 清理可能存在的本地模型
        import shutil
        test_path = Path("/tmp/test_model/all-MiniLM-L6-v2")
        if test_path.exists():
            shutil.rmtree(test_path)
        
        # 模拟本地目录不存在
        with patch.object(Path, "exists", return_value=False):
            # 模拟 download_model 成功
            with patch("src.agent.tools.download_embedding_model.download_model") as mock_download:
                mock_download.return_value = True
                
                # 导入并测试
                from src.agent.nodes.node_context_retriever import _download_model_with_fallback
                
                result = _download_model_with_fallback()
                
                # 应该调用下载器并返回路径
                mock_download.assert_called()
                assert result is not None

    @patch("src.agent.nodes.node_context_retriever._LOCAL_MODEL_DIR", Path("/tmp/test_model"))
    def test_download_model_with_fallback_with_local(self):
        """测试有本地模型时的加载"""
        import shutil
        test_path = Path("/tmp/test_model/all-MiniLM-L6-v2")
        
        # 创建假的本地模型目录
        test_path.mkdir(parents=True, exist_ok=True)
        (test_path / "config.json").write_text("{}")
        (test_path / "pytorch_model.bin").write_text("fake")
        (test_path / "tokenizer.json").write_text("{}")
        
        try:
            # 模拟 _get_embeddings 避免实际加载
            with patch("src.agent.nodes.node_context_retriever._get_embeddings"):
                result = _download_model_with_fallback()
                
                # 应该返回本地路径
                assert result == str(test_path)
        finally:
            # 清理
            if test_path.exists():
                shutil.rmtree(test_path)

    @patch("src.agent.nodes.node_context_retriever._CHROMA_DIR", Path("/tmp/test_chroma"))
    @patch("src.agent.nodes.node_context_retriever._vectorstore")
    def test_init_vectorstore_no_chroma_dir(self, mock_vectorstore: Mock):
        """测试没有 Chroma 目录时的初始化"""
        mock_vectorstore.exists = False
        
        with patch("src.agent.nodes.node_context_retriever.Path") as mock_path:
            mock_path_instance = Mock()
            mock_path_instance.exists.return_value = False
            mock_path.return_value = mock_path_instance
            
            # 模拟 _get_embeddings
            with patch("src.agent.nodes.node_context_retriever._get_embeddings") as mock_get_emb:
                mock_emb = Mock()
                mock_get_emb.return_value = mock_emb
                
                # 清理全局状态
                import src.agent.nodes.node_context_retriever as retriever
                retriever._vectorstore = None
                
                result = retriever._init_vectorstore()
                
                # 应该返回一个 InMemoryVectorStore
                from langchain_core.vectorstores import InMemoryVectorStore
                assert isinstance(result, InMemoryVectorStore)


class TestRAGErrorHandling:
    """测试 RAG 错误处理"""

    @patch("src.agent.nodes.node_context_retriever._get_embeddings")
    def test_init_vectorstore_embedding_error(self, mock_get_emb: Mock):
        """测试 embedding 加载失败时的错误处理"""
        mock_get_emb.side_effect = RuntimeError("Embedding load failed")
        
        # 清理全局状态
        import src.agent.nodes.node_context_retriever as retriever
        retriever._vectorstore = None
        retriever._load_error = None
        
        result = retriever._init_vectorstore()
        
        # 应该返回 None
        assert result is None
        # 应该有错误信息
        assert retriever._load_error is not None
        assert "Embedding load failed" in retriever._load_error

    def test_init_vectorstore_already_cached(self):
        """测试 vectorstore 已缓存时的快速返回"""
        from langchain_core.vectorstores import InMemoryVectorStore
        
        import src.agent.nodes.node_context_retriever as retriever
        mock_vs = Mock(spec=InMemoryVectorStore)
        retriever._vectorstore = mock_vs
        
        result = retriever._init_vectorstore()
        
        # 应该直接返回缓存的实例
        assert result == mock_vs


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
