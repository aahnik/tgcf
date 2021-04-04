from tgcf.config import CONFIG
import logging

def list_safe(message) -> bool:
    logging.info('Making list safe')
    for forbidden in CONFIG.blacklist:
        if forbidden in message.raw_text:
            return False
    if not CONFIG.whitelist:
        return True
    for allowed in CONFIG.whitelist:
        if allowed in message.raw_text:
            return True
    return False
