"""
download_embedding_model.py - Embedding 模型下载模块（兼容层）

从 download_model.py 重新导出，并提供标准化接口。
"""

from pathlib import Path
from typing import Tuple, List, Dict, Any, Optional

from huggingface_hub import HfApi
from src.agent.tools.download_model import (
    DOWNLOAD_TIMEOUT,
    DOWNLOAD_SOURCES,
    REQUIRED_FILES,
    verify_model,
    download_embedding_model,
    download_embedding_files,
    download_mirror,
    download_file_with_requests,
)


def download_model(
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    local_dir: Path = None,
    force: bool = False,
    speed_test: bool = False,
) -> bool:
    """下载 embedding 模型的标准化接口"""
    if local_dir is None:
        local_dir = Path("./models")
    return download_embedding_model(
        model_name=model_name,
        local_dir=local_dir,
        force=force,
        speed_test=speed_test,
    )


def download_with_snapshot(
    model_id: str,
    local_path: Path,
    mirror_url: str = "https://hf-mirror.com",
) -> bool:
    """使用 snapshot_download 下载模型"""
    return download_mirror(model_id, local_path, mirror_url)


def download_model_files_from_source(
    model_id: str,
    local_dir: Path,
    source: Dict[str, str],
) -> Tuple[bool, List[str]]:
    """从指定源下载模型文件"""
    source_name = source["name"]
    base_url = source["base_url"]

    try:
        api = HfApi()
        info = api.model_info(model_id)

        local_dir.mkdir(parents=True, exist_ok=True)

        downloaded_files = []
        for file_info in info.siblings:
            filename = file_info.rfilename
            if any(filename.endswith(f) for f in REQUIRED_FILES):
                file_url = f"{base_url}/{model_id}/resolve/main/{filename}"
                save_path = local_dir / filename
                success = download_file_with_requests(file_url, save_path, timeout=DOWNLOAD_TIMEOUT)
                if success:
                    downloaded_files.append(filename)

        return len(downloaded_files) > 0, downloaded_files

    except Exception as e:
        return False, []


__all__ = [
    "download_model",
    "download_with_snapshot",
    "download_model_files_from_source",
    "DOWNLOAD_TIMEOUT",
    "DOWNLOAD_SOURCES",
    "REQUIRED_FILES",
    "verify_model",
    "HfApi",
    "download_file_with_requests",
]
