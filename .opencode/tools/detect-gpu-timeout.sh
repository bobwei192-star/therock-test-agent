#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <log-file-or-dir>" >&2
  exit 2
fi

TARGET="$1"
PATTERN='ring gfx|GPU reset|MES failed|REMOVE_QUEUE|PERMISSION_FAULT|HSA_STATUS_ERROR|amdgpu.*timeout'

if [ -d "$TARGET" ]; then
  grep -RniE "$PATTERN" "$TARGET" || true
elif [ -f "$TARGET" ]; then
  grep -niE "$PATTERN" "$TARGET" || true
else
  echo "Target not found: $TARGET" >&2
  exit 2
fi
