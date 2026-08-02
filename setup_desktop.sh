#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
desktop_dir="${XDG_DATA_HOME:-$HOME/.local/share}/applications"
desktop_file="$desktop_dir/Stronghold Finder.desktop"

mkdir -p "$desktop_dir"

cat > "$desktop_file" <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Stronghold Finder
Comment=Minecraft Stronghold Triangulation Calculator
Exec=/bin/bash "$script_dir/launch.sh"
Icon=$script_dir/icon.png
Terminal=false
Categories=Utility;Development;
EOF

chmod +x "$desktop_file"

printf 'Installed desktop launcher to %s\n' "$desktop_file"