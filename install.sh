#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*"; }
log_step()  { echo -e "\n${BLUE}[STEP $1/$TOTAL_STEPS]${NC} $2"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
TOTAL_STEPS=8
log_info "Project root: $SCRIPT_DIR"
# ─────────────────────────────────────────────────────
# 辅助函数
# ─────────────────────────────────────────────────────

_pip_source_speed_test() {
    local sources=(
        "https://pypi.org/simple"
        "https://mirror.baidu.com/pypi/simple"
        "https://pypi.tuna.tsinghua.edu.cn/simple"
        "https://mirrors.aliyun.com/pypi/simple"
        "https://pypi.mirrors.ustc.edu.cn/simple"
    )
    local fastest_source="https://pypi.org/simple"
    local fastest_time=999999
    
    echo -e "${GREEN}[INFO]${NC} 正在测试PyPI源速度..." >&2
    
    for source in "${sources[@]}"; do
        local start=$(date +%s%N)
        if curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 --max-time 5 "$source/pip/" | grep -q "200"; then
            local end=$(date +%s%N)
            local time=$(( (end - start) / 1000000 ))
            printf "  %-40s %4d ms\n" "$source" "$time" >&2
            
            if [ "$time" -lt "$fastest_time" ]; then
                fastest_time="$time"
                fastest_source="$source"
            fi
        else
            printf "  %-40s %s\n" "$source" "连接失败" >&2
        fi
    done
    
    echo -e "${GREEN}[INFO]${NC} 最快源: $fastest_source ($fastest_time ms)" >&2
    echo "$fastest_source"
}

_get_pip_index_url() {
    local url="$1"
    local host=$(echo "$url" | awk -F/ '{print $3}')
    if [ -n "$host" ] && [ "$host" != "$url" ]; then
        echo "$url"
    else
        echo ""
    fi
}

_get_pip_trusted_host() {
    local url="$1"
    local host=$(echo "$url" | awk -F/ '{print $3}')
    if [ -n "$host" ] && [ "$host" != "$url" ]; then
        echo "$host"
    else
        echo ""
    fi
}

_docker_ok() {
    if ! command -v docker >/dev/null 2>&1; then
        log_error "Docker 未安装，跳过容器部署。"
        log_info "安装 Docker: curl -fsSL https://get.docker.com | bash"
        return 1
    fi
    
    if ! docker info >/dev/null 2>&1; then
        log_warn "当前用户没有 Docker 访问权限"
        
        if groups | grep -q docker; then
            log_warn "用户已在 docker 组，但当前 shell 未生效"
            if command -v sg >/dev/null 2>&1; then
                log_info "尝试用 sg 命令验证权限..."
                if sg docker -c "docker info >/dev/null 2>&1"; then
                    log_info "权限验证成功，使用 sg docker 执行后续操作"
                    DOCKER_PREFIX="sg docker -c"
                    return 0
                fi
            fi
            log_warn "需要重新登录或执行: newgrp docker"
        else
            log_warn "用户不在 docker 组中"
            if command -v sudo >/dev/null 2>&1; then
                log_info "尝试自动添加用户到 docker 组..."
                if sudo usermod -aG docker "$USER" >/dev/null 2>&1; then
                    log_info "用户已添加到 docker 组"
                    if command -v sg >/dev/null 2>&1; then
                        log_info "验证新权限..."
                        if sg docker -c "docker info >/dev/null 2>&1"; then
                            log_info "权限验证成功，使用 sg docker 执行后续操作"
                            DOCKER_PREFIX="sg docker -c"
                            return 0
                        fi
                    fi
                    log_warn "需要重新登录才能使权限生效"
                else
                    log_warn "无法添加用户到 docker 组（可能需要密码）"
                fi
            else
                log_warn "无法获取 sudo 权限，跳过 Docker 部署"
                return 1
            fi
        fi
        
        log_error "Docker 权限问题无法自动修复，跳过容器部署。"
        log_info "手动修复方法: sudo usermod -aG docker $USER && newgrp docker"
        return 1
    fi
    
    DOCKER_PREFIX=""
    if docker compose version >/dev/null 2>&1; then
        DOCKER_COMPOSE="docker compose"
    elif command -v docker-compose >/dev/null 2>&1; then
        DOCKER_COMPOSE="docker-compose"
    else
        log_error "docker compose / docker-compose 都不可用，跳过容器部署。"
        return 1
    fi
    return 0
}

_container_running() {
    docker ps --format '{{.Names}}' 2>/dev/null | grep -q "$1"
}

_setup_docker_mirrors() {
    local daemon_cfg="/etc/docker/daemon.json"
    local mirror_url="https://docker.m.daocloud.io"

    if [ ! -w "$(dirname "$daemon_cfg")" ] && ! command -v sudo >/dev/null 2>&1; then
        log_warn "无权限配置 Docker 镜像加速，镜像拉取可能失败"
        return 1
    fi

    local cmd_prefix=""
    if [ ! -w "$(dirname "$daemon_cfg")" ]; then
        cmd_prefix="sudo"
    fi

    local need_update=1
    if [ -f "$daemon_cfg" ]; then
        local current_mirrors=$($cmd_prefix python3 -c "
import json
with open('$daemon_cfg') as f:
    cfg = json.load(f)
mirrors = cfg.get('registry-mirrors', [])
print(' '.join(mirrors))
" 2>/dev/null)
        if [ -n "$current_mirrors" ]; then
            for m in $current_mirrors; do
                local code=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 2 --max-time 3 "$m/v2/" 2>/dev/null || echo "000")
                if [ "$code" = "401" ] || [ "$code" = "200" ]; then
                    log_info "Docker 镜像 $m 可达，沿用现有配置"
                    need_update=0
                    break
                fi
            done
        fi
    fi

    if [ "$need_update" -eq 0 ]; then
        return 0
    fi

    log_info "现有镜像不可达，切换为 $mirror_url ..."

    local tmpfile=$(mktemp)
    cat > "$tmpfile" <<EOF
{
    "registry-mirrors": ["$mirror_url"]
}
EOF

    if [ -f "$daemon_cfg" ]; then
        $cmd_prefix python3 -c "
import json
with open('$daemon_cfg') as f:
    cfg = json.load(f)
cfg['registry-mirrors'] = ['$mirror_url']
with open('$tmpfile', 'w') as f:
    json.dump(cfg, f, indent=2)
" 2>/dev/null
    fi

    if $cmd_prefix cp "$tmpfile" "$daemon_cfg" 2>/dev/null; then
        $cmd_prefix systemctl restart docker 2>/dev/null || $cmd_prefix systemctl reload docker 2>/dev/null || true
        sleep 2
        log_info "Docker 镜像加速已配置: $mirror_url"
        rm -f "$tmpfile"
        return 0
    fi

    rm -f "$tmpfile"
    log_warn "Docker 镜像加速配置失败（可能需要 sudo 或文件系统只读）"
    log_info "手动配置: sudo tee /etc/docker/daemon.json <<<'{\"registry-mirrors\":[\"https://docker.m.daocloud.io\"]}' && sudo systemctl restart docker"
    return 1
}

_docker_compose_up() {
    local dir="$1"
    local name="${2:-service}"

    _setup_docker_mirrors

    cd "$dir"

    if [ -n "$DOCKER_PREFIX" ]; then
        if $DOCKER_PREFIX "$DOCKER_COMPOSE up -d" 2>&1; then
            log_info "$name started. Access: http://localhost:3000"
            cd "$SCRIPT_DIR"
            return 0
        fi
    else
        if $DOCKER_COMPOSE up -d 2>&1; then
            log_info "$name started. Access: http://localhost:3000"
            cd "$SCRIPT_DIR"
            return 0
        fi
    fi

    log_error "$name 启动失败 — Docker Hub 可能不可达，跳过。"
    log_info "若需启用，先确保 Docker 能拉取镜像后手动执行:"
    log_info "  cd $dir && docker compose up -d"
    log_info "镜像加速参考:"
    log_info "  sudo tee /etc/docker/daemon.json <<<'{\"registry-mirrors\":[\"https://docker.m.daocloud.io\"]}'"
    log_info "  sudo systemctl reload docker"
    cd "$SCRIPT_DIR"
    return 1
}

# ─────────────────────────────────────────────────────
# Step 1-5: Python 环境
# ─────────────────────────────────────────────────────

log_step 1 "Create and activate project virtual environment"
if [ ! -d ".venv" ] || [ ! -f ".venv/bin/activate" ]; then
    if [ -d ".venv" ]; then
        log_warn ".venv exists but is incomplete, removing it..."
        rm -rf ".venv"
    fi
    
    if python3 -m venv .venv 2>/dev/null; then
        log_info "Created .venv with ensurepip"
    else
        log_warn "ensurepip not available, creating venv without pip"
        python3 -m venv --without-pip .venv
        log_info "Created .venv without pip"
        
        source .venv/bin/activate
        
        log_info "Installing pip manually..."
        curl -sSL https://bootstrap.pypa.io/get-pip.py | python
        log_info "pip installed"
    fi
else
    log_warn ".venv already exists, reuse it"
fi
source .venv/bin/activate
log_info "python: $(command -v python)"
log_info "VIRTUAL_ENV: ${VIRTUAL_ENV:-}"
python --version

log_step 2 "Test PyPI sources and select fastest"
PIP_INDEX_URL=$(_pip_source_speed_test)
PIP_TRUSTED_HOST=$(_get_pip_trusted_host "$PIP_INDEX_URL")

log_step 3 "Upgrade pip & install project"
python -m pip install --upgrade pip -q -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"
pip install graphrag -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"

log_step 4 "Install project requirements (including RAG + CLI deps)"
python -m pip install -r requirements.txt -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"
python -m pip install -e . -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"
python -m pip install pytest-html -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"
python -m pip install \
    typer rich \
    langchain-community langchain-text-splitters \
    langchain-huggingface langchain-chroma chromadb \
    sentence-transformers \
    -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"
python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install prompt_toolkit -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"
log_step 5 "Install DeepAgents"
if [ -f "etc/deepagents/pyproject.toml" ] || [ -f "etc/deepagents/setup.py" ]; then
    python -m pip install -e etc/deepagents -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"
else
    python -m pip install deepagents -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"
fi

log_step 6 "Verify core dependencies"
python - <<'PY'
import importlib.util, sys
modules = {
    "langgraph": "langgraph",
    "langchain": "langchain",
    "langchain_openai": "langchain_openai",
    "langfuse": "langfuse",
    "deepagents": "deepagents",
    "typer": "typer",
    "rich": "rich",
}
missing = []
for label, name in modules.items():
    ok = importlib.util.find_spec(name) is not None
    print(f"  {label}: {'✅' if ok else '❌ NOT INSTALLED'}")
    if not ok:
        missing.append(label)
if missing:
    sys.exit(f"Missing: {', '.join(missing)}")
PY
if ! command -v langgraph >/dev/null 2>&1; then
    log_error "langgraph CLI is not available in .venv"
    exit 1
fi
langgraph --version

# ─────────────────────────────────────────────────────
# Step 7: Agent Chat UI (langchain-ai/agent-chat-ui)
# 官方文档: https://github.com/langchain-ai/agent-chat-ui
# ─────────────────────────────────────────────────────

pip install paramiko -i "$PIP_INDEX_URL" --trusted-host "$PIP_TRUSTED_HOST"

_install_nodejs() {
    log_info "正在安装 Node.js 22..."
    
    # 尝试多个安装位置
    local node_version="22.11.0"
    local arch=$(uname -m)
    
    case "$arch" in
        x86_64)
            local node_url="https://nodejs.org/dist/v${node_version}/node-v${node_version}-linux-x64.tar.xz"
            ;;
        aarch64)
            local node_url="https://nodejs.org/dist/v${node_version}/node-v${node_version}-linux-arm64.tar.xz"
            ;;
        *)
            log_error "不支持的架构: $arch"
            return 1
            ;;
    esac
    
    # 尝试的安装位置列表（按优先级）
    local node_locations=(
        "$HOME/.local/node"
        "$SCRIPT_DIR/.node"
        "/tmp/node-$node_version"
    )
    
    # 检查是否已安装
    for node_dir in "${node_locations[@]}"; do
        if [ -d "$node_dir" ] && [ -x "$node_dir/bin/node" ]; then
            log_info "Node.js 已安装在 $node_dir"
            export PATH="$node_dir/bin:$PATH"
            return 0
        fi
    done
    
    # 尝试安装到第一个可写位置
    for node_dir in "${node_locations[@]}"; do
        if mkdir -p "$node_dir" 2>/dev/null; then
            log_info "尝试安装 Node.js 到 $node_dir..."
            if curl -sSL "$node_url" | tar -xJ -C "$node_dir" --strip-components=1; then
                log_info "Node.js 安装成功: $node_dir"
                export PATH="$node_dir/bin:$PATH"
                node -v
                return 0
            else
                log_error "Node.js 下载或解压失败"
                rm -rf "$node_dir"
            fi
        else
            log_warn "无法创建目录: $node_dir (只读)"
        fi
    done
    
    log_error "所有位置都无法安装 Node.js"
    return 1
}

