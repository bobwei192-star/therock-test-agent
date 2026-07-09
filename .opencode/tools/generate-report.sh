#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <run_id> [output_root]" >&2
  exit 2
fi

RUN_ID="$1"
OUTPUT_ROOT="${2:-$(cd "${SCRIPT_DIR}/../.." && pwd)/runs}"

"${SCRIPT_DIR}/therock_agent.sh" report "$RUN_ID" --output-root "$OUTPUT_ROOT"
