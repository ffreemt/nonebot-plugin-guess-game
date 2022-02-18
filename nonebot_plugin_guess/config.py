"""Config guess."""
# pylint: disable=invalid-name)

from typing import List

from pydantic import BaseSettings, Field, validator

from logzero import logger


class Settings(BaseSettings):
    """Config."""
    name: str = "城市名"
    # fmt: off
    limit: int = Field(
        4,
        lt=8,
        gt=-1,
        description="max number of guesses",
        title="limit",
    )
    name_list: List[str] = Field(default_factory=lambda: [
        "", "上海", "北京", "广州", "深圳", "香港", "雅典",
        "西安", "长沙", "多伦多", "旧金山", "Zurich", "约翰内斯堡",
    ])
    # fmt: on

    @validator("limit")
    def validate_limit(cls, i):  # pylint:  disable=no-self-argument, no-self-use
        """Validate limit."""
        if i < 1:
            logger.warning(" limit = %s < 1 makes no sense, setting to 1.", i)
            i = 1
        return i

    @validator("name_list")
    def validate_namelist(cls, v):  # pylint:  disable=no-self-argument, no-self-use
        """Validate namelist."""
        res = []
        for elm in v:
            try:
                elm = elm.strip()
            except Exception as exc:
                logger.error(exc)
                raise

            if len(elm) > 7:
                raise ValueError(
                    f"Each entry must be shorter than 8, this entry [{elm}] too long"
                )

            if len(elm) == 0:
                logger.warning(
                    "This entry [%s] is empty: probably not what you want, but we let it pass.",
                    elm,
                )

            res.append(elm)

        if len(res) < 2:
            raise ValueError("The name_list length should be at least 2.")

        return res

    class Config:  # pylint: disable=too-few-public-methods
        """Config."""

        env_prefix = "guess_"
        # extra = "allow"
        env_file = ".env"
        env_file_encoding = "utf-8"

        logger.info("env_prefix: %s, env_file: %s", env_prefix, env_file)
