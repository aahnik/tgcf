import logging
from importlib import import_module
from typing import List

from tgcf.config import CONFIG

PLUGINS = CONFIG.plugins

plugins = []


def load_plugins():
    plugins = []
    for plugin_id, plugin_data in PLUGINS.items():
        plugin_module_name = f"tgcf_{plugin_id}"
        plugin_class_name = f"Tgcf{plugin_id.title()}"
        try:
            plugin_module = import_module(plugin_module_name)
            PluginClass = getattr(plugin_module, plugin_class_name)
            plugin = PluginClass(plugin_data)
            assert plugin.id == plugin_id

        except ModuleNotFoundError:
            logging.error(f"Could not find plugin for {plugin_id}")
        except AttributeError:
            logging.error(f"Found plugin {plugin_id}, but failed to load.")
        else:
            print(f"Loaded plugin {plugin_id}")
            plugins.append(plugin)
    return plugins


plugins = load_plugins()


def apply_plugins(message) -> List:
    for plugin in plugins:
        message = plugin.modify(message)
        logging.info(f"Applied plugin {plugin.id}")
        if not message:
            return
    return message
