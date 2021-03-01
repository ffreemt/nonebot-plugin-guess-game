"""Config guess."""
from typing import List

from pydantic import BaseSettings, Field, validator

from logzero import logger


class Settings(BaseSettings):
    name: str = "城市名"
    limit: int = 4
    # fmt: off
    name_list: List[str] = Field(default_factory=lambda: [
        "", "上海", "北京", "广州", "深圳", "香港", "雅典",
        "西安", "长沙", "多伦多", "旧金山", "Zurich", "约翰内斯堡",
    ])
    # fmt: on

    @validator("limit")
    def validate_limit(cls, i):
        if i < 1:
            logger.warning(" limit = %s < 1 makes no sense, setting to 1.", i)
            i = 1
        return i

    @validator("name_list")
    def validate_namelist(cls, v):
        res = []
        for elm in v:
            try:
                elm = elm.strip()
            except Exception as exc:
                logger.error(exc)
                raise

            if len(elm) > 7:
                raise ValueError(
                    "Each entry must be shorter than 8, this entry [%s] too short" % elm
                )

            if len(elm) == 0:
                logger.warning(
                    "This empty entry [%s]: probably not what you want, but we pass.",
                    elm,
                )

            res.append(elm)

        if len(res) < 2:
            raise ValueError("The namelist should be at least 2.")

        return res

    class Config:  # pylint: disable=too-few-public-methods
        """Config."""

        env_prefix = "guess_"
        # extra = "allow"
        env_file = ".env"
        env_file_encoding = "utf-8"
