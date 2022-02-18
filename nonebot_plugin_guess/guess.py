"""Guess a city name."""
from typing import Optional
from nonebot.typing import T_State

from pathlib import Path
from random import choice
# from packaging import version

import logzero
from logzero import logger

from nonebot import on_command  # , __version__

# from nonebot.rule import to_me

# from nonebot.adapters.cqhttp import Bot, Event
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot_plugin_guess.config import Settings

# _ = f"该插件需要 nonebot2，你的nonebot为{__version__}"
# assert version.parse(__version__).major > 1, _

config = Settings()
logzero.loglevel(20)

# guess = on_command("guess", rule=to_me(), priority=5)
# guess = on_command("guess", priority=5)
# fmt: off
guess = on_command(
    "guess",
    aliases={'cai', '猜猜看', '猜', },
    priority=5,
)
# fmt: on

logger.info("loading %s", Path(__file__).resolve().as_posix())

NAME = "城市"
LIMIT = 5
# fmt: off
NAME_LIST = [
    "", "上海", "北京", "广州", "深圳", "香港", "雅典",
    "西安", "长沙", "多伦多", "旧金山", "Zurich", "约翰内斯堡",
]
# fmt: on

NAME = config.name
LIMIT = config.limit
NAME_LIST = config.name_list

idx = 0
city = ""

# fmt: off
switch = {
    ...,  # for future use
}
# fmt: on


async def process(state: Optional[dict] = None):
    global idx
    idx += 1

    if state is None:
        state = {}

    # game_logic for idx-th move

    # fmt: off
    _ = ["/guess", "/exit", "exit",
         "退出", "不玩了", "菠萝菠萝蜜"]
    # fmt: on
    if any([elm in state for elm in _]):
        await guess.finish("……（退出游戏）")

    if city not in state and idx < LIMIT:
        _ = choice(["", "错", "错了", "猜错了", "不对", "完全不对"])
        r_msg = f"{_ + ', ' * bool(_)}请重新输入。 还有{LIMIT - idx}次机会"
        if LIMIT - idx < 2:
            r_msg = f'{r_msg}，{choice(["加油！", "要好好想一想了", "别乱猜了啊", "再猜错就玩完"])}'
        await guess.reject(r_msg)

    if idx < LIMIT:
        feedback = choice(
            ["猜对了", "居然蒙对了！", "太厉害了", "well done", "give yourself a pat on the back"]
        )
    else:
        feedback = choice(["goodbye", "再来一次（键入 /guess）？", "是有点难"])

    idx = 0

    await guess.finish(f"{feedback} (谜底： {city if city else '***'})")


@guess.handle()
# async def handle(bot: Bot, event: Event, state: dict):
async def handle(bot: Bot, event: Event, state: T_State):
    global city
    city = choice(NAME_LIST)
    logger.info(f"\n\t==> 谜底： {city}")
    await guess.send(f"猜一个{NAME}，你有{LIMIT}次机会")


@guess.receive()
async def receive(bot: Bot, event: Event, state: T_State):

    args = str(event.message).strip()
    state[args] = 1

    await process(state)
