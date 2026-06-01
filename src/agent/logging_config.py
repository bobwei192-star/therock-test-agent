#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Case Agent 的结构化日志配置模块（使用 structlog）。

本模块配置结构化日志系统，将日志输出到两个目标：
1. test_case_agent.log - JSON 格式的详细日志，用于调试和分析
2. 控制台 - 人类可读的日志格式，用于实时监控

使用示例：
    from src.agent.logging_config import get_logger
    logger = get_logger("my_module")
    logger.info("task_completed", task="test_generation", status="success", duration=12.5)
"""

import os
import sys
import json
import logging
from pathlib import Path

import structlog

# Log file location (in project root)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_FILE = PROJECT_ROOT / "test_case_agent.log"


def configure_logging(level: str = "INFO") -> None:
    """Configure structlog for structured logging (compatible with structlog 25.x)."""
    
    # Set log level from environment or parameter
    log_level = os.environ.get("LOG_LEVEL", level).upper()
    
    # Configure structlog with stdlib integration
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
    )
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    # Remove default handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Console handler (human-readable)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_formatter = structlog.stdlib.ProcessorFormatter(
        processor=structlog.dev.ConsoleRenderer(colors=True),
    )
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    # File handler (JSON format)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(
        LOG_FILE,
        mode="a",
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)  # File gets all debug logs
    
    def json_processor(logger, method_name, event_dict):
        """Custom JSON processor with proper formatting."""
        event_dict["level"] = method_name.upper()
        return json.dumps(event_dict, ensure_ascii=False, indent=2, default=str)
    
    file_formatter = structlog.stdlib.ProcessorFormatter(
        processor=json_processor,
    )
    file_handler.setFormatter(file_formatter)
    root_logger.addHandler(file_handler)


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """Get a structured logger with the given name."""
    return structlog.get_logger(name)


# Initialize logging on module load
configure_logging()


# Example usage
if __name__ == "__main__":
    logger = get_logger("test")
    
    logger.debug("debug_message", key="value", number=42)
    logger.info("info_message", task="test", status="running")
    logger.warning("warning_message", warning="something might be wrong")
    logger.error("error_message", error="something went wrong", code=500)
    
    try:
        raise ValueError("Test exception")
    except ValueError:
        logger.exception("exception_occurred", context="test")
    
    print(f"Logs written to: {LOG_FILE}")
