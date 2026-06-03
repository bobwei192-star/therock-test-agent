.PHONY: help install serve test test-unit test-integration lint format clean clean-state clean-all clean-frontend chat chat-restart gen mock-gen get-assistant-id

VENV := .venv/bin
PYTHON := $(VENV)/python
PIP := $(VENV)/pip
PYTEST := PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 $(VENV)/python -m pytest

help:
	@echo 'TestCaseAgent Makefile'
	@echo ''
	@echo '  make install         安装项目依赖 (pip install -e .)'
	@echo '  make serve           启动 langgraph dev 开发服务器'
	@echo '  make chat            启动 Assistant UI (npm run dev)'
	@echo '  make chat-restart    清理前端缓存并重启前端服务'
	@echo '  make test            运行全部单元测试'
	@echo '  make test-integration 运行集成测试 (需要 langgraph dev)'
	@echo '  make test-all        运行所有测试'
	@echo '  make lint            代码检查 (ruff)'
	@echo '  make format          代码格式化 (ruff)'
	@echo '  make clean           清理缓存和输出'
	@echo '  make clean-state     清理 LangGraph 状态存储'
	@echo '  make clean-frontend  清理前端缓存'
	@echo '  make clean-all       清理所有缓存（包括状态）'
	@echo '  make smoke           冒烟测试 (需要配置 LLM 密钥)'
	@echo '  make gen             生成测试用例 (CLI, 需要 LLM API)'
	@echo '  make mock-gen        生成测试用例 (Mock, 无需 LLM API)'
	@echo '  make get-assistant-id 获取 assistant_id 并更新前端配置'

install:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

serve:
	. $(VENV)/activate && langgraph dev

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

clean-state:
	@echo "🧹 清理 LangGraph 状态存储..."
	@echo "   停止后端进程..."
	pkill -f "langgraph" 2>/dev/null || true
	@sleep 2
	@echo "   删除持久化存储文件..."
	rm -rf .langgraph_api/ 2>/dev/null || true
	@echo "   清理前端缓存..."
	rm -rf etc/agent-chat-ui/.next/* 2>/dev/null || true
	@echo "✅ 状态已清理，请重新启动后端服务 (make serve)"

clean-all: clean clean-state

clean-frontend:
	@echo "🧹 清理前端缓存..."
	rm -rf etc/agent-chat-ui/.next/cache/* 2>/dev/null || true
	rm -rf etc/agent-chat-ui/.next/* 2>/dev/null || true
	@echo "✅ 前端缓存已清理"

chat-restart: clean-frontend
	@echo "🔄 重启前端服务..."
	pkill -f "next dev" 2>/dev/null || true
	sleep 1
	export PATH="$(PWD)/.node/bin:$${PATH}" && cd etc/agent-chat-ui && nohup pnpm dev > /dev/null 2>&1 &
	@echo "✅ 前端服务已重启"

gen:
	$(PYTHON) -m src.agent.cli run "写一个pytest测试用例，测试rocm-smi指令的存在性和正确性"

mock-gen:
	@echo "🔧 Mock mode — 使用预设 LLM 响应，无需 API 密钥"
	$(PYTHON) -m src.agent.mock_gen

chat:
	export PATH="$(PWD)/.node/bin:$${PATH}" && cd etc/agent-chat-ui && pnpm dev

get-assistant-id:
	@echo "🔍 获取 assistant_id..."
	@ASSISTANT_ID=$$(curl -s -X POST http://localhost:2024/assistants/search \
		-H "Content-Type: application/json" \
		-d '{}' | $(PYTHON) -c "import sys,json; print(json.load(sys.stdin)[0].get('assistant_id',''))"); \
	if [ -z "$$ASSISTANT_ID" ] || [ "$$ASSISTANT_ID" = "null" ]; then \
		echo "❌ 无法获取 assistant_id，请确保后端服务正在运行 (make serve)"; \
	else \
		echo "✅ assistant_id: $$ASSISTANT_ID"; \
		echo ""; \
		echo "📝 更新前端配置..."; \
		sed -i "s/^NEXT_PUBLIC_ASSISTANT_ID=.*/NEXT_PUBLIC_ASSISTANT_ID=$$ASSISTANT_ID/" etc/agent-chat-ui/.env; \
		echo "✅ 已更新 etc/agent-chat-ui/.env"; \
		echo ""; \
		echo "🔄 请重启前端服务: make clean-frontend && make chat"; \
	fi

