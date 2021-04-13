"""Test config.py."""
import nonebot
import pytest

nonebot.init()
from nonebot_plugin_guess.config import Settings  # noqa: E402


def test_settings():
    """Test settings."""
    config = Settings(limit=0)
    assert config.limit == 1


@pytest.mark.xfail
def test_limit_negative():
    """Test negative limit value."""
    config = Settings(limit=-1)  # noqa: F841
