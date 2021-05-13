import logging
from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel


class Style(str, Enum):
    BOLD = ("bold",)
    ITALICS = "italics"
    CODE = "code"
    STRIKE = "strike"
    NORMAL = "normal"


class Format(BaseModel):
    style: Style = Style.NORMAL


STYLE_CODES = {"bold": "**", "italics": "__", "code": "`", "strike": "~~", "normal": ""}


class TgcfFormat:
    id = "format"

    def __init__(self, data):
        self.format = Format(**data)
        logging.info(self.format)

    def modify(self, message):
        msg_text: str = message.raw_text
        if not msg_text:
            return message
        style = STYLE_CODES.get(self.format.style)
        message.text = f"{style}{msg_text}{style}"
        return message
