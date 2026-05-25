"""Embedding 模型下载工具 - 参考官方 LangChain 文档实现

解决以下问题：
1. HuggingFace 下载失败问题
2. 客户端关闭错误
3. 断点续传支持
4. 详细的错误处理和重试机制

使用方式：
    python -m src.agent.tools.download_embedding_model
    或
    from src.agent.tools.download_embedding_model import download_model
    download_model()
"""

import os
import sys
import time
import shutil
from pathlib import Path
from typing import Optional, Dict, Any

import requests
from huggingface_hub import snapshot_download, hf_hub_url, HfApi
from huggingface_hub.utils import (
    RepositoryNotFoundError,
    RevisionNotFoundError,
    HFValidationError,
    HfHubHTTPError,
)

# 默认模型配置
DEFAULT_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_LOCAL_DIR = Path("/home/zx/TestCaseAgent/llm_model")

# 必要的模型文件列表
REQUIRED_FILES = [
    "config.json",
    "pytorch_model.bin",
    "tokenizer.json",
    "tokenizer_config.json",
    "vocab.txt",
    "modules.json",
    "special_tokens_map.json",
    "README.md",
]


def download_with_requests(url: str, save_path: Path, chunk_size: int = 8192) -> bool:
    """使用 requests 库下载文件，支持断点续传"""
    try:
        # 检查是否已存在文件
        if save_path.exists():
            file_size = save_path.stat().st_size
            headers = {"Range": f"bytes={file_size}-"}
        else:
            file_size = 0
            headers = {}

        response = requests.get(url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()

        # 获取总大小
        total_size = int(response.headers.get("content-length", 0)) + file_size

        with open(save_path, "ab") as f:
            downloaded = file_size
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    # 显示进度
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\r[下载] {save_path.name}: {progress:.1f}% ({downloaded}/{total_size})", end="")

        print(f"\n[下载] ✅ {save_path.name} 下载完成")
        return True

    except requests.exceptions.RequestException as e:
        print(f"\n[下载] ❌ {save_path.name} 下载失败: {e}")
        return False


def download_model_files(model_name: str, local_dir: Path) -> bool:
    """手动下载模型文件列表"""
    print(f"[下载] 开始手动下载模型文件: {model_name}")
    
    api = HfApi()
    try:
        # 获取模型文件列表
        info = api.model_info(model_name)
        print(f"[下载] 模型信息: {info.modelId}, 版本: {info.sha}")
        
        # 创建目录
        local_dir.mkdir(parents=True, exist_ok=True)
        
        # 下载每个文件
        for file_info in info.siblings:
            filename = file_info.rfilename
            # 只下载必要的文件
            if any(filename.endswith(f) for f in REQUIRED_FILES):
                file_url = hf_hub_url(model_name, filename)
                save_path = local_dir / filename
                
                print(f"\n[下载] 获取: {filename}")
                if not download_with_requests(file_url, save_path):
                    print(f"[下载] ⚠️ 跳过 {filename}（下载失败）")
        
        return True
        
    except Exception as e:
        print(f"[下载] ❌ 获取模型信息失败: {e}")
        return False


def download_model(
    model_name: str = DEFAULT_MODEL_NAME,
    local_dir: Path = DEFAULT_LOCAL_DIR,
    force: bool = False,
) -> bool:
    """
    下载 HuggingFace embedding 模型到本地
    
    Args:
        model_name: HuggingFace 模型名称
        local_dir: 本地存储目录
        force: 是否强制重新下载
    
    Returns:
        True if download succeeded, False otherwise
    """
    print(f"\n{'='*60}")
    print(f"[下载器] 开始下载模型: {model_name}")
    print(f"[下载器] 目标目录: {local_dir}")
    print(f"{'='*60}")

    model_local_dir = local_dir / model_name.split("/")[-1]
    
    # 检查是否已存在完整模型
    if model_local_dir.exists() and not force:
        missing_files = []
        for required_file in REQUIRED_FILES:
            if not (model_local_dir / required_file).exists():
                missing_files.append(required_file)
        
        if not missing_files:
            print(f"[下载器] ✅ 模型已完整存在于: {model_local_dir}")
            return True
        else:
            print(f"[下载器] ⚠️ 模型目录存在但不完整，缺少: {missing_files}")
    
    # 创建目录
    model_local_dir.mkdir(parents=True, exist_ok=True)

    # 方法1: 尝试使用 huggingface_hub snapshot_download
    print("\n[下载器] 方法1: 使用 snapshot_download...")
    try:
        snapshot_download(
            repo_id=model_name,
            local_dir=str(model_local_dir),
            repo_type="model",
            ignore_patterns=["*.bin.index.json"],
            max_workers=4,
        )
        
        # 验证下载结果
        if all((model_local_dir / f).exists() for f in REQUIRED_FILES):
            print(f"[下载器] ✅ snapshot_download 成功")
            return True
        else:
            print(f"[下载器] ⚠️ snapshot_download 完成但文件不完整")
    
    except (RepositoryNotFoundError, RevisionNotFoundError) as e:
        print(f"[下载器] ❌ 模型不存在: {e}")
        return False
    except HFValidationError as e:
        print(f"[下载器] ❌ 验证失败: {e}")
    except HfHubHTTPError as e:
        print(f"[下载器] ❌ HTTP 错误: {e}")
    except Exception as e:
        print(f"[下载器] ❌ snapshot_download 失败: {type(e).__name__}: {e}")

    # 方法2: 手动下载必要文件
    print("\n[下载器] 方法2: 尝试手动下载...")
    if download_model_files(model_name, model_local_dir):
        # 验证下载结果
        missing_files = []
        for required_file in REQUIRED_FILES:
            if not (model_local_dir / required_file).exists():
                missing_files.append(required_file)
        
        if not missing_files:
            print(f"[下载器] ✅ 手动下载成功")
            return True
        else:
            print(f"[下载器] ❌ 手动下载仍缺少文件: {missing_files}")

    return False


def verify_model(model_path: Path) -> Dict[str, Any]:
    """验证模型目录是否完整"""
    result = {
        "model_path": str(model_path),
        "exists": model_path.exists(),
        "complete": False,
        "missing_files": [],
        "file_sizes": {},
    }
    
    if not model_path.exists():
        return result
    
    for required_file in REQUIRED_FILES:
        file_path = model_path / required_file
        if file_path.exists():
            result["file_sizes"][required_file] = file_path.stat().st_size
        else:
            result["missing_files"].append(required_file)
    
    result["complete"] = len(result["missing_files"]) == 0
    return result


def main():
    """命令行入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description="下载 HuggingFace embedding 模型")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL_NAME,
        help=f"模型名称 (默认: {DEFAULT_MODEL_NAME})"
    )
    parser.add_argument(
        "--local-dir",
        default=str(DEFAULT_LOCAL_DIR),
        help=f"本地存储目录 (默认: {DEFAULT_LOCAL_DIR})"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新下载"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="仅验证模型是否完整"
    )
    
    args = parser.parse_args()
    
    model_local_dir = Path(args.local_dir) / args.model.split("/")[-1]
    
    if args.verify:
        result = verify_model(model_local_dir)
        print(f"\n{'='*60}")
        print(f"模型验证结果: {model_local_dir}")
        print(f"{'='*60}")
        print(f"目录存在: {result['exists']}")
        print(f"模型完整: {result['complete']}")
        if result["missing_files"]:
            print(f"缺少文件: {result['missing_files']}")
        if result["file_sizes"]:
            print("文件大小:")
            for filename, size in result["file_sizes"].items():
                print(f"  {filename}: {size / 1024 / 1024:.2f} MB")
        sys.exit(0)
    
    # 执行下载
    success = download_model(
        model_name=args.model,
        local_dir=Path(args.local_dir),
        force=args.force
    )
    
    if success:
        print(f"\n{'='*60}")
        print("[下载器] ✅ 模型下载完成！")
        print(f"[下载器] 模型位置: {model_local_dir}")
        print(f"{'='*60}")
        sys.exit(0)
    else:
        print(f"\n{'='*60}")
        print("[下载器] ❌ 模型下载失败！")
        print(f"{'='*60}")
        sys.exit(1)


if __name__ == "__main__":
    main()
