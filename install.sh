#!/usr/bin/env bash
set -euo pipefail

# ====================== 全局配置 ======================
# 本定制仓库根目录（install.sh所在目录）
CUSTOM_REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# 原版OpenCode克隆目录
OPENCODE_SRC_DIR="${CUSTOM_REPO_ROOT}/opencode"
# 独立外置子Agent（单组件执行器）存放路径
TEST_AGENT_TARGET_DIR="$HOME/therock-test-agent"
# OpenCode上游源码仓库
OPENCODE_GIT_URL="https://github.com/anomalyco/opencode.git"

# 安装 Bun（安装至 ~/.local，适配无root环境）
install_bun() {
    echo "=== 步骤1: 安装 Bun ==="
    if command -v bun &>/dev/null; then
        echo "Bun 已存在: $(bun --version)"
        export PATH="$HOME/.local/bin:$PATH"
        return
    fi

    export BUN_INSTALL="$HOME/.local"
    curl -fsSL shturl.cc/XshxM9vzpn2i | bash
    export PATH="$BUN_INSTALL/bin:$PATH"

    if ! command -v bun &>/dev/null; then
        echo "Bun 安装失败，请手动执行安装脚本"
        exit 1
    fi
    echo "Bun 安装完成: $(bun --version)"
}

# 拉取/更新原版 OpenCode 源码
clone_opencode() {
    echo -e "\n=== 步骤2: 同步原版 OpenCode 源码 ==="
    if [ -d "${OPENCODE_SRC_DIR}/.git" ]; then
        echo "已存在OpenCode目录，执行git pull更新上游"
        cd "$OPENCODE_SRC_DIR"
        git pull
    else
        echo "全新克隆OpenCode源码至: ${OPENCODE_SRC_DIR}"
        git clone --depth 1 "$OPENCODE_GIT_URL" "$OPENCODE_SRC_DIR"
    fi
}

# 极简覆盖：仅拷贝Agent配置 + 辅助工具脚本
overlay_custom_extensions() {
    echo -e "\n=== 步骤3: 注入TheRock测试编排扩展文件 ==="
    OVERLAY_ROOT="${CUSTOM_REPO_ROOT}/.opencode"
    if [ ! -d "$OVERLAY_ROOT" ]; then
        echo "未检测到.opencode扩展目录，跳过文件注入"
        return
    fi

    mkdir -p "$OPENCODE_SRC_DIR/.opencode"
    cp -r "$OVERLAY_ROOT"/* "$OPENCODE_SRC_DIR/.opencode/"
    echo "已注入文件："
    echo "  - .opencode/agents/therock-loop.md (测试循环逻辑)"
    echo "  - .opencode/agents/therock-orchestrator.md (主循环Primary Agent)"
    echo "  - .opencode/agents/therock-test-executor.md (子执行SubAgent)"
    echo "  - .opencode/tools/detect-gpu-timeout.sh (GPU Ring超时检测)"
    echo "  - .opencode/tools/generate-report.sh (三层报告生成)"
}

# 部署外置独立 therock-test-agent 目录
deploy_external_subagent() {
    echo -e "\n=== 步骤4: 部署外置单组件测试Agent ~/therock-test-agent ==="
    EXTERNAL_AGENT_SRC="${CUSTOM_REPO_ROOT}/agent-src/therock-test-agent"
    if [ ! -d "$EXTERNAL_AGENT_SRC" ]; then
        echo "无外置Agent源码，跳过部署"
        return
    fi
    rm -rf "$TEST_AGENT_TARGET_DIR"
    cp -r "$EXTERNAL_AGENT_SRC" "$TEST_AGENT_TARGET_DIR"
    chmod +x "$TEST_AGENT_TARGET_DIR"/*.sh 2>/dev/null || true
    echo "外置测试执行器部署完成：$TEST_AGENT_TARGET_DIR"
}

# 安装OpenCode项目依赖
install_dependencies() {
    echo -e "\n=== 步骤5: 安装OpenCode依赖 ==="
    cd "$OPENCODE_SRC_DIR"
    bun install
}

# TS类型校验
typecheck() {
    echo -e "\n=== 步骤6: 执行类型检查 ==="
    cd "$OPENCODE_SRC_DIR/packages/opencode"
    bun typecheck
}

# 可选构建单文件二进制
build_binary() {
    echo -e "\n=== 步骤7: 构建OpenCode单文件可执行程序 ==="
    cd "$OPENCODE_SRC_DIR"
    ./packages/opencode/script/build.ts --single
}

# 部署完成使用指引
print_usage() {
    echo -e "\n====================================="
    echo "        TheRock 极简测试引擎部署完成"
    echo "====================================="
    echo "1. 进入OpenCode交互终端"
    echo "   cd ${OPENCODE_SRC_DIR}"
    echo "   bun dev"
    echo ""
    echo "2. 直接调用主循环编排Agent"
    echo "   @therock-orchestrator"
    echo ""
    echo "3. 外置单组件测试执行器目录"
    echo "   $TEST_AGENT_TARGET_DIR"
    echo ""
    echo "扩展组件清单（无TS引擎、无插件、无自定义命令）"
    echo "  · 主调度：therock-orchestrator (Primary 内置循环逻辑)"
    echo "  · 子执行：therock-test-executor (Subagent 单组件CTest执行)"
    echo "  · 工具脚本：GPU硬件异常检测 + 自动三层报告生成"
    echo "  · 状态读写：原生Read/Write工具操作global_state.json"
}

# 主执行入口
main() {
    echo "===== TheRock Minimal Test Orchestrator 一键部署 ====="
    echo "定制仓库根目录: $CUSTOM_REPO_ROOT"
    echo "原版OpenCode路径: $OPENCODE_SRC_DIR"
    echo "外置测试Agent路径: $TEST_AGENT_TARGET_DIR"
    echo ""

    install_bun
    clone_opencode
    overlay_custom_extensions
    deploy_external_subagent
    install_dependencies
    typecheck
    build_binary
    print_usage
}

main