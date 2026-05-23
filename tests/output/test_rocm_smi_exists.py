"""
test_rocm_smi_exists.py

验证 ROCm 基础环境中 rocm-smi 工具已正确安装且可执行。
包含 stdout/stderr 捕获分离验证测试。
"""

import shutil
import subprocess
import pytest

ROCM_SMI_CMD = "rocm-smi"
ROCM_SMI_HARD_PATH = "/opt/rocm/bin/rocm-smi"


def _find_rocm_smi():
    """返回 rocm-smi 的路径，如果找不到则返回 None。"""
    path = shutil.which(ROCM_SMI_CMD)
    if path:
        return path
    if shutil.which(ROCM_SMI_HARD_PATH) or (
        ROCM_SMI_HARD_PATH
        and __import__("os").access(ROCM_SMI_HARD_PATH, __import__("os").X_OK)
    ):
        return ROCM_SMI_HARD_PATH
    return None


def _run_rocm_smi(*args):
    """运行 rocm-smi 并返回 CompletedProcess。"""
    cmd = [_find_rocm_smi(), *args]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=30)


@pytest.fixture(scope="module")
def rocm_smi_path():
    """Fixture: 返回 rocm-smi 路径，不存在则 skip。"""
    path = _find_rocm_smi()
    if path is None:
        pytest.skip("rocm-smi not found in PATH or /opt/rocm/bin/")
    return path


class TestRocmSmiExists:
    """rocm-smi 存在性及基本功能测试。"""

    def test_rocm_smi_found(self, rocm_smi_path):
        """验证 rocm-smi 命令在系统中存在。"""
        assert rocm_smi_path, "rocm-smi 路径不应为空"
        assert rocm_smi_path.endswith("rocm-smi"), (
            f"路径应以 rocm-smi 结尾: {rocm_smi_path}"
        )

    def test_rocm_smi_executable(self, rocm_smi_path):
        """验证 rocm-smi 文件可执行。"""
        import os

        assert os.access(rocm_smi_path, os.X_OK), f"rocm-smi 不可执行: {rocm_smi_path}"

    def test_rocm_smi_version(self, rocm_smi_path):
        """运行 rocm-smi --version，验证返回版本号且 exit code 为 0。"""
        result = _run_rocm_smi("--version")
        assert result.returncode == 0, (
            f"rocm-smi --version 失败\n"
            f"returncode: {result.returncode}\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )
        assert len(result.stdout.strip()) > 0, "rocm-smi --version 输出为空"

    def test_rocm_smi_showhw(self, rocm_smi_path):
        """运行 rocm-smi --showhw，验证能检测 GPU 硬件信息。

        此测试在无 GPU 环境下可能失败，但不阻断整个 suite。
        """
        result = _run_rocm_smi("--showhw")
        if result.returncode != 0:
            pytest.skip(
                f"rocm-smi --showhw 未返回 0（可能无 GPU 设备）\n"
                f"returncode: {result.returncode}\n"
                f"stdout: {result.stdout}\n"
                f"stderr: {result.stderr}"
            )
        assert len(result.stdout.strip()) > 0, "rocm-smi --showhw 输出为空"

    def test_rocm_smi_capture_stdout_stderr(self, rocm_smi_path):
        """验证 subprocess 调用能正确捕获并分离 stdout 和 stderr。

        使用 rocm-smi --help（产生 stdout）和 rocm-smi 无效选项（产生 stderr）
        来验证捕获机制正确分离两个输出流。
        """
        # --- 测试 1: stdout 捕获 ---
        result_help = subprocess.run(
            [rocm_smi_path, "--help"], capture_output=True, text=True, timeout=30
        )
        assert result_help.returncode == 0, (
            f"rocm-smi --help 失败\n"
            f"returncode: {result_help.returncode}\n"
            f"stdout: {result_help.stdout}\n"
            f"stderr: {result_help.stderr}"
        )
        assert len(result_help.stdout.strip()) > 0, (
            "rocm-smi --help 的 stdout 为空，捕获可能失败"
        )

        # --- 测试 2: stderr 捕获 ---
        result_bad = subprocess.run(
            [rocm_smi_path, "--nonexistent-flag-xyz"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        # 无效选项预期返回非 0
        assert result_bad.returncode != 0, "rocm-smi 无效选项预期返回非 0，但返回了 0"
        assert len(result_bad.stderr.strip()) > 0, (
            "rocm-smi --nonexistent-flag-xyz 的 stderr 为空，stderr 捕获可能失败"
        )

        # --- 测试 3: 流分离验证 ---
        # stdout 不应包含 stderr 内容
        assert "nonexistent" not in result_help.stderr.lower(), (
            "stdout 流中不应包含 stderr 的错误信息"
        )
        # stderr 不应包含 stdout 的帮助信息
        assert "usage" not in result_bad.stdout.lower(), (
            "stderr 流中不应包含 stdout 的使用帮助信息"
        )

    def test_rocm_smi_capture_separation(self, rocm_smi_path):
        """验证 stdout 和 stderr 内容互不污染。

        使用一个同时产生 stdout 和 stderr 的命令（通过 shell 组合），
        验证两个流被正确分离捕获。
        """
        # 构造一个同时输出 stdout 和 stderr 的 shell 命令
        # 使用 rocm-smi --version 输出到 stdout，同时用无效选项输出到 stderr
        combined_cmd = (
            f"{rocm_smi_path} --version 2>/dev/null; "
            f"{rocm_smi_path} --nonexistent-flag-xyz 2>&1 1>/dev/null"
        )
        result = subprocess.run(
            ["bash", "-c", combined_cmd], capture_output=True, text=True, timeout=30
        )

        # 验证 stdout 包含版本信息
        assert len(result.stdout.strip()) > 0, (
            f"组合命令的 stdout 为空\n"
            f"returncode: {result.returncode}\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )

        # 验证 stderr 包含错误信息
        assert len(result.stderr.strip()) > 0, (
            f"组合命令的 stderr 为空\n"
            f"returncode: {result.returncode}\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )

        # 验证流分离：stdout 不应包含 stderr 的错误关键词
        assert "unrecognized" not in result.stdout.lower(), (
            f"stdout 被 stderr 污染，包含 'unrecognized'\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )
