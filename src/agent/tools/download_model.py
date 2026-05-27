#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
download_model.py - 通用模型下载工具
支持多源阶梯下载、断点续传、速度自动探测、文件进度检测

功能特点：
1. 支持多种下载方法（mirror、token、sbert、transformers、hf-cli、git-lfs、hfd）
2. 下载前自动测速，智能选择最快下载源
3. 支持 embedding 模型专门处理，只下载必要文件
4. 断点续传支持，避免重复下载
5. 模型完整性验证

用法:
  python download_model.py              # 默认 auto，自动测速并选择最快方式
  python download_model.py --method mirror
  python download_model.py --model sentence-transformers/all-MiniLM-L6-v2
"""

import os
import sys
import time
import json
import argparse
import subprocess
import threading
import requests
from pathlib import Path
from typing import Optional, Callable, List, Tuple, Dict, Any

# ========================= 配置区 =========================
DEFAULT_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
_LOCAL_MODEL_DIR = Path("./llm_model")
HF_MIRROR_URL = "https://hf-mirror.com"
PROBE_TIMEOUT = 10       # API 探测超时（秒）
DOWNLOAD_START_TIMEOUT = 15  # 下载启动检测：15s 内必须有文件写入
DOWNLOAD_TIMEOUT = 30     # 单个文件下载超时
SPEED_TEST_TIMEOUT = 10    # 速度测试超时（秒）
SPEED_TEST_FILE_SIZE = 1024 * 1024 * 8  # 8MB 测速文件（增大提高准确性）

# Embedding 模型必要文件列表
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

# 下载源配置（用于速度测试）
DOWNLOAD_SOURCES = [
    {"name": "HF-Mirror", "base_url": "https://hf-mirror.com"},
    {"name": "HuggingFace", "base_url": "https://huggingface.co"},
]

# 测速测试文件（选择小而常见的文件）
SPEED_TEST_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
SPEED_TEST_FILE = "config.json"
# ==========================================================


def load_env_file(filepath: str = ".env") -> None:
    """加载 .env 文件"""
    env_path = Path(filepath)
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    os.environ.setdefault(key, value)


def get_hf_token() -> Optional[str]:
    """获取 HuggingFace Token"""
    load_env_file(".env")
    return os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")


def get_local_model_path(model_id: str, base_dir: Path = _LOCAL_MODEL_DIR) -> Path:
    """获取本地模型路径"""
    return base_dir / model_id.replace("/", "--")


def flush_print(msg: str):
    """立即刷新打印"""
    print(msg, flush=True)


# ───────────────────────────────────────────────
# 速度测试功能
# ───────────────────────────────────────────────
def test_download_speed(url: str, timeout: int = SPEED_TEST_TIMEOUT, chunk_size: int = 16384) -> float:
    """
    测试下载速度（改进版）
    
    Args:
        url: 测试文件URL
        timeout: 超时时间（秒）
        chunk_size: 下载块大小
    
    Returns:
        下载速度（MB/s），失败返回 0
    """
    try:
        start_time = time.time()
        downloaded = 0
        session = requests.Session()
        
        # 设置合理的超时
        response = session.get(url, stream=True, timeout=timeout)
        response.raise_for_status()
        
        # 获取文件大小（如果服务器提供）
        content_length = response.headers.get('Content-Length')
        file_size = int(content_length) if content_length else SPEED_TEST_FILE_SIZE
        
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                downloaded += len(chunk)
                elapsed = time.time() - start_time
                
                # 达到超时时间或下载了足够的数据就停止
                if elapsed >= timeout or downloaded >= SPEED_TEST_FILE_SIZE:
                    break
        
        elapsed = time.time() - start_time
        
        if elapsed > 0 and downloaded > 0:
            speed_mbps = (downloaded / (1024 * 1024)) / elapsed
            return round(speed_mbps, 2)
        
        return 0.0
    except requests.exceptions.RequestException as e:
        # 网络错误，返回0
        return 0.0
    except Exception:
        return 0.0


def test_all_speeds_parallel(model_id: str, token: Optional[str] = None) -> List[Tuple[str, float]]:
    """
    并行测试所有下载源的速度（更快）
    
    Args:
        model_id: 模型ID（用于构建测试URL）
        token: HuggingFace Token
    
    Returns:
        按速度排序的列表 [(name, speed_mbps), ...]
    """
    flush_print(f"\n{'='*60}")
    flush_print("🚀 正在并行测试各下载源速度...")
    flush_print(f"{'='*60}")
    
    speed_results = {}
    threads = []
    
    def test_source(name: str, url: str):
        """测试单个源的速度"""
        speed = test_download_speed(url, SPEED_TEST_TIMEOUT)
        speed_results[name] = speed
    
    # 构建测试URL列表
    test_urls = []
    
    # 1. 镜像站
    mirror_test_url = f"{HF_MIRROR_URL}/{SPEED_TEST_MODEL}/resolve/main/{SPEED_TEST_FILE}"
    test_urls.append(("镜像站 (hf-mirror.com)", mirror_test_url))
    
    # 2. 官方Hub（带Token）
    if token:
        official_token_url = f"https://huggingface.co/{SPEED_TEST_MODEL}/resolve/main/{SPEED_TEST_FILE}"
        test_urls.append(("Token + 官方 Hub", official_token_url))
    
    # 3. 官方Hub（无Token）
    official_url = f"https://huggingface.co/{SPEED_TEST_MODEL}/resolve/main/{SPEED_TEST_FILE}"
    test_urls.append(("官方 Hub (无Token)", official_url))
    
    # 并行启动所有测试
    for name, url in test_urls:
        t = threading.Thread(target=test_source, args=(name, url), daemon=True)
        threads.append(t)
        t.start()
    
    # 等待所有测试完成
    for t in threads:
        t.join()
    
    # 按速度降序排序
    speed_results_list = sorted(speed_results.items(), key=lambda x: -x[1])
    
    # 输出结果
    for name, speed in speed_results_list:
        status = "✅" if speed > 0 else "❌"
        flush_print(f"   {status} [{speed:6.2f} MB/s] {name}")
    
    flush_print(f"\n{'='*60}")
    if speed_results_list and speed_results_list[0][1] > 0:
        flush_print(f"🏆 最快源: {speed_results_list[0][0]} ({speed_results_list[0][1]:.2f} MB/s)")
    else:
        flush_print("⚠️ 所有源速度测试失败，使用默认顺序")
    flush_print(f"{'='*60}")
    
    return speed_results_list


def get_speed_priority(method_name: str, speed_results: List[Tuple[str, float]]) -> float:
    """
    根据速度测试结果获取方法优先级
    
    Args:
        method_name: 方法名称
        speed_results: 速度测试结果列表
    
    Returns:
        优先级分数（越小优先级越高）
    """
    for name, speed in speed_results:
        if name in method_name or method_name.split(" ")[0] in name:
            return -speed  # 速度越快，优先级越高（负数用于升序排序）
    
    # 如果没有匹配，返回最低优先级
    return float('inf')


# ───────────────────────────────────────────────
# 通用：带超时的函数执行 + 文件进度检测
# ───────────────────────────────────────────────
def run_with_file_watch(
    func: Callable,
    args: tuple,
    watch_dir: Path,
    start_timeout: int = DOWNLOAD_START_TIMEOUT
) -> tuple:
    """
    在后台线程运行下载函数。
    - start_timeout 秒内若 watch_dir 无新文件/无更新 → 视为卡住，返回失败
    - 若有文件活动 → 继续等待直至完成
    返回: (success: bool, info: str)
    """
    result = [None]
    exc = [None]

    def wrapper():
        try:
            result[0] = func(*args)
        except Exception as e:
            exc[0] = e

    def get_file_state():
        if not watch_dir.exists():
            return set(), {}
        files = list(watch_dir.rglob("*"))
        file_set = {f for f in files if f.is_file()}
        mtimes = {f: f.stat().st_mtime for f in file_set}
        return file_set, mtimes

    initial_files, initial_mtimes = get_file_state()

    t = threading.Thread(target=wrapper, daemon=True)
    t.start()
    t.join(start_timeout)

    if not t.is_alive():
        if exc[0]:
            return False, str(exc[0])
        return True, "完成"

    current_files, current_mtimes = get_file_state()
    new_files = current_files - initial_files
    updated = {f for f in (current_files & initial_files) if current_mtimes.get(f, 0) > initial_mtimes.get(f, 0)}

    if new_files or updated:
        flush_print(f"   ⏳ 检测到下载活动 ({len(new_files)} 新文件, {len(updated)} 更新)，继续等待...")
        t.join()
        if exc[0]:
            return False, str(exc[0])
        return True, "完成"
    else:
        flush_print(f"   ⏱️ {start_timeout}s 内无任何文件写入，判定为网络无响应")
        return False, "timeout"


def run_probe(func: Callable, args: tuple, timeout: int = PROBE_TIMEOUT) -> bool:
    """带超时的探测函数"""
    result = [None]
    exc = [None]

    def wrapper():
        try:
            result[0] = func(*args)
        except Exception as e:
            exc[0] = e

    t = threading.Thread(target=wrapper, daemon=True)
    t.start()
    t.join(timeout)

    if t.is_alive() or exc[0] is not None:
        return False
    return bool(result[0])


# ───────────────────────────────────────────────
# 连通性探测
# ───────────────────────────────────────────────
def probe_mirror(model_id: str, mirror_url: str = HF_MIRROR_URL) -> bool:
    """探测镜像站连通性"""
    try:
        r = requests.get(f"{mirror_url}/api/models/{model_id}", timeout=PROBE_TIMEOUT)
        return r.status_code == 200
    except Exception:
        return False


def probe_hf_official(model_id: str, token: Optional[str] = None) -> bool:
    """探测官方 Hub 连通性"""
    try:
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        r = requests.get(f"https://huggingface.co/api/models/{model_id}", headers=headers, timeout=PROBE_TIMEOUT)
        return r.status_code == 200
    except Exception:
        return False


# ───────────────────────────────────────────────
# 单个文件下载（支持断点续传）
# ───────────────────────────────────────────────
def download_file_with_requests(
    url: str,
    save_path: Path,
    chunk_size: int = 8192,
    timeout: int = DOWNLOAD_TIMEOUT
) -> bool:
    """使用 requests 库下载单个文件（支持断点续传）"""
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


# ───────────────────────────────────────────────
# 下载方法实现
# ───────────────────────────────────────────────
def download_mirror(model_id: str, local_path: Path, mirror_url: str = HF_MIRROR_URL):
    """从镜像站下载"""
    flush_print(f"  → 镜像站 snapshot_download 开始...")
    os.environ["HF_ENDPOINT"] = mirror_url
    from huggingface_hub import snapshot_download
    local_path.mkdir(parents=True, exist_ok=True)
    snapshot_download(repo_id=model_id, local_dir=str(local_path))
    return True


def download_token(model_id: str, local_path: Path, token: str):
    """使用 Token 认证下载"""
    flush_print(f"  → Token 认证 snapshot_download 开始...")
    from huggingface_hub import snapshot_download
    local_path.mkdir(parents=True, exist_ok=True)
    snapshot_download(repo_id=model_id, local_dir=str(local_path), token=token)
    return True


def download_sbert(model_id: str, local_path: Path, token: Optional[str] = None):
    """使用 sentence-transformers 库下载"""
    flush_print(f"  → sentence-transformers 下载开始...")
    from sentence_transformers import SentenceTransformer
    local_path.mkdir(parents=True, exist_ok=True)
    model = SentenceTransformer(model_id, cache_folder=str(local_path.parent), token=token)
    model.save(str(local_path))
    return True


def download_transformers(model_id: str, local_path: Path, token: Optional[str] = None):
    """使用 transformers 库下载"""
    flush_print(f"  → transformers 下载开始...")
    from transformers import AutoModel, AutoTokenizer
    local_path.mkdir(parents=True, exist_ok=True)
    tok = AutoTokenizer.from_pretrained(model_id, cache_dir=str(local_path), token=token)
    mdl = AutoModel.from_pretrained(model_id, cache_dir=str(local_path), token=token)
    tok.save_pretrained(str(local_path))
    mdl.save_pretrained(str(local_path))
    return True


def download_hf_cli(model_id: str, local_path: Path, token: Optional[str] = None):
    """使用 hf CLI 下载"""
    flush_print(f"  → hf CLI 下载开始...")
    local_path.mkdir(parents=True, exist_ok=True)
    cmd = ["hf", "download", model_id, "--local-dir", str(local_path)]
    if token:
        cmd.extend(["--token", token])
    subprocess.run(cmd, check=True)
    return True


def download_git_lfs(model_id: str, local_path: Path, token: Optional[str] = None):
    """使用 git-lfs 克隆"""
    flush_print(f"  → git-lfs 克隆开始...")
    local_path.mkdir(parents=True, exist_ok=True)
    git_url = f"https://{('user:' + token + '@') if token else ''}huggingface.co/{model_id}"
    subprocess.run(["git", "clone", "--depth", "1", git_url, str(local_path)], check=True)
    return True


def download_hfd(model_id: str, local_path: Path, token: Optional[str] = None):
    """使用 hfd.sh + aria2c 下载（国内镜像加速，多线程）"""
    flush_print(f"  → hfd.sh + aria2c 下载开始...")
    local_path.mkdir(parents=True, exist_ok=True)
    
    # 检查 aria2c 是否安装
    try:
        subprocess.run(["aria2c", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        flush_print("  ⚠️ aria2c 未安装，尝试自动安装...")
        try:
            subprocess.run(["sudo", "snap", "install", "aria2c"], check=True)
        except subprocess.CalledProcessError:
            subprocess.run(["sudo", "apt", "update", "-y"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "aria2"], check=True)
    
    # 下载 hfd.sh 脚本（如果不存在）
    hfd_script = Path.home() / ".local" / "bin" / "hfd"
    if not hfd_script.exists():
        flush_print("  下载 hfd.sh 脚本...")
        subprocess.run(["wget", "-q", "-O", str(hfd_script), "https://hf-mirror.com/hfd/hfd.sh"], check=True)
        subprocess.run(["chmod", "+x", str(hfd_script)], check=True)
    
    # 使用 hfd.sh 下载
    env = os.environ.copy()
    env["HF_ENDPOINT"] = "https://hf-mirror.com"
    cmd = [str(hfd_script), model_id, "--tool", "aria2c", "-x", "4", "--local-dir", str(local_path.parent)]
    if token:
        cmd.extend(["--token", token])
    
    subprocess.run(cmd, check=True, env=env)
    return True


def download_embedding_files(model_id: str, local_path: Path, source: Dict[str, str]) -> Tuple[bool, List[str]]:
    """
    从指定源手动下载 embedding 模型必要文件（支持断点续传）
    
    Args:
        model_id: 模型名称
        local_path: 本地目录
        source: 下载源配置 {name, base_url}
    
    Returns:
        (success, downloaded_files) 元组
    """
    source_name = source["name"]
    base_url = source["base_url"]
    
    flush_print(f"\n  📥 从 {source_name} ({base_url}) 下载文件...")
    
    try:
        from huggingface_hub import HfApi
        api = HfApi()
        info = api.model_info(model_id)
        
        local_path.mkdir(parents=True, exist_ok=True)
        
        downloaded_files = []
        for file_info in info.siblings:
            filename = file_info.rfilename
            # 只下载必要的文件
            if any(filename.endswith(f) for f in REQUIRED_FILES):
                file_url = f"{base_url}/{model_id}/resolve/main/{filename}"
                save_path = local_path / filename
                
                flush_print(f"\n  📥 获取: {filename}")
                
                # 带超时的下载（支持断点续传）
                success = download_file_with_requests(
                    file_url,
                    save_path,
                    timeout=DOWNLOAD_TIMEOUT
                )
                
                if success:
                    downloaded_files.append(filename)
                else:
                    flush_print(f"  ⚠️ 跳过 {filename}（下载失败或超时）")
        
        return len(downloaded_files) > 0, downloaded_files
        
    except Exception as e:
        flush_print(f"  ❌ 获取模型信息失败: {e}")
        return False, []


# ───────────────────────────────────────────────
# 模型验证
# ───────────────────────────────────────────────
def verify_model(model_path: Path, required_files: List[str] = None) -> Dict[str, Any]:
    """验证模型目录是否完整"""
    files_to_check = required_files or REQUIRED_FILES
    
    result = {
        "model_path": str(model_path),
        "exists": model_path.exists(),
        "complete": False,
        "missing_files": [],
        "file_sizes": {},
    }
    
    if not model_path.exists():
        return result
    
    for required_file in files_to_check:
        file_path = model_path / required_file
        if file_path.exists():
            result["file_sizes"][required_file] = file_path.stat().st_size
        else:
            result["missing_files"].append(required_file)
    
    result["complete"] = len(result["missing_files"]) == 0
    return result


# ───────────────────────────────────────────────
# Auto 模式：并行测速 → 智能排序 → 下载 → 进度检测 → 回退
# ───────────────────────────────────────────────
def download_auto(model_id: str, local_path: Path, mirror_url: str = HF_MIRROR_URL, is_embedding: bool = False, speed_test: bool = True):
    """自动模式下载（支持并行速度测试）"""
    token = get_hf_token()
    flush_print(f"\n🚀 Auto 模式 | 模型: {model_id}")
    flush_print(f"   本地路径: {local_path}")
    flush_print(f"   HF_TOKEN: {(token or '未设置')[:20]}...")
    flush_print(f"   探测超时: {PROBE_TIMEOUT}s | 下载启动检测: {DOWNLOAD_START_TIMEOUT}s")
    flush_print(f"   模式: {'Embedding 模型' if is_embedding else '通用模型'}")
    flush_print(f"   速度测试: {'启用' if speed_test else '禁用'}")

    # 定义所有下载方法及其对应的测速源名称
    all_methods = [
        ("镜像站 (hf-mirror.com)", "镜像站", probe_mirror, (model_id, mirror_url), download_mirror, (model_id, local_path, mirror_url)),
        ("hfd.sh + aria2c (镜像加速)", "镜像站", None, None, download_hfd, (model_id, local_path, token)),
        ("Token + 官方 Hub", "Token + 官方 Hub", probe_hf_official, (model_id, token), download_token, (model_id, local_path, token)),
        ("官方 Hub (无Token)", "官方 Hub (无Token)", probe_hf_official, (model_id, None), download_mirror, (model_id, local_path, "https://huggingface.co")),
        ("sentence-transformers", "官方 Hub (无Token)", None, None, download_sbert, (model_id, local_path, token)),
        ("transformers 库", "官方 Hub (无Token)", None, None, download_transformers, (model_id, local_path, token)),
        ("hf CLI", "官方 Hub (无Token)", None, None, download_hf_cli, (model_id, local_path, token)),
        ("git-lfs 克隆", "官方 Hub (无Token)", None, None, download_git_lfs, (model_id, local_path, token)),
    ]

    speed_results = []
    # 并行速度测试并排序
    if speed_test:
        speed_results = test_all_speeds_parallel(model_id, token)
        
        # 根据速度结果重新排序方法
        def priority_key(method):
            method_name, speed_source_name, _, _, _, _ = method
            return get_speed_priority(speed_source_name, speed_results)
        
        all_methods.sort(key=priority_key)
        
        # 过滤掉速度为0的源对应的方法（如果所有源都有速度，不过滤）
        if any(speed > 0 for _, speed in speed_results):
            all_methods = [m for m in all_methods if get_speed_priority(m[1], speed_results) != float('inf')]
    
    methods = all_methods

    # 打印排序后的下载顺序
    if speed_test and speed_results:
        flush_print("\n📊 按速度排序后的下载顺序:")
        for i, m in enumerate(methods, 1):
            flush_print(f"   {i}. {m[0]}")

    for idx, (name, _, probe_fn, probe_args, dl_fn, dl_args) in enumerate(methods, 1):
        flush_print(f"\n{'─' * 50}")
        flush_print(f"[{idx}/{len(methods)}] 尝试: {name}")

        if probe_fn is not None:
            flush_print(f"   ⏳ API 探测连通性 ({PROBE_TIMEOUT}s)...")
            if run_probe(probe_fn, probe_args, PROBE_TIMEOUT):
                flush_print(f"   ✅ API 探测通过")
            else:
                flush_print(f"   ❌ API 探测失败，跳过")
                continue

        flush_print(f"   ⏳ 开始下载，{DOWNLOAD_START_TIMEOUT}s 内检测文件活动...")
        ok, info = run_with_file_watch(dl_fn, dl_args, local_path, DOWNLOAD_START_TIMEOUT)
        if ok:
            flush_print(f"\n🎉 成功通过 [{name}] 完成下载!")
            return True
        else:
            flush_print(f"   ❌ {info}")
            continue

    # 如果是 embedding 模型，尝试手动下载文件作为最后手段
    if is_embedding:
        flush_print(f"\n{'─' * 50}")
        flush_print(f"[备用] 尝试手动下载 embedding 文件...")
        for source in DOWNLOAD_SOURCES:
            success, downloaded_files = download_embedding_files(model_id, local_path, source)
            if success:
                # 验证下载结果
                result = verify_model(local_path)
                if result["complete"]:
                    flush_print(f"\n🎉 通过手动下载完成 embedding 模型!")
                    return True
                else:
                    flush_print(f"   ⚠️ 下载不完整，缺少: {result['missing_files']}")

    flush_print(f"\n💥 所有下载方法均失败")
    return False


# ───────────────────────────────────────────────
# Embedding 模型专用下载
# ───────────────────────────────────────────────
def download_embedding_model(
    model_name: str = DEFAULT_MODEL_ID,
    local_dir: Path = _LOCAL_MODEL_DIR,
    force: bool = False,
    speed_test: bool = True,
) -> bool:
    """
    多源阶梯下载 HuggingFace embedding 模型
    
    策略：
    1. 下载前自动测速，选择最快源
    2. 依次尝试每个下载源
    3. 每个源设置 10 秒超时
    4. 如果一个源超时或失败，自动切换到下一个源
    5. 优先使用 snapshot_download，失败则回退到手动下载文件
    
    Args:
        model_name: HuggingFace 模型名称
        local_dir: 本地存储目录
        force: 是否强制重新下载
        speed_test: 是否启用速度测试
    
    Returns:
        True if download succeeded, False otherwise
    """
    flush_print(f"\n{'='*60}")
    flush_print(f"🤖 多源阶梯下载 Embedding 模型: {model_name}")
    flush_print(f"📁 目标目录: {local_dir}")
    flush_print(f"⏱️ 每种方法超时: {DOWNLOAD_TIMEOUT}秒")
    flush_print(f"{'='*60}")

    model_local_dir = local_dir / model_name.split("/")[-1]

    # 检查是否已存在完整模型
    if model_local_dir.exists() and not force:
        result = verify_model(model_local_dir)
        if result["complete"]:
            flush_print(f"✅ 模型已完整存在于: {model_local_dir}")
            return True
        else:
            flush_print(f"⚠️ 模型目录存在但不完整，缺少: {result['missing_files']}")

    # 创建目录
    model_local_dir.mkdir(parents=True, exist_ok=True)

    # 尝试自动模式下载
    return download_auto(model_name, model_local_dir, is_embedding=True, speed_test=speed_test)


# ───────────────────────────────────────────────
# 通用模型下载
# ───────────────────────────────────────────────
def download_general_model(
    model_name: str,
    local_dir: Path = _LOCAL_MODEL_DIR,
    speed_test: bool = True,
) -> bool:
    """
    下载通用模型
    
    Args:
        model_name: HuggingFace 模型名称
        local_dir: 本地存储目录
        speed_test: 是否启用速度测试
    
    Returns:
        True if download succeeded, False otherwise
    """
    flush_print(f"\n{'='*60}")
    flush_print(f"🤖 下载通用模型: {model_name}")
    flush_print(f"📁 目标目录: {local_dir}")
    flush_print(f"{'='*60}")

    local_path = get_local_model_path(model_name, local_dir)
    
    # 检查是否已存在
    if local_path.exists():
        flush_print(f"⚠️ 模型目录已存在: {local_path}")
        flush_print(f"   如果需要重新下载，请先删除该目录")
    
    # 创建目录
    local_path.mkdir(parents=True, exist_ok=True)

    # 尝试自动模式下载
    return download_auto(model_name, local_path, is_embedding=False, speed_test=speed_test)


# ───────────────────────────────────────────────
# 主函数
# ───────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="一键下载 Hugging Face 模型，自动测速、智能选择最快源、阶梯回退、10s 超时检测",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python download_model.py              # 默认 auto，自动测速并选择最快方式
  python download_model.py --method mirror
  python download_model.py --method hfd  # 使用 hfd.sh + aria2c 加速下载
  python download_model.py --no-speed-test  # 禁用速度测试，使用默认顺序
  python download_model.py --model bert-base-chinese --cache-dir ./my_models
  python download_model.py --embedding  # 专门下载 embedding 模型
        """
    )
    parser.add_argument("--method", type=str, default="auto",
                        choices=["auto", "mirror", "token", "sbert", "transformers", "hf-cli", "git-lfs", "hfd"],
                        help="下载方法 (默认: auto)")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL_ID, help=f"模型ID (默认: {DEFAULT_MODEL_ID})")
    parser.add_argument("--token", type=str, default=None, help="HF Token (覆盖 .env)")
    parser.add_argument("--cache-dir", type=str, default=str(_LOCAL_MODEL_DIR), help=f"保存路径 (默认: {_LOCAL_MODEL_DIR})")
    parser.add_argument("--mirror-url", type=str, default=HF_MIRROR_URL, help=f"镜像站 (默认: {HF_MIRROR_URL})")
    parser.add_argument("--embedding", action="store_true", help="使用 embedding 模型专用下载模式")
    parser.add_argument("--force", action="store_true", help="强制重新下载 (仅 embedding 模式)")
    parser.add_argument("--verify", action="store_true", help="仅验证模型是否完整")
    parser.add_argument("--no-speed-test", action="store_true", help="禁用下载前速度测试")

    args = parser.parse_args()
    if args.token:
        os.environ["HF_TOKEN"] = args.token

    local_path = get_local_model_path(args.model, Path(args.cache_dir))
    speed_test = not args.no_speed_test

    # 验证模式
    if args.verify:
        result = verify_model(local_path)
        flush_print(f"\n{'='*60}")
        flush_print(f"模型验证结果: {local_path}")
        flush_print(f"{'='*60}")
        flush_print(f"目录存在: {result['exists']}")
        flush_print(f"模型完整: {result['complete']}")
        if result["missing_files"]:
            flush_print(f"缺少文件: {result['missing_files']}")
        if result["file_sizes"]:
            flush_print("文件大小:")
            for filename, size in result["file_sizes"].items():
                flush_print(f"  {filename}: {size / 1024 / 1024:.2f} MB")
        sys.exit(0)

    # Embedding 专用模式
    if args.embedding:
        success = download_embedding_model(
            model_name=args.model,
            local_dir=Path(args.cache_dir),
            force=args.force,
            speed_test=speed_test
        )
    else:
        # 通用模式
        method_map = {
            "mirror": lambda: download_mirror(args.model, local_path, args.mirror_url),
            "token": lambda: download_token(args.model, local_path, get_hf_token()),
            "sbert": lambda: download_sbert(args.model, local_path, get_hf_token()),
            "transformers": lambda: download_transformers(args.model, local_path, get_hf_token()),
            "hf-cli": lambda: download_hf_cli(args.model, local_path, get_hf_token()),
            "git-lfs": lambda: download_git_lfs(args.model, local_path, get_hf_token()),
            "hfd": lambda: download_hfd(args.model, local_path, get_hf_token()),
        }

        if args.method == "auto":
            success = download_auto(args.model, local_path, args.mirror_url, is_embedding=False, speed_test=speed_test)
        else:
            flush_print(f"\n📦 模型: {args.model} | 📁 保存到: {local_path}")
            try:
                method_map[args.method]()
                success = True
            except Exception as e:
                flush_print(f"❌ 失败: {e}")
                success = False

    if success:
        flush_print(f"\n✅ 完成! 模型保存在: {local_path}")
        sys.exit(0)
    else:
        flush_print("\n❌ 下载失败。建议排查:\n   1. 检查网络能否访问 hf-mirror.com\n   2. 尝试开启代理后重试\n   3. 手动用浏览器下载模型文件")
        sys.exit(1)


if __name__ == "__main__":
    main()
