import logging
from typing import Dict, Optional

from pydantic import BaseModel


class Replace(BaseModel):
    text: Optional[Dict[str, str]] = {}


class TgcfReplace:
    id_ = "replace"

    def __init__(self, data):
        self.replace = Replace(**data)
        logging.info(self.replace)

    def modify(self, message):
        msg_text: str = message.text
        if not msg_text:
            return message
        for original, new in self.replace.text.items():
            msg_text = msg_text.replace(original, new)
        message.text = msg_text
        return message
