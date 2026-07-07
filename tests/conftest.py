"""Shared test fixtures."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import respx


@pytest.fixture
def fixtures_dir() -> Path:
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def load_fixture(fixtures_dir: Path):
    def _load(name: str) -> dict[str, Any]:
        return json.loads((fixtures_dir / name).read_text())
    return _load


@pytest.fixture
def respx_mock():
    with respx.mock(assert_all_called=False) as mock:
        yield mock
