"""Subpackage of tgcf: plugins.

Contains all the first-party tgcf plugins.
"""


import inspect
import logging
from enum import Enum
from importlib import import_module
from typing import Any, Dict

from telethon.tl.custom.message import Message

from tgcf.config import CONFIG
from tgcf.plugin_models import ASYNC_PLUGIN_IDS, FileType
from tgcf.utils import cleanup, stamp

# PLUGINS = CONFIG.plugin_cfgs


class TgcfMessage:
    def __init__(self, message: Message) -> None:
        self.message = message
        self.text = self.message.text
        self.raw_text = self.message.raw_text
        self.sender_id = self.message.sender_id
        self.file_type = self.guess_file_type()
        self.new_file = None
        self.cleanup = False
        self.reply_to = None
        self.client = self.message.client

    async def get_file(self) -> str:
        """Downloads the file in the message and returns the path where its saved."""
        if self.file_type == FileType.NOFILE:
            raise FileNotFoundError("No file exists in this message.")
        self.file = stamp(await self.message.download_media(""), self.sender_id)
        return self.file

    def guess_file_type(self) -> FileType:
        for i in FileType:
            if i == FileType.NOFILE:
                return i
            obj = getattr(self.message, i.value)
            if obj:
                return i

    def clear(self) -> None:
        if self.new_file and self.cleanup:
            cleanup(self.new_file)
            self.new_file = None


class TgcfPlugin:
    id_ = "plugin"

    def __init__(self, data: Dict[str, Any]) -> None:  # TODO data type has changed
        self.data = data

    async def __ainit__(self) -> None:
        """Asynchronous initialization here."""

    def modify(self, tm: TgcfMessage) -> TgcfMessage | None:
        """Modify the message here."""
        return tm


def load_plugins() -> Dict[int, Dict[str, TgcfPlugin]]:
    """Load the plugins specified in config."""
    _plugins: Dict = {}
    # plugin_cfg_id: { plugin_id: plugin }
    for pcfg_id, cfg in enumerate(CONFIG.plugin_cfgs):
        _plugins[pcfg_id] = {}
        for item in cfg:
            if item[0] == "alias":
                continue

            plugin_id = item[0]
            if item[1].check == False:
                continue

            plugin_class_name = f"Tgcf{plugin_id.title().replace('_', '')}"
            logging.info(f"plugin class name {plugin_class_name}")

            try:  # try to load first party plugin
                plugin_module = import_module("tgcf.plugins." + plugin_id)

            except ModuleNotFoundError:
                logging.error(
                    f"{plugin_id} is not a first party plugin. Third party plugins are not supported."
                )
            else:
                logging.info(f"First party plugin {plugin_id} loaded!")

            try:
                plugin_class = getattr(plugin_module, plugin_class_name)
                if not issubclass(plugin_class, TgcfPlugin):
                    logging.error(
                        f"Plugin class {plugin_class_name} does not inherit TgcfPlugin"
                    )
                    continue
                plugin: TgcfPlugin = plugin_class(item[1])
                if not plugin.id_ == plugin_id:
                    logging.error(
                        f"Plugin id for {plugin_id} does not match expected id."
                    )
                    continue
            except AttributeError as err:
                logging.error(f"Found plugin {plugin_id}, but plugin class not found.")
                logging.error(err)
            else:
                logging.info(f"Loaded plugin {plugin_id}")
                _plugins[pcfg_id].update({plugin.id_: plugin})
    return _plugins


async def load_async_plugins() -> None:
    """Load async plugins specified plugin_models."""
    if plugins:
        for pcfg_id, cfg in plugins.items():
            for _id in ASYNC_PLUGIN_IDS:
                if _id in plugins[pcfg_id].keys():
                    await plugins[pcfg_id][_id].__ainit__()
                    logging.info(f"Plugin {_id} asynchronously loaded")


async def apply_plugins(pcfg_id: int, message: Message) -> TgcfMessage | None:
    """Apply all loaded plugins to a message."""
    tm = TgcfMessage(message)
    pcfg = plugins[pcfg_id]

    for _id, plugin in pcfg.items():
        try:
            if inspect.iscoroutinefunction(plugin.modify):
                ntm = await plugin.modify(tm)
            else:
                ntm = plugin.modify(tm)
        except Exception as err:
            logging.error(f"Failed to apply plugin {_id}. \n {err} ")
        else:
            logging.info(f"Applied plugin {_id}")
            if not ntm:
                tm.clear()
                return None
    return tm


plugins = load_plugins()
