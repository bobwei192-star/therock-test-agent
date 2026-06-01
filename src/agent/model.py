"""LLM 模型配置与构建模块 —— 支持多 Provider 的统一接口

本模块提供：
1. ModelConfig: 模型配置数据类，封装所有必需的连接参数
2. build_model_config(): 从环境变量构建配置对象
3. build_model(): 创建 ChatOpenAI 兼容的模型实例

支持的 Provider：
- amd: AMD 内部 LLM 服务
- deepseek: DeepSeek 云服务
- openai: OpenAI 官方服务
- ark: 火山方舟
- yuanyuai: 元语 AI
- generic: 通用 OpenAI 兼容接口

配置方式：
1. 设置环境变量 TEST_CASE_AGENT_MODEL_PROVIDER 指定 Provider
2. 根据 Provider 设置对应的 API 密钥和其他参数
3. 支持通过 .env 文件加载配置
"""

import os
from dataclasses import dataclass

from langchain_openai import ChatOpenAI


@dataclass(frozen=True)
class ModelConfig:
    """OpenAI 兼容的聊天模型配置。

    Attributes:
        model: 模型名称（如 gpt-4o, deepseek-chat）
        base_url: API 基础 URL
        api_key: API 密钥
        temperature: 温度参数，控制输出随机性（0-2）
        subscription_key: 订阅密钥（部分 Provider 需要，如 AMD）
        user: 用户标识（用于计费和追踪）
    """

    model: str
    base_url: str
    api_key: str
    temperature: float = 0.2
    subscription_key: str | None = None
    user: str | None = None


def _optional_load_dotenv() -> None:
    """当 python-dotenv 安装时，尝试从 .env 文件加载环境变量。"""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    load_dotenv()


def build_model_config(provider: str | None = None) -> ModelConfig:
    """从环境变量构建模型配置。

    Args:
        provider: 模型 Provider 名称，支持: amd, deepseek, openai, ark, yuanyuai, generic
                  如果未指定，从 TEST_CASE_AGENT_MODEL_PROVIDER 环境变量读取，默认 amd

    Returns:
        ModelConfig 配置对象，供 build_model() 使用

    Raises:
        RuntimeError: 当所选 Provider 缺少必需的凭证时
    """
    _optional_load_dotenv()
    
    # 确定 Provider
    selected_provider = (
        provider
        or os.environ.get("TEST_CASE_AGENT_MODEL_PROVIDER")
        or os.environ.get("LLM_PROVIDER")
    )
    if not selected_provider:
        selected_provider = "amd"
    selected_provider = selected_provider.lower()

    # DeepSeek Provider
    if selected_provider == "deepseek":
        api_key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("LLM_API_KEY")
        if not api_key:
            raise RuntimeError("缺少 DEEPSEEK_API_KEY 或 LLM_API_KEY 环境变量")
        return ModelConfig(
            model=(
                os.environ.get("DEEPSEEK_MODEL")
                or os.environ.get("LLM_MODEL_ID")
                or os.environ.get("LLM_MODEL")
                or "deepseek-chat"
            ),
            base_url=os.environ.get("DEEPSEEK_BASE_URL")
            or os.environ.get("LLM_BASE_URL")
            or "https://api.deepseek.com/v1",
            api_key=api_key,
            temperature=float(os.environ.get("LLM_TEMPERATURE", "0.2")),
        )

    # AMD Provider
    if selected_provider == "amd":
        subscription_key = os.environ.get("AMD_LLM_SUBSCRIPTION_KEY")
        if not subscription_key:
            raise RuntimeError("缺少 AMD_LLM_SUBSCRIPTION_KEY 环境变量")
        return ModelConfig(
            model=os.environ.get("AMD_LLM_MODEL", "GPT55"),
            base_url=os.environ.get(
                "AMD_LLM_BASE_URL", "https://llm-api.amd.com/OnPrem"
            ),
            api_key=os.environ.get("AMD_LLM_API_KEY", "dummy"),
            temperature=float(os.environ.get("LLM_TEMPERATURE", "0.2")),
            subscription_key=subscription_key,
            user=os.environ.get("AMD_LLM_USER") or os.environ.get("USER"),
        )

    # OpenAI Provider
    if selected_provider == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("缺少 OPENAI_API_KEY 环境变量")
        return ModelConfig(
            model=os.environ.get("OPENAI_MODEL", "gpt-4o"),
            base_url=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"),
            api_key=api_key,
            temperature=float(os.environ.get("LLM_TEMPERATURE", "0.2")),
        )

    # 火山方舟 Provider
    if selected_provider == "ark":
        api_key = os.environ.get("ARK_API_KEY")
        if not api_key:
            raise RuntimeError("缺少 ARK_API_KEY 环境变量")
        return ModelConfig(
            model=os.environ.get("ARK_MODEL", "deepseek-v3-2-251201"),
            base_url=os.environ.get("ARK_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3"),
            api_key=api_key,
            temperature=float(os.environ.get("LLM_TEMPERATURE", "0.2")),
        )

    # 元语 AI Provider
    if selected_provider == "yuanyuai":
        api_key = os.environ.get("YUNYUAI_API_KEY")
        if not api_key:
            raise RuntimeError("缺少 YUNYUAI_API_KEY 环境变量")
        return ModelConfig(
            model=os.environ.get("YUNYUAI_MODEL", "kimi-k2.6"),
            base_url=os.environ.get("YUNYUAI_BASE_URL", "https://yuanyuaicloud.cn/v1"),
            api_key=api_key,
            temperature=float(os.environ.get("LLM_TEMPERATURE", "0.2")),
        )

    # 通用 Provider（需要手动指定所有参数）
    api_key = os.environ.get("LLM_API_KEY")
    base_url = os.environ.get("LLM_BASE_URL")
    model = os.environ.get("LLM_MODEL")
    if not api_key or not base_url or not model:
        raise RuntimeError(
            "通用 Provider 需要设置 LLM_API_KEY、LLM_BASE_URL 和 LLM_MODEL 环境变量"
        )
    return ModelConfig(
        model=model,
        base_url=base_url,
        api_key=api_key,
        temperature=float(os.environ.get("LLM_TEMPERATURE", "0.2")),
    )


def build_model(provider: str | None = None):
    """从环境变量创建 ChatOpenAI 兼容的模型实例。

    Args:
        provider: 模型 Provider 名称（可选）

    Returns:
        ChatOpenAI 实例，可直接用于 LLM 调用
    """
    config = build_model_config(provider=provider)
    
    # 构建自定义请求头（用于 AMD 等需要额外认证的 Provider）
    default_headers = None
    if config.subscription_key:
        default_headers = {
            "Ocp-Apim-Subscription-Key": config.subscription_key,
        }
        if config.user:
            default_headers["user"] = config.user

    # 创建并返回 ChatOpenAI 实例
    return ChatOpenAI(
        model=config.model,
        base_url=config.base_url,
        api_key=config.api_key,
        temperature=config.temperature,
        default_headers=default_headers,
        request_timeout=int(os.environ.get("LLM_REQUEST_TIMEOUT", "120")),
        max_retries=int(os.environ.get("LLM_MAX_RETRIES", "2")),
    )
