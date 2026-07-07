#!/usr/bin/env bash
set -euo pipefail

# Ensure ~/.local/bin is on PATH for pip --user installs, for this script
# and for future interactive shells (bash + zsh).
export PATH="$HOME/.local/bin:$PATH"
for rc in "$HOME/.bashrc" "$HOME/.zshrc" "$HOME/.profile"; do
  if [ -f "$rc" ] && ! grep -qF '$HOME/.local/bin' "$rc"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$rc"
  fi
done

echo "[post-create] Installing dev dependencies..."
pip install --user --upgrade pip
pip install --user -e '.[dev]'

echo "[post-create] Verifying tools on PATH..."
python --version
pip --version
openapi-python-client --version
pytest --version
ruff --version
mypy --version

echo "[post-create] Marking complete."
touch .devcontainer/.post-create-done
