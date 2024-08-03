# ruff: noqa: E402, N999

from nonebot.plugin import PluginMetadata, inherit_supported_adapters, require

require("nonebot_plugin_alconna")

from . import __main__ as __main__
from .config import ConfigModel
from .data_source import load_search_func

load_search_func()

__version__ = "2.0.0"
__plugin_meta__ = PluginMetadata(
    name="YetAnotherPicSearch",
    description="基于 NoneBot2 及 PicImageSearch 的另一个 NoneBot 搜图插件",
    usage="",
    type="application",
    homepage="https://github.com/NekoAria/YetAnotherPicSearch",
    config=ConfigModel,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    extra={},
)
