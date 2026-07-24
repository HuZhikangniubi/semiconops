#!/usr/bin/env bash
set -euo pipefail
commands=(python3 git uv gh docker jq tree psql make)
failed=0
for command in "${commands[@]}"; do
  if command -v "$command" >/dev/null 2>&1; then
    printf "[OK] %-12s %s\n" "$command" "$(command -v "$command")"
  else
    printf "[MISSING] %s\n" "$command"
    failed=1
  fi
done
docker compose version
python3 --version
git --version
exit "$failed"
