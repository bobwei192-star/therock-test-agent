#!/usr/bin/env bash
set -euo pipefail

# TheRock test agent is a project-level OpenCode overlay.
# Install it into the directory where the user will run `opencode`.

AGENT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR=""
SETUP_SUDO_AGENT=0

while [ "$#" -gt 0 ]; do
    case "$1" in
        --setup-sudo-agent)
            SETUP_SUDO_AGENT=1
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [--setup-sudo-agent] [TARGET_DIR]"
            exit 0
            ;;
        *)
            if [ -n "$TARGET_DIR" ]; then
                echo "未知参数或重复目标目录: $1" >&2
                exit 1
            fi
            TARGET_DIR="$1"
            shift
            ;;
    esac
done

TARGET_DIR="${TARGET_DIR:-$(pwd)}"

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

verify_overlay_install() {
    local target="$1"

    local required_paths=(
        ".opencode/commands/therock-run.md"
        ".opencode/commands/therock-status.md"
        ".opencode/commands/therock-stop.md"
        ".opencode/commands/therock-resume.md"
        ".opencode/commands/therock-report.md"
        ".opencode/tools/therock_agent.sh"
        ".opencode/tools/therock_agent/cli.py"
        ".opencode/tools/therock_agent/executor.py"
        ".opencode/tools/therock_agent/reports.py"
        "scripts/therock-sudo-agent"
        "docs_this_project/component_sort_order.json"
        "docs_this_project/component_env_script_index.json"
        "docs_this_project/official_exclude.json"
    )

    for rel_path in "${required_paths[@]}"; do
        if [ ! -e "${target}/${rel_path}" ]; then
            echo "安装校验失败，缺少 ${rel_path}" >&2
            exit 1
        fi
    done
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

upsert_env_key() {
    local env_file="$1"
    local key="$2"
    local value="$3"
    local tmp_file

    tmp_file="$(mktemp)"
    if [ -f "$env_file" ]; then
        grep -v -E "^${key}=" "$env_file" > "$tmp_file" || true
    fi
    printf '%s=%s\n' "$key" "$value" >> "$tmp_file"
    mv "$tmp_file" "$env_file"
    chmod 600 "$env_file"
}

setup_sudo_agent() {
    local target="$1"
    local state_dir="${HOME}/.therock"
    local helper="${state_dir}/sudo-askpass.sh"
    local socket_path="${state_dir}/sudo-agent.sock"

    mkdir -p "$state_dir"
    chmod 700 "$state_dir"

    cat > "$helper" <<EOF
#!/usr/bin/env bash
exec "${target}/scripts/therock-sudo-agent" askpass "\$@"
EOF
    chmod 700 "$helper"

    upsert_env_key "${target}/.env" "THEROCK_SUDO_POLICY" "askpass"
    upsert_env_key "${target}/.env" "THEROCK_SUDO_ASKPASS" "$helper"
    upsert_env_key "${target}/.env" "THEROCK_SUDO_AGENT_SOCKET" "$socket_path"

    echo "已配置 session-scoped sudo agent:"
    echo "  askpass helper: ${helper}"
    echo "  socket:         ${socket_path}"
    echo "  .env:           ${target}/.env"
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
    echo "  nano .env   # 可选：设置 THEROCK_SUDO_POLICY=none/cache/askpass，不要写 sudo 密码"
    echo "  sudo -v     # 可选：仅当 THEROCK_SUDO_POLICY=cache 且本机测试需要 sudo 时执行"
    echo "  ./scripts/therock-sudo-agent run -- opencode  # 推荐：askpass 自动启动并在退出时清理"
    echo "  /therock-run artifacts=/output-linux-portable/build gpu=gfx1151 components=all test_types=all gpu_risk=skip"
    echo "  /therock-status run_id=<run_id>"
    echo "  /therock-report run_id=<run_id>"
    echo ""
    echo "已安装模块化 runner："
    echo "  .opencode/tools/therock_agent.sh"
    echo "  .opencode/tools/therock_agent/*.py"
    echo ""
    echo "也可以直接手动验证 runner："
    echo "  .opencode/tools/therock_agent.sh start-kv artifacts=/output-linux-portable/build gpu=gfx1151 components=hiprand test_types=quick"
    echo "  .opencode/tools/therock_agent.sh status"
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
    copy_overlay_dir "${AGENT_ROOT}/scripts" "${target_abs}/scripts" "scripts"
    install_env_template "$target_abs"
    if [ "$SETUP_SUDO_AGENT" -eq 1 ]; then
        setup_sudo_agent "$target_abs"
    fi
    verify_overlay_install "$target_abs"

    if [ -d "${target_abs}/.opencode/tools" ]; then
        chmod +x "${target_abs}/.opencode/tools/"*.sh 2>/dev/null || true
    fi
    if [ -d "${target_abs}/scripts" ]; then
        chmod +x "${target_abs}/scripts/"* 2>/dev/null || true
    fi

    print_usage "$target_abs"
}

main "$@"
