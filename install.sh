#!/usr/bin/env bash
set -euo pipefail

# TheRock test agent is a project-level OpenCode overlay.
# Install it into the directory where the user will run `opencode`.

AGENT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-$(pwd)}"

resolve_path() {
    local path="$1"
    mkdir -p "$path"
    cd "$path" && pwd
}

copy_overlay_dir() {
    local source_dir="$1"
    local target_dir="$2"
    local label="$3"

    if [ ! -d "$source_dir" ]; then
        echo "缺少 ${label}: ${source_dir}" >&2
        exit 1
    fi

    if [ "$(cd "$source_dir" && pwd)" = "$(resolve_path "$target_dir")" ]; then
        echo "跳过 ${label}: 源目录和目标目录相同"
        return
    fi

    mkdir -p "$target_dir"
    cp -a "${source_dir}/." "$target_dir/"
    echo "已安装 ${label}: ${target_dir}"
}

install_env_template() {
    local target="$1"
    local source_env="${AGENT_ROOT}/.env_example"

    if [ ! -f "$source_env" ]; then
        echo "缺少 .env_example: ${source_env}" >&2
        exit 1
    fi

    cp -a "$source_env" "${target}/.env_example"
    if [ ! -f "${target}/.env" ]; then
        cp -a "$source_env" "${target}/.env"
        chmod 600 "${target}/.env"
        echo "已创建 .env: ${target}/.env"
    else
        echo "保留已有 .env: ${target}/.env"
    fi
}

print_usage() {
    local target="$1"

    echo ""
    echo "====================================="
    echo " TheRock OpenCode overlay 安装完成"
    echo "====================================="
    echo ""
    echo "目标目录: ${target}"
    echo ""
    echo "下一步："
    echo "  cd \"${target}\""
    echo "  nano .env   # 可选：设置 THEROCK_SUDO_POLICY=none/cache/ask，不要写 sudo 密码"
    echo "  sudo -v     # 可选：仅当 THEROCK_SUDO_POLICY=cache 且本机测试需要 sudo 时执行"
    echo "  opencode"
    echo "  /therock-run /output-linux-portable/build gfx1151"
    echo ""
    echo "也可以直接手动验证 runner："
    echo "  .opencode/tools/therock_agent.sh init --artifacts /output-linux-portable/build --gpu gfx1151 --components hiprand --test-types quick"
    echo ""
}

main() {
    local target_abs
    target_abs="$(resolve_path "$TARGET_DIR")"

    echo "===== TheRock OpenCode overlay installer ====="
    echo "Agent overlay root: ${AGENT_ROOT}"
    echo "Install target:     ${target_abs}"
    echo ""

    copy_overlay_dir "${AGENT_ROOT}/.opencode" "${target_abs}/.opencode" ".opencode"
    copy_overlay_dir "${AGENT_ROOT}/docs_this_project" "${target_abs}/docs_this_project" "docs_this_project"
    install_env_template "$target_abs"

    if [ -d "${target_abs}/.opencode/tools" ]; then
        chmod +x "${target_abs}/.opencode/tools/"*.sh 2>/dev/null || true
    fi

    print_usage "$target_abs"
}

main "$@"
