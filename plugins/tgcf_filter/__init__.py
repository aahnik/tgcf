import logging
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class FilterList(BaseModel):
    blacklist: Optional[List[str]] = []
    whitelist: Optional[List[str]] = []


class FileType(str, Enum):
    AUDIO = "audio"
    GIF = "gif"
    VIDEO = "video"
    VIDEO_NOTE = "video_note"
    STICKER = "sticker"
    CONTACT = "contact"
    PHOTO = "photo"
    DOCUMENT = "document"
    NOFILE = "nofile"


class FilesFilterList(BaseModel):
    blacklist: Optional[List[FileType]] = []
    whitelist: Optional[List[FileType]] = []


class TextFilter(FilterList):
    case_sensitive: Optional[bool] = False


class Filters(BaseModel):
    users: Optional[FilterList] = FilterList()
    files: Optional[FilesFilterList] = FilesFilterList()
    text: Optional[TextFilter] = TextFilter()


class TgcfFilter:
    id_ = "filter"

    def __init__(self, data):
        print("tgcf filter data loaded")
        self.filters = Filters(**data)
        self.case_correct()
        logging.info(self.filters)

    def case_correct(self):
        textf: TextFilter = self.filters.text

        if textf.case_sensitive is False:
            textf.blacklist = [item.lower() for item in textf.blacklist]
            textf.whitelist = [item.lower() for item in textf.whitelist]

    def modify(self, message):

        if self.users_safe(message):
            if self.files_safe(message):
                if self.text_safe(message):
                    return message

    def text_safe(self, message):
        flist = self.filters.text

        text = message.text
        if not flist.case_sensitive:
            text = text.lower()
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

        def file_type(message):
            file_types = [
                FileType.AUDIO,
                FileType.GIF,
                FileType.VIDEO,
                FileType.VIDEO_NOTE,
                FileType.STICKER,
                FileType.CONTACT,
                FileType.PHOTO,
                FileType.DOCUMENT,
            ]
            for _type in file_types:
                obj = getattr(message, _type)
                if obj:
                    return _type

        fl_type = file_type(message)
        if not fl_type:
            fl_type = FileType.NOFILE
        print(fl_type)
        if fl_type in flist.blacklist:
            return False
        if not flist.whitelist:
            return True
        if fl_type in flist.whitelist:
            return True
