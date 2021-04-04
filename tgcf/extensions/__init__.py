from tgcf.config import CONFIG
from tgcf.extensions.filters import list_safe

def extended(message):
    if CONFIG.blacklist or CONFIG.whitelist:
        if not list_safe(message):
            return
    if CONFIG.replace:
        pass
    if CONFIG.text_format:
        pass
    return message


