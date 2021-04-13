"""Test Sanity."""
import nonebot

nonebot.init()

from nonebot_plugin_guess import __version__  # noqa: E402


def test_version():
    assert __version__ == "0.1.2"
