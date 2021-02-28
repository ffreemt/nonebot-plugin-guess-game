"""Config guess."""
from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    name: str = "城市"
    limit: int = 4
    # fmt: off
    name_list: List[str] = Field(default_factory=lambda: [
        "", "上海", "北京", "广州", "深圳", "香港", "雅典",
        "西安", "长沙", "多伦多", "旧金山", "Zurich", "约翰内斯堡",
    ])
    # fmt: on

    class Config:  # pylint: disable=too-few-public-methods
        """Config."""

        env_prefix = "guess_"
        # extra = "allow"
        env_file = ".env"
        env_file_encoding = "utf-8"
