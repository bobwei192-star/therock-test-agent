.PHONY: help install serve test test-unit test-integration lint format clean

VENV := .venv/bin
PYTHON := $(VENV)/python
PIP := $(VENV)/pip
PYTEST := $(VENV)/python -m pytest

help:
	@echo 'TestCaseAgent Makefile'
	@echo ''
	@echo '  make install         安装项目依赖 (pip install -e .)'
	@echo '  make serve           启动 langgraph dev 开发服务器'
	@echo '  make test            运行全部单元测试'
	@echo '  make test-integration 运行集成测试 (需要 langgraph dev)'
	@echo '  make test-all        运行所有测试'
	@echo '  make lint            代码检查 (ruff)'
	@echo '  make format          代码格式化 (ruff)'
	@echo '  make clean           清理缓存和输出'
	@echo '  make smoke           冒烟测试 (需要配置 LLM 密钥)'

install:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

serve:
	source $(VENV)/activate && langgraph dev

test:
	$(PYTEST) tests/unit -q

test-integration:
	$(PYTEST) tests/integration -q

test-all:
	$(PYTEST) tests/ -q

smoke:
	$(PYTEST) tests/integration/test_graph_smoke.py -v -s

lint:
	$(PYTHON) -m ruff check src tests

format:
	$(PYTHON) -m ruff format src tests

clean:
	rm -rf output/ .pytest_cache/ */**/__pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
