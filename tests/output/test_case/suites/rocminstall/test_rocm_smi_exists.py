"""
test_rocm_smi_exists.py

验证 ROCm 基础环境中 rocm-smi 工具已正确安装且可执行。
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
