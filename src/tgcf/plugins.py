from tgcf.config import CONFIG
from importlib import import_module
PLUGINS = CONFIG.plugins

def load_plugins():
    for plugin_name in PLUGINS:
        plugin = import_module(plugin_name)
        
