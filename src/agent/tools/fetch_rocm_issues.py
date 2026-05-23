"""从 ROCm/ROCm GitHub 仓库拉取所有 Issues 并整理到本地文件夹。

用法：
    python scripts/fetch_rocm_issues.py                        # 无认证（限制 60 req/h）
    python scripts/fetch_rocm_issues.py --token ghp_xxx         # 使用 GitHub Token
    python scripts/fetch_rocm_issues.py --token ghp_xxx --limit 500
    python scripts/fetch_rocm_issues.py --token ghp_xxx --state closed

输出结构：
    rocm_issues/
    ├── index.json                   # 所有 Issue 的汇总索引
    ├── stats.json                   # 统计信息
    └── issues/
        ├── 1_<title-sanitized>.md   # 每个 Issue 一个文件
        ├── 2_<title-sanitized>.md
        └── ...
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
REPO_OWNER = "ROCm"
REPO_NAME = "ROCm"
API_BASE = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
PER_PAGE = 100
MAX_RETRIES = 3
RETRY_DELAY_SEC = 5

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent / "rocm_issues"
ISSUES_DIR = OUTPUT_DIR / "issues"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def sanitize_filename(title: str, max_len: int = 80) -> str:
    """将 Issue 标题转为安全的文件名。"""
    safe = re.sub(r'[<>:"/\\|?*]', "", title)
    safe = re.sub(r"\s+", "_", safe.strip())
    safe = safe[:max_len].rstrip("._")
    return safe if safe else "untitled"


def build_headers(token: str | None) -> dict:
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "TestCaseAgent-Script/1.0",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def parse_link_header(link_header: str | None) -> dict[str, str]:
    """解析 GitHub API 的 Link header，提取各 rel 对应的 URL。"""
    if not link_header:
        return {}
    links: dict[str, str] = {}
    for part in link_header.split(","):
        match = re.search(r'<([^>]+)>;\s*rel="([^"]+)"', part.strip())
        if match:
            links[match.group(2)] = match.group(1)
    return links


def check_rate_limit(headers: dict) -> tuple[int, int]:
    """检查当前 API 速率限制剩余量。"""
    resp = requests.get(
        "https://api.github.com/rate_limit", headers=headers, timeout=10
    )
    if resp.status_code != 200:
        return 0, 0
    data = resp.json()
    core = data.get("resources", {}).get("core", {})
    return core.get("remaining", 0), core.get("limit", 0)


def handle_rate_limit(response: requests.Response, headers: dict):
    """遇到 403/429 时等待 reset 时间后重试。"""
    if response.status_code in (403, 429):
        reset_ts = int(response.headers.get("X-RateLimit-Reset", 0))
        now = int(time.time())
        wait = max(reset_ts - now + 1, 60)
        print(
            f"  ⏳ 触发速率限制，等待 {wait} 秒 (到 {datetime.fromtimestamp(reset_ts).strftime('%H:%M:%S')})..."
        )
        time.sleep(wait)
        return True
    return False


def fetch_with_retry(
    url: str, headers: dict, params: dict | None = None
) -> requests.Response:
    """带重试的 GET 请求。"""
    for attempt in range(1, MAX_RETRIES + 1):
        resp = requests.get(url, headers=headers, params=params, timeout=30)

        if resp.status_code == 200:
            return resp

        if handle_rate_limit(resp, headers):
            continue

        if resp.status_code >= 500:
            print(f"  ⚠️  服务器错误 {resp.status_code}，第 {attempt} 次重试...")
            time.sleep(RETRY_DELAY_SEC * attempt)
            continue

        if resp.status_code == 404:
            print(f"  ❌ 404 未找到: {url}")
            resp.raise_for_status()

        print(f"  ⚠️  请求失败 {resp.status_code}: {url}")
        resp.raise_for_status()

    raise RuntimeError(f"重试 {MAX_RETRIES} 次后仍失败: {url}")


def fetch_all_issues(
    headers: dict,
    state: str = "all",
    limit: int | None = None,
) -> list[dict]:
    """分页拉取所有 Issues。"""
    issues: list[dict] = []
    page = 1
    total_fetched = 0

    while True:
        params = {
            "state": state,
            "per_page": PER_PAGE,
            "page": page,
            "sort": "created",
            "direction": "desc",
        }

        print(f"  📄 正在获取第 {page} 页 (已获取 {total_fetched})...")
        resp = fetch_with_retry(f"{API_BASE}/issues", headers=headers, params=params)
        page_issues = resp.json()

        if not page_issues:
            break

        # 过滤掉 Pull Request（GitHub API 会把 PR 也作为 Issue 返回）
        real_issues = [i for i in page_issues if "pull_request" not in i]
        issues.extend(real_issues)
        total_fetched += len(real_issues)

        print(f"     → 本页 {len(page_issues)} 条，其中 Issue {len(real_issues)} 条")
        remaining, _ = check_rate_limit(headers)
        print(f"     → API 剩余额度: {remaining}")

        if limit and total_fetched >= limit:
            issues = issues[:limit]
            print(f"  🛑 达到 limit={limit}，停止拉取")
            break

        # 检查是否有下一页
        links = parse_link_header(resp.headers.get("Link"))
        if "next" not in links:
            break

        page += 1
        time.sleep(0.5)

    return issues


def fetch_issue_comments(issue_number: int, headers: dict) -> list[dict]:
    """拉取单个 Issue 的评论（最多前 100 条）。"""
    url = f"{API_BASE}/issues/{issue_number}/comments"
    params = {"per_page": 100, "page": 1}
    try:
        resp = fetch_with_retry(url, headers=headers, params=params)
        return resp.json()
    except Exception as e:
        print(f"    ⚠️  拉取评论失败 (#{issue_number}): {e}")
        return []


def fetch_issue_events(issue_number: int, headers: dict) -> list[dict]:
    """拉取 Issue 的时间线事件（用于获取时间线信息）。"""
    url = f"{API_BASE}/issues/{issue_number}/events"
    params = {"per_page": 100}
    try:
        resp = fetch_with_retry(url, headers=headers, params=params)
        return resp.json()
    except Exception as e:
        print(f"    ⚠️  拉取事件失败 (#{issue_number}): {e}")
        return []


def format_issue_body(issue: dict, comments: list[dict]) -> str:
    """将 Issue 及其评论格式化为 Markdown。"""
    created_at = issue.get("created_at", "")
    updated_at = issue.get("updated_at", "")
    closed_at = issue.get("closed_at")

    lines = [
        f"# {issue['title']}",
        "",
        f"> **Issue #{issue['number']}**",
        f"> **状态**: {issue['state']}",
        f"> **创建时间**: {created_at}",
        f"> **更新时间**: {updated_at}",
    ]
    if closed_at:
        lines.append(f"> **关闭时间**: {closed_at}")
    lines.append(
        f"> **作者**: {issue['user']['login'] if issue.get('user') else 'unknown'}"
    )
    lines.append(f"> **标签**: {', '.join(l['name'] for l in issue.get('labels', []))}")
    lines.append(f"> **URL**: {issue.get('html_url', '')}")
    lines.append("")

    # 标签详细
    labels = issue.get("labels", [])
    if labels:
        lines.extend(["## 标签", ""])
        for label in labels:
            color = label.get("color", "000000")
            lines.append(f"- **{label['name']}** (颜色: #{color})")
        lines.append("")

    # Assignees
    assignees = issue.get("assignees", [])
    if assignees:
        lines.extend(["## 负责人", ""])
        for a in assignees:
            lines.append(f"- {a['login']}")
        lines.append("")

    # 正文
    body = issue.get("body")
    if body:
        lines.extend(["## 描述", "", body, ""])
    else:
        lines.extend(["## 描述", "", "*(无描述)*", ""])

    # 评论
    if comments:
        lines.extend(["---", "", f"## 评论 ({len(comments)} 条)", ""])
        for i, comment in enumerate(comments, 1):
            comment_user = comment.get("user", {}).get("login", "unknown")
            comment_time = comment.get("created_at", "")
            lines.extend(
                [
                    f"### 评论 #{i} — {comment_user} ({comment_time})",
                    "",
                    comment.get("body", "") or "",
                    "",
                    "---",
                    "",
                ]
            )

    return "\n".join(lines)


def build_index_entry(issue: dict, filename: str, comment_count: int) -> dict:
    """构建索引条目。"""
    labels = issue.get("labels", [])
    return {
        "number": issue["number"],
        "title": issue["title"],
        "state": issue["state"],
        "created_at": issue.get("created_at"),
        "updated_at": issue.get("updated_at"),
        "closed_at": issue.get("closed_at"),
        "author": issue.get("user", {}).get("login", "unknown"),
        "labels": [l["name"] for l in labels],
        "label_colors": {l["name"]: f"#{l['color']}" for l in labels},
        "assignees": [a["login"] for a in issue.get("assignees", [])],
        "comment_count": comment_count,
        "url": issue.get("html_url", ""),
        "filename": filename,
    }


def build_stats(issues: list[dict], index: list[dict]) -> dict:
    """构建统计信息。"""
    open_count = sum(1 for i in issues if i.get("state") == "open")
    closed_count = sum(1 for i in issues if i.get("state") == "closed")

    label_counts: dict[str, int] = {}
    for issue in issues:
        for label in issue.get("labels", []):
            name = label["name"]
            label_counts[name] = label_counts.get(name, 0) + 1
    sorted_labels = sorted(label_counts.items(), key=lambda x: -x[1])

    author_counts: dict[str, int] = {}
    for issue in issues:
        author = issue.get("user", {}).get("login", "unknown")
        author_counts[author] = author_counts.get(author, 0) + 1
    sorted_authors = sorted(author_counts.items(), key=lambda x: -x[1])[:20]

    return {
        "repo": f"{REPO_OWNER}/{REPO_NAME}",
        "total_issues": len(issues),
        "open_issues": open_count,
        "closed_issues": closed_count,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "top_labels": [{"name": n, "count": c} for n, c in sorted_labels[:30]],
        "top_authors": [{"name": n, "count": c} for n, c in sorted_authors],
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="从 ROCm/ROCm GitHub 仓库拉取所有 Issues 并整理到本地文件夹",
    )
    parser.add_argument(
        "--token",
        help="GitHub Personal Access Token（可选，不传则匿名访问，限制 60 req/h）",
        default=None,
    )
    parser.add_argument(
        "--state",
        choices=["open", "closed", "all"],
        default="all",
        help="Issue 状态筛选（默认 all）",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="最多拉取多少条 Issue（默认不限制）",
    )
    parser.add_argument(
        "--comments",
        action="store_true",
        default=True,
        help="同时拉取评论（默认启用，耗时较长）",
    )
    parser.add_argument(
        "--no-comments",
        action="store_false",
        dest="comments",
        help="不拉取评论（速度更快）",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=OUTPUT_DIR,
        help=f"输出目录（默认 {OUTPUT_DIR}）",
    )
    args = parser.parse_args()

    output_dir = args.output.resolve()
    issues_dir = output_dir / "issues"
    headers = build_headers(args.token)

    # ---- 检查 API 可用性 ----
    print(f"🔍 检查 GitHub API 可用性...")
    remaining, limit = check_rate_limit(headers)
    print(f"   API 额度: {remaining}/{limit}")
    if remaining == 0:
        print("   ❌ API 额度已用完，请稍后再试或使用 --token")
        sys.exit(1)
    if remaining < 100 and not args.token:
        print("   ⚠️  匿名访问额度低，建议使用 --token")

    # ---- 拉取 Issues ----
    print(f"\n📥 开始拉取 {REPO_OWNER}/{REPO_NAME} Issues (state={args.state})...")
    if args.limit:
        print(f"   限制: 最多 {args.limit} 条")
    issues = fetch_all_issues(headers, state=args.state, limit=args.limit)

    if not issues:
        print("❌ 未拉取到任何 Issue")
        sys.exit(1)

    print(f"\n✅ 共获取 {len(issues)} 条 Issue")
    open_count = sum(1 for i in issues if i.get("state") == "open")
    closed_count = sum(1 for i in issues if i.get("state") == "closed")
    print(f"   Open: {open_count} | Closed: {closed_count}")

    # ---- 创建输出目录 ----
    output_dir.mkdir(parents=True, exist_ok=True)
    issues_dir.mkdir(parents=True, exist_ok=True)

    # ---- 拉取评论并保存 Issue 文件 ----
    print(f"\n📝 保存 Issue 到 {issues_dir}...")
    index: list[dict] = []
    errors = 0

    for idx, issue in enumerate(issues, 1):
        num = issue["number"]
        title = issue["title"]
        filename = f"{num}_{sanitize_filename(title)}.md"
        filepath = issues_dir / filename

        # 进度显示
        bar_len = 40
        progress = idx / len(issues)
        filled = int(bar_len * progress)
        bar = "█" * filled + "▒" * (bar_len - filled)
        print(f"\r  [{bar}] {idx}/{len(issues)}  #{num}", end="", flush=True)

        # 拉取评论
        comments = []
        if args.comments:
            try:
                comments = fetch_issue_comments(num, headers)
            except Exception as e:
                print(f"\n    ⚠️  #{num} 评论拉取失败: {e}")

        # 写入文件
        try:
            content = format_issue_body(issue, comments)
            filepath.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"\n    ❌ #{num} 写入失败: {e}")
            errors += 1
            continue

        # 构建索引
        index.append(build_index_entry(issue, filename, len(comments)))

    print()

    # ---- 写入索引 ----
    index_path = output_dir / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"\n📑 索引已保存: {index_path}")

    # ---- 写入统计 ----
    stats = build_stats(issues, index)
    stats_path = output_dir / "stats.json"
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print(f"📊 统计已保存: {stats_path}")

    # ---- 写入 README ----
    readme_lines = [
        f"# ROCm/ROCm Issues ({datetime.now().strftime('%Y-%m-%d')})",
        "",
        f"从 [{REPO_OWNER}/{REPO_NAME}](https://github.com/{REPO_OWNER}/{REPO_NAME}) 自动拉取",
        "",
        "## 统计",
        "",
        f"- 总数: {stats['total_issues']}",
        f"- Open: {stats['open_issues']}",
        f"- Closed: {stats['closed_issues']}",
        f"- 拉取时间: {stats['fetched_at']}",
        "",
        "## 标签分布（Top 20）",
        "",
    ]
    for label in stats["top_labels"][:20]:
        bar = "█" * max(1, label["count"] // 5)
        readme_lines.append(f"- **{label['name']}**: {label['count']} {bar}")
    readme_lines.extend(
        ["", "## 文件结构", "", "- `index.json` - 所有 Issue 的汇总索引"]
    )
    readme_lines.append("- `stats.json` - 统计信息")
    readme_lines.append("- `issues/` - 每个 Issue 的 Markdown 文件")
    readme_lines.append("  - 命名规则: `<issue_number>_<title>.md`")
    readme_lines.append("  - 内容包含: 标题、标签、负责人、描述、评论")

    readme_path = output_dir / "README.md"
    readme_path.write_text("\n".join(readme_lines), encoding="utf-8")
    print(f"📖 README 已保存: {readme_path}")

    # ---- 汇总 ----
    print(f"\n{'=' * 60}")
    print(f"✅ 完成!")
    print(f"   仓库: {REPO_OWNER}/{REPO_NAME}")
    print(f"   拉取: {len(issues)} 条 Issue")
    print(f"   文件: {len(index)} 个 (错误: {errors})")
    print(f"   目录: {output_dir}")
    if errors:
        print(f"   ⚠️  有 {errors} 个文件写入失败，请查看上方日志")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
