#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
download_model.py
一键自动下载 Hugging Face 模型，阶梯回退，10s 超时探测 + 下载进度检测

用法:
  python download_model.py              # 默认 auto，自动探测并下载
  python download_model.py --method mirror
  python download_model.py --method sbert
"""

import os
import sys
import time
import argparse
import subprocess
import threading
import requests
from pathlib import Path
from typing import Optional, Callable, List

# ========================= 配置区 =========================
DEFAULT_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
_LOCAL_MODEL_DIR = Path("./llm_model")
HF_MIRROR_URL = "https://hf-mirror.com"
PROBE_TIMEOUT = 10       # API 探测超时（秒）
DOWNLOAD_START_TIMEOUT = 10  # 下载启动检测：10s 内必须有文件写入
# ==========================================================


def load_env_file(filepath: str = ".env") -> None:
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
    load_env_file(".env")
    return os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")


def get_local_model_path(model_id: str, base_dir: Path = _LOCAL_MODEL_DIR) -> Path:
    return base_dir / model_id.replace("/", "--")


def flush_print(msg: str):
    print(msg, flush=True)


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
    try:
        r = requests.get(f"{mirror_url}/api/models/{model_id}", timeout=PROBE_TIMEOUT)
        return r.status_code == 200
    except Exception:
        return False


def probe_hf_official(model_id: str, token: Optional[str] = None) -> bool:
    try:
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        r = requests.get(f"https://huggingface.co/api/models/{model_id}", headers=headers, timeout=PROBE_TIMEOUT)
        return r.status_code == 200
    except Exception:
        return False


# ───────────────────────────────────────────────
# 下载方法实现
# ───────────────────────────────────────────────
def download_mirror(model_id: str, local_path: Path, mirror_url: str = HF_MIRROR_URL):
    flush_print(f"  → 镜像站 snapshot_download 开始...")
    os.environ["HF_ENDPOINT"] = mirror_url
    from huggingface_hub import snapshot_download
    local_path.mkdir(parents=True, exist_ok=True)
    snapshot_download(repo_id=model_id, local_dir=str(local_path))
    return True


def download_token(model_id: str, local_path: Path, token: str):
    flush_print(f"  → Token 认证 snapshot_download 开始...")
    from huggingface_hub import snapshot_download
    local_path.mkdir(parents=True, exist_ok=True)
    snapshot_download(repo_id=model_id, local_dir=str(local_path), token=token)
    return True


def download_sbert(model_id: str, local_path: Path, token: Optional[str] = None):
    flush_print(f"  → sentence-transformers 下载开始...")
    from sentence_transformers import SentenceTransformer
    local_path.mkdir(parents=True, exist_ok=True)
    model = SentenceTransformer(model_id, cache_folder=str(local_path.parent), token=token)
    model.save(str(local_path))
    return True


def download_transformers(model_id: str, local_path: Path, token: Optional[str] = None):
    flush_print(f"  → transformers 下载开始...")
    from transformers import AutoModel, AutoTokenizer
    local_path.mkdir(parents=True, exist_ok=True)
    tok = AutoTokenizer.from_pretrained(model_id, cache_dir=str(local_path), token=token)
    mdl = AutoModel.from_pretrained(model_id, cache_dir=str(local_path), token=token)
    tok.save_pretrained(str(local_path))
    mdl.save_pretrained(str(local_path))
    return True


def download_hf_cli(model_id: str, local_path: Path, token: Optional[str] = None):
    flush_print(f"  → hf CLI 下载开始...")
    local_path.mkdir(parents=True, exist_ok=True)
    cmd = ["hf", "download", model_id, "--local-dir", str(local_path)]
    if token:
        cmd.extend(["--token", token])
    subprocess.run(cmd, check=True)
    return True


def download_git_lfs(model_id: str, local_path: Path, token: Optional[str] = None):
    flush_print(f"  → git-lfs 克隆开始...")
    local_path.mkdir(parents=True, exist_ok=True)
    git_url = f"https://{('user:' + token + '@') if token else ''}huggingface.co/{model_id}"
    subprocess.run(["git", "clone", "--depth", "1", git_url, str(local_path)], check=True)
    return True


# ───────────────────────────────────────────────
# Auto 模式：探测 → 下载 → 10s 进度检测 → 回退
# ───────────────────────────────────────────────
def download_auto(model_id: str, local_path: Path, mirror_url: str = HF_MIRROR_URL):
    token = get_hf_token()
    flush_print(f"\n🚀 Auto 模式 | 模型: {model_id}")
    flush_print(f"   本地路径: {local_path}")
    flush_print(f"   HF_TOKEN: {(token or '未设置')[:20]}...")
    flush_print(f"   探测超时: {PROBE_TIMEOUT}s | 下载启动检测: {DOWNLOAD_START_TIMEOUT}s\n")

    methods: List[tuple] = [
        ("镜像站 (hf-mirror.com)", probe_mirror, (model_id, mirror_url), download_mirror, (model_id, local_path, mirror_url)),
        ("Token + 官方 Hub", probe_hf_official, (model_id, token), download_token, (model_id, local_path, token)),
        ("sentence-transformers", None, None, download_sbert, (model_id, local_path, token)),
        ("transformers 库", None, None, download_transformers, (model_id, local_path, token)),
        ("hf CLI", None, None, download_hf_cli, (model_id, local_path, token)),
        ("git-lfs 克隆", None, None, download_git_lfs, (model_id, local_path, token)),
    ]

    for idx, (name, probe_fn, probe_args, dl_fn, dl_args) in enumerate(methods, 1):
        flush_print(f"{'─' * 50}")
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

    flush_print(f"\n💥 所有 {len(methods)} 种方法均失败")
    return False


# ───────────────────────────────────────────────
# 主函数
# ───────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="一键下载 Hugging Face 模型，自动探测、阶梯回退、10s 超时检测",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python download_model.py              # 默认 auto，自动探测所有方法
  python download_model.py --method mirror
  python download_model.py --method sbert
  python download_model.py --model bert-base-chinese --cache-dir ./my_models
        """
    )
    parser.add_argument("--method", type=str, default="auto",
                        choices=["auto", "mirror", "token", "sbert", "transformers", "hf-cli", "git-lfs"],
                        help="下载方法 (默认: auto)")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL_ID, help=f"模型ID (默认: {DEFAULT_MODEL_ID})")
    parser.add_argument("--token", type=str, default=None, help="HF Token (覆盖 .env)")
    parser.add_argument("--cache-dir", type=str, default=str(_LOCAL_MODEL_DIR), help=f"保存路径 (默认: {_LOCAL_MODEL_DIR})")
    parser.add_argument("--mirror-url", type=str, default=HF_MIRROR_URL, help=f"镜像站 (默认: {HF_MIRROR_URL})")

    args = parser.parse_args()
    if args.token:
        os.environ["HF_TOKEN"] = args.token

    local_path = get_local_model_path(args.model, Path(args.cache_dir))

    method_map = {
        "mirror": lambda: download_mirror(args.model, local_path, args.mirror_url),
        "token": lambda: download_token(args.model, local_path, get_hf_token()),
        "sbert": lambda: download_sbert(args.model, local_path, get_hf_token()),
        "transformers": lambda: download_transformers(args.model, local_path, get_hf_token()),
        "hf-cli": lambda: download_hf_cli(args.model, local_path, get_hf_token()),
        "git-lfs": lambda: download_git_lfs(args.model, local_path, get_hf_token()),
    }

    if args.method == "auto":
        success = download_auto(args.model, local_path, args.mirror_url)
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
