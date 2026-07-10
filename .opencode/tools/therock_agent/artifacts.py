from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


def check_sudo_policy(policy: str, env: dict[str, str] | None = None) -> None:
    """Validate sudo readiness without reading or prompting for passwords."""
    if policy == "none":
        return
    if policy not in {"askpass", "cache"}:
        raise SystemExit(f"未知 THEROCK_SUDO_POLICY: {policy}")

    sudo = shutil.which("sudo")
    if not sudo:
        raise SystemExit(f"THEROCK_SUDO_POLICY={policy} 需要系统存在 sudo 命令。")

    if policy == "askpass":
        check_env = dict(os.environ)
        check_env.update(env or {})
        askpass = check_env.get("SUDO_ASKPASS") or check_env.get("THEROCK_SUDO_ASKPASS")
        if not askpass:
            raise SystemExit("THEROCK_SUDO_POLICY=askpass 需要设置 SUDO_ASKPASS。")
        askpass_path = Path(askpass).expanduser()
        if not askpass_path.is_file() or not os.access(askpass_path, os.X_OK):
            raise SystemExit(f"SUDO_ASKPASS 不存在或不可执行: {askpass_path}")
        try:
            result = subprocess.run(
                [sudo, "-A", "true"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                env=check_env,
                text=True,
                timeout=30,
            )
        except subprocess.TimeoutExpired as exc:
            raise SystemExit("THEROCK_SUDO_POLICY=askpass sudo 验证超时。") from exc
        if result.returncode != 0:
            raise SystemExit(
                "THEROCK_SUDO_POLICY=askpass 但 sudo askpass 验证失败。请先执行 "
                "`./scripts/therock-sudo-agent run -- opencode` 启动 OpenCode，"
                "或确认 session-scoped sudo agent 正在运行。"
            )
        return

    result = subprocess.run(
        [sudo, "-n", "true"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(
            "THEROCK_SUDO_POLICY=cache 但当前 sudo 缓存不可用。请先在同一用户终端执行 "
            "`sudo -v`，再启动 opencode 或重新执行 /therock-run。"
        )


def discover_therock_repo(project_root: Path, raw_path: str = "") -> Path | None:
    """Find the TheRock checkout without forcing users to pass --therock-repo."""
    candidates = [
        raw_path,
        os.environ.get("THEROCK_REPO", ""),
        str(project_root),
        str(Path.cwd()),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        path = Path(candidate).expanduser().resolve()
        scripts_dir = path / "build_tools" / "github_actions" / "test_executable_scripts"
        if scripts_dir.is_dir():
            return path
    return None


def resolve_artifacts_path(raw_path: str) -> tuple[Path, Path]:
    """Resolve build root and dist/rocm path from accepted artifact path shapes."""
    path = Path(raw_path).expanduser().resolve()

    if (path / "dist" / "rocm").is_dir():
        return path, path / "dist" / "rocm"

    if path.name == "rocm" and path.parent.name == "dist":
        return path.parent.parent, path

    if (path / "bin").is_dir() and ((path / "lib").is_dir() or (path / "lib64").is_dir()):
        return path.parent.parent if path.parent.name == "dist" else path, path

    raise SystemExit(
        "无法识别 ROCm artifacts path。请传入 /output-linux-portable/build、"
        "/output/build，或 dist/rocm 目录。"
    )