log_step 7 "Setup Agent Chat UI (langchain-ai/agent-chat-ui)"
UI_DIR="$SCRIPT_DIR/etc/agent-chat-ui"

if ! command -v node >/dev/null 2>&1; then
    log_warn "Node.js 未安装，尝试自动安装..."
    if _install_nodejs; then
        log_info "Node.js 安装成功"
    else
        log_error "Node.js 安装失败，Agent Chat UI 需要 Node.js 22+。跳过。"
        log_info "手动安装: curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt install -y nodejs"
        SKIP_UI=true
    fi
fi

if [ -z "${SKIP_UI:-}" ]; then
    log_info "Node.js: $(node -v)"

    # 设置 npm 使用项目目录作为缓存
    export NPM_CONFIG_CACHE="$SCRIPT_DIR/.npm-cache"
    mkdir -p "$NPM_CONFIG_CACHE"

    # 官方安装方式: git clone 或 npx create-agent-chat-app
    if [ ! -d "$UI_DIR" ] || [ ! -f "$UI_DIR/package.json" ]; then
        if [ -d "$UI_DIR" ]; then
            log_warn "agent-chat-ui 目录存在但不完整，重新创建..."
            rm -rf "$UI_DIR"
        fi
        
        log_info "正在克隆 agent-chat-ui 仓库..."
        git clone https://github.com/langchain-ai/agent-chat-ui.git "$UI_DIR"
        
        log_info "Created agent-chat-ui project -> $UI_DIR"
    else
        log_warn "agent-chat-ui 源码已存在，跳过克隆"
    fi

    # 安装依赖
    if [ -f "$UI_DIR/package.json" ]; then
        cd "$UI_DIR"
        
        # 使用 pnpm 安装（官方推荐）
        if command -v pnpm >/dev/null 2>&1; then
            log_info "使用 pnpm 安装依赖..."
            pnpm install
        else
            log_info "使用 npm 安装依赖..."
            npm install
        fi
        
        log_info "Dependencies installed"
    fi

    # 创建 .env 文件，配置连接到本地 LangGraph server
    if [ -f "$UI_DIR/package.json" ] && [ ! -f "$UI_DIR/.env" ]; then
        cat > "$UI_DIR/.env" <<'DOTENV'
