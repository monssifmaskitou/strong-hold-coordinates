#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
venv_python="$script_dir/.venv/bin/python"

if [[ -x "$venv_python" ]]; then
  exec "$venv_python" "$script_dir/app.py"
fi

exec python3 "$script_dir/app.py"