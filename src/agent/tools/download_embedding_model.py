"""Embedding 模型下载工具 - 支持多源阶梯下载（10秒超时切换）

解决以下问题：
1. HuggingFace 下载失败问题
2. 多种下载源自动切换（10秒超时）
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
import threading
import queue
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

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

# 下载超时时间（秒）
DOWNLOAD_TIMEOUT = 10

# 多种下载源配置（按优先级排序）
# 注意：HF-Mirror 在前面优先尝试，因为国内可直接访问
DOWNLOAD_SOURCES = [
    {"name": "HF-Mirror", "base_url": "https://hf-mirror.com", "priority": 1},
    {"name": "HuggingFace", "base_url": "https://huggingface.co", "priority": 2},
]


class DownloadTimeoutError(Exception):
    """下载超时异常"""
    pass


class DownloadResult:
    """下载结果"""
    def __init__(self, success: bool, message: str, method: str = "", files_downloaded: List[str] = None):
        self.success = success
        self.message = message
        self.method = method
        self.files_downloaded = files_downloaded or []


def download_with_timeout(
    download_func,
    timeout: int = DOWNLOAD_TIMEOUT,
    *args,
    **kwargs
) -> Tuple[bool, str]:
    """
    带超时的下载函数
    
    Args:
        download_func: 下载函数
        timeout: 超时时间（秒）
        *args, **kwargs: 传递给下载函数的参数
    
    Returns:
        (success, message) 元组
    """
    result_queue = queue.Queue()
    error_queue = queue.Queue()
    
    def worker():
        try:
            result = download_func(*args, **kwargs)
            result_queue.put(result)
        except Exception as e:
            error_queue.put(str(e))
    
    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
    thread.join(timeout=timeout)
    
    if thread.is_alive():
        # 超时
        return False, f"下载超时（{timeout}秒）"
    
    if not error_queue.empty():
        # 执行出错
        return False, error_queue.get()
    
    if not result_queue.empty():
        # 成功
        return True, result_queue.get()
    
    return False, "未知错误"


def download_file_with_requests(
    url: str, 
    save_path: Path, 
    chunk_size: int = 8192,
    timeout: int = DOWNLOAD_TIMEOUT
) -> bool:
    """使用 requests 库下载单个文件"""
    try:
        # 检查是否已存在文件（断点续传）
        if save_path.exists():
            file_size = save_path.stat().st_size
            headers = {"Range": f"bytes={file_size}-"}
        else:
            file_size = 0
            headers = {}

        response = requests.get(url, headers=headers, stream=True, timeout=timeout)
        response.raise_for_status()

        # 获取总大小
        total_size = int(response.headers.get("content-length", 0)) + file_size

        with open(save_path, "wb" if file_size == 0 else "ab") as f:
            downloaded = file_size
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    # 显示进度
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\r  [进度] {save_path.name}: {progress:.1f}%", end="")

        print(f"\n  ✅ {save_path.name} 下载完成")
        return True

    except requests.exceptions.Timeout:
        print(f"\n  ⏱️ {save_path.name} 下载超时")
        return False
    except requests.exceptions.RequestException as e:
        print(f"\n  ❌ {save_path.name} 下载失败: {e}")
        return False


def download_model_files_from_source(
    model_name: str, 
    local_dir: Path,
    source: Dict[str, str]
) -> Tuple[bool, List[str]]:
    """
    从指定源下载模型文件列表
    
    Args:
        model_name: 模型名称
        local_dir: 本地目录
        source: 下载源配置 {name, base_url}
    
    Returns:
        (success, downloaded_files) 元组
    """
    source_name = source["name"]
    base_url = source["base_url"]
    
    print(f"\n  📥 从 {source_name} ({base_url}) 下载...")
    
    try:
        api = HfApi()
        info = api.model_info(model_name)
        
        local_dir.mkdir(parents=True, exist_ok=True)
        
        downloaded_files = []
        for file_info in info.siblings:
            filename = file_info.rfilename
            # 只下载必要的文件
            if any(filename.endswith(f) for f in REQUIRED_FILES):
                file_url = f"{base_url}/{model_name}/resolve/main/{filename}"
                save_path = local_dir / filename
                
                print(f"\n  📥 获取: {filename}")
                
                # 带超时的下载
                success = download_file_with_requests(
                    file_url, 
                    save_path, 
                    timeout=DOWNLOAD_TIMEOUT
                )
                
                if success:
                    downloaded_files.append(filename)
                else:
                    print(f"  ⚠️ 跳过 {filename}（下载失败或超时）")
        
        return len(downloaded_files) > 0, downloaded_files
        
    except Exception as e:
        print(f"  ❌ 获取模型信息失败: {e}")
        return False, []


def download_with_snapshot(
    model_name: str,
    local_dir: Path,
    source: Dict[str, str]
) -> bool:
    """
    使用 snapshot_download 下载模型
    
    Args:
        model_name: 模型名称
        local_dir: 本地目录
        source: 下载源配置
    
    Returns:
        是否成功
    """
    source_name = source["name"]
    base_url = source["base_url"]
    
    print(f"\n  📥 使用 {source_name} snapshot_download...")
    
    # 设置环境变量（如果使用镜像）
    env = {}
    if source_name == "HF-Mirror":
        env["HF_ENDPOINT"] = base_url
    
    try:
        snapshot_download(
            repo_id=model_name,
            local_dir=str(local_dir),
            repo_type="model",
            ignore_patterns=["*.bin.index.json"],
            max_workers=4,
            timeout=DOWNLOAD_TIMEOUT,
        )
        
        # 验证下载结果
        if all((local_dir / f).exists() for f in REQUIRED_FILES if not f.endswith(".bin")):
            print(f"  ✅ {source_name} snapshot_download 成功")
            return True
            
    except Exception as e:
        print(f"  ⚠️ {source_name} snapshot_download 失败: {type(e).__name__}: {e}")
    
    return False


def download_model(
    model_name: str = DEFAULT_MODEL_NAME,
    local_dir: Path = DEFAULT_LOCAL_DIR,
    force: bool = False,
) -> bool:
    """
    多源阶梯下载 HuggingFace embedding 模型
    
    策略：
    1. 依次尝试每个下载源
    2. 每个源设置 10 秒超时
    3. 如果一个源超时或失败，自动切换到下一个源
    4. 优先使用 snapshot_download，失败则回退到手动下载文件
    
    Args:
        model_name: HuggingFace 模型名称
        local_dir: 本地存储目录
        force: 是否强制重新下载
    
    Returns:
        True if download succeeded, False otherwise
    """
    print(f"\n{'='*60}")
    print(f"🤖 多源阶梯下载模型: {model_name}")
    print(f"📁 目标目录: {local_dir}")
    print(f"⏱️ 每种方法超时: {DOWNLOAD_TIMEOUT}秒")
    print(f"{'='*60}")

    # 确保 local_dir 是 Path 对象
    if isinstance(local_dir, str):
        local_dir = Path(local_dir)
    
    model_local_dir = local_dir / model_name.split("/")[-1]
    
    # 检查是否已存在完整模型
    if model_local_dir.exists() and not force:
        missing_files = []
        for required_file in REQUIRED_FILES:
            if not (model_local_dir / required_file).exists():
                missing_files.append(required_file)
        
        if not missing_files:
            print(f"✅ 模型已完整存在于: {model_local_dir}")
            return True
        else:
            print(f"⚠️ 模型目录存在但不完整，缺少: {missing_files}")
    
    # 创建目录
    model_local_dir.mkdir(parents=True, exist_ok=True)

    # 阶梯下载策略
    download_methods = [
        # 方法1-2: 使用 snapshot_download
        lambda: ("snapshot", download_with_snapshot(
            model_name, 
            model_local_dir, 
            source
        ))
        for source in DOWNLOAD_SOURCES
    ] + [
        # 方法3-4: 手动下载文件
        lambda src=source: ("files", download_model_files_from_source(
            model_name,
            model_local_dir,
            src
        ))
        for source in DOWNLOAD_SOURCES
    ]
    
    # 依次尝试每种方法
    for idx, method_func in enumerate(download_methods, 1):
        print(f"\n{'='*60}")
        print(f"🔄 尝试方法 {idx}/{len(download_methods)}")
        print(f"{'='*60}")
        
        try:
            method_type, result = method_func()
            
            if method_type == "snapshot":
                if result:
                    print(f"\n✅ 方法 {idx} 成功！")
                    return True
            else:  # files
                success, downloaded_files = result
                if success:
                    # 验证下载结果
                    missing = [
                        f for f in REQUIRED_FILES 
                        if not (model_local_dir / f).exists()
                    ]
                    if not missing:
                        print(f"\n✅ 方法 {idx} 成功！已下载 {len(downloaded_files)} 个文件")
                        return True
                    else:
                        print(f"\n⚠️ 方法 {idx} 下载不完整，缺少: {missing}")
                        continue
            
            print(f"⏭️ 方法 {idx} 失败，尝试下一个方法...")
            
        except Exception as e:
            print(f"❌ 方法 {idx} 出错: {type(e).__name__}: {e}")
            continue

    # 所有方法都失败了
    print(f"\n❌ 所有下载方法都失败了！")
    print(f"请手动下载模型或检查网络连接")
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