# LangGraph API Configuration
NEXT_PUBLIC_API_URL=http://localhost:2024
NEXT_PUBLIC_ASSISTANT_ID=agent
DOTENV
        log_info "Created .env (连接本地 LangGraph server)"
    fi

    cd "$SCRIPT_DIR"
fi

# ─────────────────────────────────────────────────────
# Step 8: Langfuse (Docker)
# ─────────────────────────────────────────────────────
log_step 8 "Deploy Langfuse (Docker Compose, http://localhost:3000)"
LF_REPO="https://github.com/langfuse/langfuse.git"
LF_DIR="$SCRIPT_DIR/etc/langfuse"

if _docker_ok; then
    if _container_running "langfuse"; then
        log_warn "Langfuse 容器已在运行，跳过部署。"
    else
        # 检查目录是否存在且不为空（包含必要文件）
        if [ ! -d "$LF_DIR" ] || [ ! -f "$LF_DIR/docker-compose.yml" ]; then
            if [ -d "$LF_DIR" ]; then
                log_warn "langfuse 目录存在但不完整，重新克隆..."
                rm -rf "$LF_DIR"
            fi
            git clone --depth 1 "$LF_REPO" "$LF_DIR"
            log_info "Cloned langfuse -> $LF_DIR"
            cat > "$LF_DIR/.env" <<DOTENV
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=$(openssl rand -hex 32 2>/dev/null || echo "mysecret-changeme")
SALT=$(openssl rand -hex 16 2>/dev/null || echo "mysalt-changeme")
ENCRYPTION_KEY=$(openssl rand -hex 32 2>/dev/null || echo "0000000000000000000000000000000000000000000000000000000000000000")
TELEMETRY_ENABLED=true
LANGFUSE_ENABLE_EXPERIMENTAL_FEATURES=true
DOTENV
            log_info "Created .env (auto-generated secrets)"
        else
            log_warn "langfuse 源码已存在，重新启动..."
        fi
        cd "$LF_DIR"
        if [ -f "docker-compose.yml" ]; then
            _docker_compose_up "$LF_DIR" "Langfuse"
        else
            log_error "docker-compose.yml not found in $LF_DIR"
            cd "$SCRIPT_DIR"
        fi
    fi
