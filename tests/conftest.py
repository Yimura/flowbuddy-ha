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


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations: None):
    """Make custom_components/ discoverable by HA's loader in every test.

    ``enable_custom_integrations`` is provided by
    pytest-homeassistant-custom-component (registered as a pytest11 plugin);
    requesting it here as an autouse fixture means individual tests -- and in
    particular tests/test_config_flow.py's use of the ``hass`` fixture --
    don't each need to remember to depend on it explicitly.
    """
    yield
