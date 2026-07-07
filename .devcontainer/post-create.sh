#!/usr/bin/env bash
set -euo pipefail

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
