"""Subpackage of tgcf: plugins.

Contains all the first-party tgcf plugins.
"""


import logging
from importlib import import_module
from typing import List
import inspect
from tgcf.config import CONFIG

PLUGINS = CONFIG.plugins


def load_plugins():
    """Load the plugins specified in config."""
    _plugins = {}
    for plugin_id, plugin_data in PLUGINS.items():

        plugin_class_name = f"Tgcf{plugin_id.title()}"

        try:
            plugin_module = import_module("tgcf.plugins." + plugin_id)
        except ModuleNotFoundError:
            logging.error(
                f"{plugin_id} is not a first party plugin. Trying to load from availaible third party plugins."
            )
            try:
                plugin_module_name = f"tgcf_{plugin_id}"
                plugin_module = import_module(plugin_module_name)
            except ModuleNotFoundError:
                logging.error(
                    f"Module {plugin_module_name} not found. Failed to load plugin {plugin_id}"
                )
                continue
            else:
                logging.info(
                    f"Plugin {plugin_id} is successfully loaded from third party plugins"
                )
        else:
            logging.info(f"First party plugin {plugin_id} loaded!")
        try:
            plugin_class = getattr(plugin_module, plugin_class_name)
            plugin = plugin_class(plugin_data)
            assert plugin.id_ == plugin_id
        except AttributeError:
            logging.error(f"Found plugin {plugin_id}, but failed to load.")
        else:
            print(f"Loaded plugin {plugin_id}")
            _plugins.update({plugin.id_: plugin})
    return _plugins


async def apply_plugins(message) -> List:
    """Apply all loaded plugins to a message."""
    for _id, plugin in plugins.items():
        if inspect.iscoroutinefunction(plugin.modify):
            message = await plugin.modify(message)
        else:
            message = plugin.modify(message)
        logging.info(f"Applied plugin {_id}")
        if not message:
            return None
    return message


plugins = load_plugins()