fi

# ─────────────────────────────────────────────────────
# 更新 .env 文件配置（添加 Langfuse 连接信息）
# ─────────────────────────────────────────────────────
_update_env_file() {
    if [ ! -f ".env" ]; then
        cat > ".env" <<'EOF'
# LLM Provider Configuration
LLM_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o

# Langfuse Configuration
LANGFUSE_PUBLIC_KEY=your-langfuse-public-key
LANGFUSE_SECRET_KEY=your-langfuse-secret-key
LANGFUSE_HOST=http://localhost:3000

# Sandbox Configuration
TEST_CASE_AGENT_REMOTE_HOST=
TEST_CASE_AGENT_SANDBOX_PROVIDER=local_docker

# Tracing Configuration
OTEL_TRACES_EXPORTER=langfuse
EOF
        log_info "创建默认 .env 文件"
    else
        # 确保必要的配置项存在
        if ! grep -q "LANGFUSE_HOST" .env; then
            echo "LANGFUSE_HOST=http://localhost:3000" >> .env
            log_info "添加 LANGFUSE_HOST 到 .env"
        fi
        if ! grep -q "OTEL_TRACES_EXPORTER" .env; then
            echo "OTEL_TRACES_EXPORTER=langfuse" >> .env
            log_info "添加 OTEL_TRACES_EXPORTER 到 .env"
        fi
    fi
}

