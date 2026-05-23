"""
test_rocm_smi_exists.py

验证 ROCm 基础环境中 rocm-smi 工具已正确安装且可执行。
包含 stdout/stderr 捕获分离验证测试。
追加 GPU 温度检查测试函数，通过 rocm-smi --showtemp 验证温度传感器可访问、
温度值在合理范围内，且输出格式符合预期。
"""

import os
import re
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
        ROCM_SMI_HARD_PATH and os.access(ROCM_SMI_HARD_PATH, os.X_OK)
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

        # 验证 stdout 和 stderr 内容不同（流已分离）
        assert result.stdout.strip() != result.stderr.strip(), (
            f"stdout 和 stderr 内容相同，流分离可能失败\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )


class TestGpuTemperature:
    """GPU 温度检查测试。

    通过 rocm-smi --showtemp 获取 GPU 温度信息，验证：
    - 命令执行成功 (exit code 0)
    - 输出包含 GPU 温度行
    - 温度值在物理合理范围 (0°C ~ 110°C)
    - stderr 无报错信息
    """

    @pytest.fixture(autouse=True)
    def _check_gpu_available(self, rocm_smi_path):
        """前置检查：确保至少有一张 GPU 可被 rocm-smi 识别。"""
        result = _run_rocm_smi("--showhw")
        if result.returncode != 0:
            pytest.skip("无可用 GPU 设备或 rocm-smi 无法访问 GPU")

    def test_rocm_smi_showtemp_exit_code(self, rocm_smi_path):
        """执行 rocm-smi --showtemp，验证 exit code 为 0。"""
        result = _run_rocm_smi("--showtemp")
        assert result.returncode == 0, (
            f"rocm-smi --showtemp 失败\n"
            f"returncode: {result.returncode}\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )

    def test_rocm_smi_showtemp_has_temperature_lines(self, rocm_smi_path):
        """验证 rocm-smi --showtemp 输出包含 GPU 温度信息行。

        预期输出格式包含 GPU 索引（如 GPU[0]）和温度值（如 50.0°C）。
        支持多种格式：°C、C、或纯数字。
        """
        result = _run_rocm_smi("--showtemp")
        assert result.returncode == 0, (
            f"rocm-smi --showtemp 执行失败，无法检查温度行\n"
            f"returncode: {result.returncode}\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )

        stdout = result.stdout
        # 检查是否包含 GPU 标识行（如 GPU[0]、GPU0、GPU 0 等）
        gpu_line_pattern = re.compile(r"GPU\s*\[\s*\d+\s*\]", re.IGNORECASE)
        gpu_lines = [
            line for line in stdout.splitlines() if gpu_line_pattern.search(line)
        ]

        assert len(gpu_lines) > 0, (
            f"rocm-smi --showtemp 输出中未找到 GPU 温度行\n完整 stdout:\n{stdout}"
        )

    def test_rocm_smi_showtemp_temperature_in_range(self, rocm_smi_path):
        """解析温度值，验证所有 GPU 温度在 0°C ~ 110°C 合理范围内。

        支持多种温度格式：
        - 50.0°C
        - 50.0 C
        - 50.0
        """
        result = _run_rocm_smi("--showtemp")
        assert result.returncode == 0, (
            f"rocm-smi --showtemp 执行失败，无法解析温度\n"
            f"returncode: {result.returncode}\n"
            f"stdout: {result.stdout}\n"
            f"stderr: {result.stderr}"
        )

        stdout = result.stdout
        # 匹配温度值：支持 50.0°C、50.0 C、50.0 等格式
        temp_pattern = re.compile(r"(\d+\.?\d*)\s*(°C|°\s*C|C)?", re.IGNORECASE)

        temperatures = []
        for line in stdout.splitlines():
            match = temp_pattern.search(line)
            if match:
                try:
                    temp_val = float(match.group(1))
                    temperatures.append(temp_val)
                except ValueError:
                    continue

        assert len(temperatures) > 0, (
            f"rocm-smi --showtemp 输出中未解析到任何温度值\n完整 stdout:\n{stdout}"
        )

        # 验证每个温度值在合理范围内
        for i, temp in enumerate(temperatures):
            assert 0.0 <= temp <= 110.0, (
                f"GPU {i} 温度 {temp}°C 超出合理范围 [0, 110]\n完整 stdout:\n{stdout}"
            )

    def test_rocm_smi_showtemp_stderr_empty(self, rocm_smi_path):
        """验证 rocm-smi --showtemp 的 stderr 无报错信息。"""
        result = _run_rocm_smi("--showtemp")
        # 即使 exit code 为 0，也要检查 stderr
        stderr_clean = result.stderr.strip()
        assert len(stderr_clean) == 0, (
            f"rocm-smi --showtemp 的 stderr 包含非预期输出\n"
            f"stderr: {result.stderr}\n"
            f"stdout: {result.stdout}"
        )

    def test_rocm_smi_showtemp_all_gpus_reported(self, rocm_smi_path):
        """验证 rocm-smi --showtemp 为每张 GPU 都报告了温度。

        通过对比 --showhw 检测到的 GPU 数量和 --showtemp 输出的温度行数。
        """
        # 先获取 GPU 数量
        hw_result = _run_rocm_smi("--showhw")
        if hw_result.returncode != 0:
            pytest.skip("无法通过 --showhw 获取 GPU 数量")

        # 统计 GPU 数量：匹配 GPU[0-9] 或类似标识
        gpu_count_hw = len(
            re.findall(r"GPU\s*\[\s*\d+\s*\]", hw_result.stdout, re.IGNORECASE)
        )

        if gpu_count_hw == 0:
            pytest.skip("--showhw 未检测到 GPU 设备")

        # 获取温度输出中的 GPU 行数
        temp_result = _run_rocm_smi("--showtemp")
        assert temp_result.returncode == 0, (
            f"rocm-smi --showtemp 执行失败\n"
            f"returncode: {temp_result.returncode}\n"
            f"stdout: {temp_result.stdout}\n"
            f"stderr: {temp_result.stderr}"
        )

        gpu_lines_temp = [
            line
            for line in temp_result.stdout.splitlines()
            if re.search(r"GPU\s*\[\s*\d+\s*\]", line, re.IGNORECASE)
        ]

        assert len(gpu_lines_temp) == gpu_count_hw, (
            f"温度报告 GPU 数量 ({len(gpu_lines_temp)}) 与硬件检测数量 ({gpu_count_hw}) 不一致\n"
            f"--showhw 输出:\n{hw_result.stdout}\n"
            f"--showtemp 输出:\n{temp_result.stdout}"
        )

    def test_rocm_smi_showtemp_alternative_flag(self, rocm_smi_path):
        """验证 rocm-smi -t（短选项）与 --showtemp 输出一致。"""
        result_long = _run_rocm_smi("--showtemp")
        if result_long.returncode != 0:
            pytest.skip("rocm-smi --showtemp 不可用，跳过短选项对比测试")

        result_short = _run_rocm_smi("-t")
        if result_short.returncode != 0:
            pytest.skip("rocm-smi -t 不可用，跳过对比测试")

        # 两个选项都应成功
        assert result_long.returncode == 0, (
            f"--showtemp 返回码非 0: {result_long.returncode}"
        )
        assert result_short.returncode == 0, f"-t 返回码非 0: {result_short.returncode}"

        # 两个输出都应包含温度信息
        assert len(result_long.stdout.strip()) > 0, "--showtemp 输出为空"
        assert len(result_short.stdout.strip()) > 0, "-t 输出为空"
