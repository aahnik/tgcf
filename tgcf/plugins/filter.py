import logging
from typing import Any, Dict, List

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from tgcf.plugins import FileType, TgcfMessage, TgcfPlugin
from tgcf.utils import match


class FilterList(BaseModel):
    blacklist: List[str] = []
    whitelist: List[str] = []


class FilesFilterList(BaseModel):
    blacklist: List[FileType] = []
    whitelist: List[FileType] = []


class TextFilter(FilterList):
    case_sensitive: bool = False
    regex: bool = False


class Filters(BaseModel):
    users: FilterList = FilterList()
    files: FilesFilterList = FilesFilterList()
    text: TextFilter = TextFilter()


class TgcfFilter(TgcfPlugin):
    id_ = "filter"

    def __init__(self, data: Dict[str, Any]) -> None:
        self.filters = Filters(**data)
        self.case_correct()
        logging.info(self.filters)

    def case_correct(self) -> None:
        textf: TextFilter = self.filters.text

        if textf.case_sensitive is False and textf.regex is False:
            textf.blacklist = [item.lower() for item in textf.blacklist]
            textf.whitelist = [item.lower() for item in textf.whitelist]

    def modify(self, tm: TgcfMessage) -> TgcfMessage:

        if self.users_safe(tm):
            logging.info("Message passed users filter")
            if self.files_safe(tm):
                logging.info("Message passed files filter")
                if self.text_safe(tm):
                    logging.info("Message passed text filter")
                    return tm

    def text_safe(self, tm: TgcfMessage) -> bool:
        flist = self.filters.text

        text = tm.text
        if not flist.case_sensitive:
            text = text.lower()
        if not text and flist.whitelist == []:
            return True

        # first check if any blacklisted pattern is present
        for forbidden in flist.blacklist:
            if match(forbidden, text, self.filters.text.regex):
                return False  # when a forbidden pattern is found

        if not flist.whitelist:
            return True  # if no whitelist is present

        # if whitelist is present
        for allowed in flist.whitelist:
            if match(allowed, text, self.filters.text.regex):
                return True  # only when atleast one whitelisted pattern is found

    def users_safe(self, tm: TgcfMessage) -> bool:
        flist = self.filters.users
        sender = str(tm.sender_id)
        if sender in flist.blacklist:
            return False
        if not flist.whitelist:
            return True
        if sender in flist.whitelist:
            return True

    def files_safe(self, tm: TgcfMessage) -> bool:
        flist = self.filters.files
        fl_type = tm.file_type
        if fl_type in flist.blacklist:
            return False
        if not flist.whitelist:
            return True
        if fl_type in flist.whitelist:
            return True
