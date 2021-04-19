from importlib import import_module
import logging
from typing import List
from tgcf.config import CONFIG

PLUGINS = CONFIG.plugins


def apply_plugins(message)->List:
    for plugin_id,plugin_data in PLUGINS.items():
        plugin_name = f"tgcf_{plugin_id}"
        try:
            plugin = import_module(plugin_name)
        except ModuleNotFoundError:
            logging.error(f"Could not find plugin {plugin_name}")
        else:
            print(plugin_name)
            print(plugin_data)
    return None




