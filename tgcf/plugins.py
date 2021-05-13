"""Load and apply plugins."""

import logging
from importlib import import_module
from typing import List

from tgcf.config import CONFIG

PLUGINS = CONFIG.plugins


def load_plugins():
    """Load the plugins specified in config."""
    _plugins = {}
    for plugin_id, plugin_data in PLUGINS.items():
        plugin_module_name = f"tgcf_{plugin_id}"
        plugin_class_name = f"Tgcf{plugin_id.title()}"
        try:
            plugin_module = import_module(plugin_module_name)
            plugin_class = getattr(plugin_module, plugin_class_name)
            plugin = plugin_class(plugin_data)
            assert plugin.id_ == plugin_id

        except ModuleNotFoundError:
            logging.error(f"Could not find plugin for {plugin_id}")
        except AttributeError:
            logging.error(f"Found plugin {plugin_id}, but failed to load.")
        else:
            print(f"Loaded plugin {plugin_id}")
            _plugins.update({plugin.id_: plugin})
    return _plugins


def apply_plugins(message) -> List:
    """Apply all loaded plugins to a message."""
    for _id,plugin in plugins.items():
        message = plugin.modify(message)
        logging.info(f"Applied plugin {_id}")
        if not message:
            return None
    return message


plugins = load_plugins()
