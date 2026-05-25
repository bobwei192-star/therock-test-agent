"""策略模式执行器 - 根据意图选择执行策略

根据 guide/09_promot优化.md 设计：
- PytestStrategy: 执行 pytest 测试
- DockerBuildStrategy: 执行 docker build
- ExternalRunStrategy: 执行外部套件
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from ..intent_router import IntentType


class ExecutionStrategy(ABC):
    """执行策略接口"""

    @abstractmethod
    def execute(self, artifact_path: str, state: Dict[str, Any]) -> Dict[str, Any]:
        """执行策略

        Args:
            artifact_path: 生成的产物路径（test_xxx.py 或 Dockerfile）
            state: 当前状态

        Returns:
            执行结果
        """
        pass


class PytestStrategy(ExecutionStrategy):
    """Pytest 测试执行策略"""

    def execute(self, artifact_path: str, state: Dict[str, Any]) -> Dict[str, Any]:
        import subprocess
        import tempfile
        import os

        print(f"[策略执行] 使用 PytestStrategy 执行: {artifact_path}")

        # 创建临时目录用于执行
        with tempfile.TemporaryDirectory() as tmp_dir:
            # 复制测试文件到临时目录
            test_filename = os.path.basename(artifact_path)
            dest_path = os.path.join(tmp_dir, test_filename)
            
            try:
                with open(artifact_path, 'r') as src, open(dest_path, 'w') as dst:
                    dst.write(src.read())
            except Exception as e:
                return {"status": "failed", "errors": [f"无法读取测试文件: {e}"]}

            # 执行 pytest
            try:
                result = subprocess.run(
                    ["python", "-m", "pytest", dest_path, "-v", "--tb=short"],
                    cwd=tmp_dir,
                    capture_output=True,
                    text=True,
                    timeout=120
                )
                return {
                    "status": "success" if result.returncode == 0 else "failed",
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "returncode": result.returncode
                }
            except subprocess.TimeoutExpired:
                return {"status": "failed", "errors": ["测试执行超时"]}
            except Exception as e:
                return {"status": "failed", "errors": [f"执行失败: {e}"]}


class DockerBuildStrategy(ExecutionStrategy):
    """Docker 构建策略"""

    def execute(self, artifact_path: str, state: Dict[str, Any]) -> Dict[str, Any]:
        import subprocess
        import re

        print(f"[策略执行] 使用 DockerBuildStrategy 构建: {artifact_path}")

        try:
            # 提取镜像标签（从状态或文件名）
            image_tag = state.get("image_tag", "rocm-test:latest")
            
            # 执行 docker build
            result = subprocess.run(
                ["docker", "build", "-f", artifact_path, "-t", image_tag, "."],
                capture_output=True,
                text=True,
                timeout=300
            )

            # 提取镜像标签
            image_tag_output = image_tag
            if result.returncode == 0:
                # 尝试从输出中提取镜像 ID
                match = re.search(r'Successfully built (\w+)', result.stdout)
                if match:
                    image_tag_output = f"{image_tag} ({match.group(1)})"

            return {
                "status": "success" if result.returncode == 0 else "failed",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
                "image_tag": image_tag_output
            }
        except subprocess.TimeoutExpired:
            return {"status": "failed", "errors": ["Docker 构建超时"]}
        except Exception as e:
            return {"status": "failed", "errors": [f"Docker 构建失败: {e}"]}


class ExternalRunStrategy(ExecutionStrategy):
    """外部套件执行策略"""

    def execute(self, artifact_path: str, state: Dict[str, Any]) -> Dict[str, Any]:
        import subprocess

        print(f"[策略执行] 使用 ExternalRunStrategy 执行: {artifact_path}")

        try:
            # 执行外部脚本/命令
            result = subprocess.run(
                ["bash", artifact_path],
                capture_output=True,
                text=True,
                timeout=300
            )

            return {
                "status": "success" if result.returncode == 0 else "failed",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
                "report": result.stdout[:2000] if result.stdout else ""
            }
        except subprocess.TimeoutExpired:
            return {"status": "failed", "errors": ["外部执行超时"]}
        except Exception as e:
            return {"status": "failed", "errors": [f"外部执行失败: {e}"]}


class StrategyFactory:
    """策略工厂 - 根据意图获取执行策略"""

    _strategies: Dict[IntentType, ExecutionStrategy] = {
        "GENERATE": PytestStrategy(),
        "APPEND": PytestStrategy(),
        "UPDATE": PytestStrategy(),
        "REFACTOR": PytestStrategy(),
        "ENV_BUILD": DockerBuildStrategy(),
        "EXECUTE_EXTERNAL": ExternalRunStrategy(),
        # DIAGNOSE/COVERAGE/PROBE 不需要执行策略（查询类）
        "DIAGNOSE": PytestStrategy(),  # 默认策略，实际不会被调用
        "COVERAGE": PytestStrategy(),
        "PROBE": PytestStrategy(),
    }

    @classmethod
    def get_strategy(cls, intent: IntentType) -> ExecutionStrategy:
        """根据意图获取执行策略

        Args:
            intent: 意图类型

        Returns:
            对应的执行策略
        """
        return cls._strategies.get(intent, PytestStrategy())

    @classmethod
    def register_strategy(cls, intent: IntentType, strategy: ExecutionStrategy) -> None:
        """注册自定义策略

        Args:
            intent: 意图类型
            strategy: 执行策略实例
        """
        cls._strategies[intent] = strategy


def execute_with_strategy(intent: IntentType, artifact_path: str, 
                          state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """使用策略模式执行

    Args:
        intent: 意图类型
        artifact_path: 生成的产物路径
        state: 当前状态（可选）

    Returns:
        执行结果
    """
    if state is None:
        state = {}

    strategy = StrategyFactory.get_strategy(intent)
    return strategy.execute(artifact_path, state)