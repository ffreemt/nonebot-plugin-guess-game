"""Run a minimal bot."""
import nonebot

# from nonebot.adapters.cqhttp import Bot
from nonebot.adapters.onebot.v11 import Adapter

nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()

# driver.register_adapter("cqhttp", Bot)
driver.register_adapter(Adapter)  # OneBot_V11_Adapter

nonebot.load_builtin_plugins()
# nonebot.load_plugins("nonebot_plugin_guess")
nonebot.load_plugin("nonebot_plugin_guess")

if __name__ == "__main__":
    # nonebot.run()
    # nonebot.run(app="bot:app")
    nonebot.run(app="minimal_bot:app")
