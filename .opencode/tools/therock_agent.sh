#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

PYTHONUNBUFFERED=1 \
PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH:-}" \
  python3 -m therock_agent.cli "${PROJECT_ROOT}" "$@"
