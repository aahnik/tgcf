import logging
from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from tgcf.plugins import TgcfMessage, TgcfPlugin


class Style(str, Enum):
    BOLD = "bold"
    ITALICS = "italics"
    CODE = "code"
    STRIKE = "strike"
    PLAIN = "plain"
    PRESERVE = "preserve"


class Format(BaseModel):
    style: Style = Style.PRESERVE


STYLE_CODES = {"bold": "**", "italics": "__", "code": "`", "strike": "~~", "normal": ""}


class TgcfFormat(TgcfPlugin):
    id_ = "format"

    def __init__(self, data: Dict[str, Any]) -> None:
        self.format = Format(**data)
        logging.info(self.format)

    def modify(self, tm: TgcfMessage) -> TgcfMessage:
        if self.format.style is Style.PRESERVE:
            return tm
        msg_text: str = tm.raw_text
        if not msg_text:
            return tm
        style = STYLE_CODES.get(self.format.style)
        tm.text = f"{style}{msg_text}{style}"
        return tm
