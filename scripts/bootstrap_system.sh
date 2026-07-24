#!/usr/bin/env bash
set -euo pipefail
sudo apt update
sudo apt install -y git curl wget unzip jq tree ca-certificates build-essential postgresql-client make shellcheck
echo "System tools installed."
