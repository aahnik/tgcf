import logging
from typing import List, Optional

from pydantic import BaseModel


class FilterList(BaseModel):
    blacklist: Optional[List[str or int]] = []
    whitelist: Optional[List[str or int]] = []


class Filters(BaseModel):
    users: Optional[FilterList] = FilterList()
    files: Optional[FilterList] = FilterList()
    text: Optional[FilterList] = FilterList()


class TgcfFilter:
    id = "filter"

    def __init__(self, data):
        print("tgcf filter data loaded")
        self.filters = Filters(**data)
        logging.info(self.filters)

    def modify(self, message):

        if self.users_safe(message):
            if self.files_safe(message):
                if self.text_safe(message):
                    return message

    def text_safe(self, message):
        flist = self.filters.text
        text = message.text
        if not text and flist.whitelist == []:
            return True
        for forbidden in flist.blacklist:
            if forbidden in text:
                return False
        if not flist.whitelist:
            return True
        for allowed in flist.whitelist:
            if allowed in text:
                return True

    def users_safe(self, message):
        flist = self.filters.users
        sender = str(message.sender_id)
        logging.info(f"M message from sender id {sender}")
        if sender in flist.blacklist:
            return False
        if not flist.whitelist:
            return True
        if sender in flist.whitelist:
            return True

    def files_safe(self, message):
        flist = self.filters.files
        return True
