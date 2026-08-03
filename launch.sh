
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
venv_dir="$script_dir/.venv"
venv_python="$venv_dir/bin/python"

if [[ ! -d "$venv_dir" ]]; then
  echo "First-time setup: creating virtual environment..."
  python3 -m venv "$venv_dir"

  echo "Installing requirements..."
  "$venv_dir/bin/pip" install -r "$script_dir/requirements.txt"
fi

exec "$venv_python" "$script_dir/app.py"