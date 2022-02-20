<!-- [![tests](https://github.com/ffreemt/nonebot-plugin-guess-game/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/nonebot-plugin-guess-game/actions/workflows/routine-tests.yml) -->
# nonebot-plugin-guess
[![nonebot2beta](https://img.shields.io/static/v1?label=nonebot&message=v2b2&color=green)](https://v2.nonebot.dev/)[![onebot](https://img.shields.io/static/v1?label=driver&message=onebot&color=green)](https://adapter-onebot.netlify.app/)[![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/nonebot-plugin-guess.svg)](https://badge.fury.io/py/nonebot-plugin-guess)

《猜猜看》nonebot2插件（Guess a name plugin for nonebot2）

Field-tested with ``nonebot 2.0.0b2``

## 安装

```bash
pip install nonebot-plugin-guess
# pip install nonebot-plugin-guess -U  # 升级到最新版
```
or
```bash
poetry add nonebot-plugin-guess
# poetry add nonebot-plugin-guess@latest   # 升级到最新版
```
or
```
poetry add git+https://github.com/ffreemt/nonebot-plugin-guess-game.git
```
or
```
pip install git+https://github.com/ffreemt/nonebot-plugin-guess-game.git
```
or clone [https://github.com/ffreemt/nonebot-plugin-guess-game](https://github.com/ffreemt/nonebot-plugin-guess-game) and install from the repo.

## 使用
```python
# bot.py
...
nonebot.load_plugin("nonebot_plugin_guess")
...
```
然后在机器人所在的群里或给机器人发私信 `/guess` （或cai, 猜猜看, 猜）即可开始“猜猜看”游戏。

### 定制

插件自带的游戏数据仅限“猜城市名” 及固定的城市名："上海", "北京", "广州", "深圳", "香港", "雅典", "西安", "长沙", "多伦多", "旧金山", "Zurich", "约翰内斯堡"; 最多猜的次数： 4

如需自己定制游戏，可在`.env` 里加入：
```bash
# .env
guess_name = "人名"
guess_max = 3
guess_name_list = ["贾宝玉", "林黛玉"，]
```