#!/bin/bash
# DeepAgents 多手段加速安装脚本（最终修复版）
# 放置位置: C:\Users\Tong\Desktop\Test_Case_Agent\install.sh
# 适用环境: WSL2 + Ubuntu 24.04 + NTFS 挂载盘
set -euo pipefail

# ---------- 颜色定义 ----------
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

log_info()  { echo -e "${GREEN}[INFO]${NC}  $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
log_error() { echo -e "${RED}[ERROR]${NC} $*"; }
log_step()  { echo -e "\n${BLUE}[STEP $1/7]${NC} $2"; }
log_cmd()   { echo -e "${CYAN}  → $*${NC}"; }

# ---------- 定位到 deepagents 子目录 ----------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/deepagents" || {
    log_error "找不到 deepagents 目录。请确保 install.sh 放在 Test_Case_Agent/ 目录下。"
    exit 1
}
log_info "工作目录: $(pwd)"

# ---------- 手段1: apt 换阿里云镜像 ----------
log_step 1 "配置 apt 国内镜像（阿里云）..."
UBUNTU_CODENAME=$(. /etc/os-release && echo "$VERSION_CODENAME")

if [ ! -f /etc/apt/sources.list.d/aliyun-noble.list ]; then
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak.$(date +%s) 2>/dev/null || true
    sudo tee /etc/apt/sources.list.d/aliyun-noble.list > /dev/null <<EOF
deb http://mirrors.aliyun.com/ubuntu/ ${UBUNTU_CODENAME} main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ ${UBUNTU_CODENAME}-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ ${UBUNTU_CODENAME}-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ ${UBUNTU_CODENAME}-security main restricted universe multiverse
EOF
    log_info "已写入阿里云 apt 镜像"
else
    log_warn "阿里云 apt 镜像已存在，跳过"
fi
sudo apt-get update -qq

# ---------- 手段2: 安装 python3.12-venv ----------
log_step 2 "安装 python3.12-venv..."
if dpkg -l python3.12-venv &>/dev/null; then
    log_warn "python3.12-venv 已安装，跳过"
else
    sudo apt-get install -y -qq python3.12-venv
    log_info "python3.12-venv 安装完成"
fi

# ---------- 手段3: 创建 venv（支持断点续装）----------
log_step 3 "创建 Python 虚拟环境..."
if [ -d ".venv" ]; then
    log_warn ".venv 已存在，跳过创建（如需重建请手动删除 .venv）"
else
    python3 -m venv .venv
    log_info "虚拟环境创建完成"
fi
source .venv/bin/activate

# ---------- 手段4: pip 国内镜像 + 优化参数 ----------
log_step 4 "配置 pip 国内镜像与优化参数..."
mkdir -p ~/.config/pip
if [ ! -f ~/.config/pip/pip.conf ]; then
    cat > ~/.config/pip/pip.conf <<'EOF'
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
extra-index-url = https://mirrors.aliyun.com/pypi/simple/
trusted-host = pypi.tuna.tsinghua.edu.cn
               mirrors.aliyun.com
timeout = 120
retries = 5
prefer-binary = true
disable-pip-version-check = true
EOF
    log_info "pip 国内镜像配置完成"
else
    log_warn "~/.config/pip/pip.conf 已存在，跳过写入"
fi

# ---------- 手段5: 升级 pip 并安装 uv ----------
log_step 5 "升级 pip 并安装 uv（Rust 极速包管理器）..."
pip install --quiet --upgrade pip

if command -v uv &>/dev/null; then
    log_warn "uv 已安装，跳过"
else
    pip install --quiet uv
    log_info "uv 安装完成"
fi

# ---------- 手段6: uv 极速安装依赖 ----------
log_step 6 "使用 uv 极速安装 Python 依赖..."

# WSL + NTFS 跨文件系统不支持 hardlink，强制使用 copy 模式
export UV_LINK_MODE=copy
export PYTHONDONTWRITEBYTECODE=1
export UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
export UV_EXTRA_INDEX_URL="https://mirrors.aliyun.com/pypi/simple"

# uv 默认只从第一个索引搜索包版本，当镜像版本不全时会冲突。
# unsafe-best-match 允许在所有索引中搜索最佳版本，解决依赖冲突。
UV_STRATEGY="--index-strategy unsafe-best-match"
UV_QUIET="--no-progress"

# ---------- 智能探测并安装本地包 ----------
log_info "探测本地 editable 包..."
LOCAL_PKG_FOUND=false
FAILED_PKGS=()

for pkg_dir in libs/*/; do
    if [ -f "${pkg_dir}pyproject.toml" ] || [ -f "${pkg_dir}setup.py" ]; then
        pkg_name=$(basename "$pkg_dir")
        log_info "发现本地包: libs/${pkg_name}，执行 editable 安装..."
        
        # 使用 --index-strategy unsafe-best-match 避免跨镜像版本缺失
        if uv pip install $UV_STRATEGY $UV_QUIET -e "$pkg_dir"; then
            log_info "libs/${pkg_name} 安装成功"
            LOCAL_PKG_FOUND=true
        else
            log_error "libs/${pkg_name} 安装失败（依赖冲突或版本不兼容）"
            FAILED_PKGS+=("$pkg_name")
        fi
    fi
done

if [ "$LOCAL_PKG_FOUND" = false ]; then
    log_warn "未在 libs/ 下找到有效的 Python 包"
fi

if [ ${#FAILED_PKGS[@]} -gt 0 ]; then
    log_warn "以下包安装失败: ${FAILED_PKGS[*]}"
    log_warn "可手动检查依赖或尝试: uv pip install -e libs/<包名> $UV_STRATEGY"
fi

# ---------- 安装 langchain-openai ----------
log_info "正在安装 langchain-openai（使用 uv）..."
uv pip install $UV_STRATEGY $UV_QUIET langchain-openai
log_info "langchain-openai 安装成功"

# ---------- 手段7: 安装后验证 ----------
log_step 7 "安装后验证..."

# 验证1: uv pip list 检查
if uv pip list | grep -q "langchain-openai"; then
    ver=$(uv pip list | grep "langchain-openai" | awk '{print $2}')
    log_info "uv 确认: langchain-openai 版本 $ver"
else
    log_warn "uv pip list 未找到 langchain-openai"
fi

# 验证2: Python import 检查
if python -c "import langchain_openai" 2>/dev/null; then
    log_info "Python import 检查通过"
else
    log_warn "Python import 检查失败"
fi

# ---------- 完成提示 ----------
echo ""
log_info "========================================"
log_info "  全部安装完成！"
log_info "========================================"
echo ""
echo -e "  激活环境命令："
echo -e "  ${YELLOW}source $(pwd)/.venv/bin/activate${NC}"
echo ""

if [ ${#FAILED_PKGS[@]} -gt 0 ]; then
    echo -e "  ${RED}注意：以下本地包安装失败，请手动处理：${NC}"
    for pkg in "${FAILED_PKGS[@]}"; do
        echo -e "  ${YELLOW}uv pip install -e libs/${pkg} --index-strategy unsafe-best-match${NC}"
    done
    echo ""
fi


source .venv/bin/activate
python -c "
import importlib.metadata as md
for pkg in ['langgraph', 'langchain', 'langchain-core', 'langchain-community']:
    try:
        v = md.version(pkg)
        print(f'{pkg}: {v}')
    except Exception as e:
        print(f'{pkg}: 未安装或异常 ({e})')
"