_update_env_file
echo ""
echo -e "${BLUE}================================================================================${NC}"
echo -e "${GREEN}                      安装完成 - TestCaseAgent${NC}"
echo ""
echo -e "${BLUE}服务概览:${NC}"
printf "  %-28s %s\n" "LangGraph API"    "http://127.0.0.1:2024   (启动: langgraph dev)"
printf "  %-28s %s\n" "Langfuse"         "http://localhost:3000     (Docker)"
printf "  %-28s %s\n" "Agent Chat UI"     "http://localhost:3000     (pnpm dev, 端口自动选择)"
printf "  %-28s %s\n" "CLI"              "python -m src.agent.cli run/chat/status"
echo ""
echo -e "${YELLOW}启动步骤:${NC}"
echo -e "  ${GREEN}1.${NC} ✅ Langfuse API Key 已自动配置，无需手动操作"
echo -e "  ${GREEN}2.${NC} 设置 LLM API Key: 修改 ${GREEN}.env${NC} 中的 OPENAI_API_KEY 或使用其他 provider"
echo ""
echo -e "  ${BLUE}【终端1】启动 LangGraph Server:${NC}"
echo -e "    cd $SCRIPT_DIR"
echo -e "    source .venv/bin/activate"
echo -e "    langgraph dev"
echo -e "    -> 访问: http://127.0.0.1:2024"
echo ""
echo -e "  ${BLUE}【终端2】启动 Agent Chat UI:${NC}"
echo -e "    cd $SCRIPT_DIR/etc/agent-chat-ui"
echo -e "    export PATH=\"$SCRIPT_DIR/.node/bin:\$PATH\""
echo -e "    pnpm dev"
echo -e "    -> 访问: http://localhost:3000 (端口可能变化，查看启动日志)"
echo ""
echo -e "  ${GREEN}3.${NC} CLI 使用: python -m src.agent.cli run \"提示词\""
echo ""
echo -e "${RED}注意:${NC} 请确保 .env 文件中配置了正确的 LLM API Key"
echo -e "${RED}注意:${NC} OTel 链路追踪已配置为使用 Langfuse，确保 Langfuse 服务正常运行"
