import logging
from typing import List, Optional

from pydantic import BaseModel


class FilterList(BaseModel):
    blacklist: Optional[List[str]] = []
    whitelist: Optional[List[str]] = []


class Filters(BaseModel):
    text: Optional[FilterList]


class TgcfFilter:
    id = "filter"

    def __init__(self, data):
        print("tgcf filter data loaded")
        self.filters = Filters(**data)
        logging.info(self.filters)

    def modify(self, message):
        msg_text = message.text
        if not msg_text:
            return message

        if self.text_safe(msg_text, self.filters.text):
            return message

    def text_safe(self, text, flist: FilterList):
        for forbidden in flist.blacklist:
            if forbidden in text:
                return False
        if not flist.whitelist:
            return True
        for allowed in flist.whitelist:
            if allowed in text:
                return True
