from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel
from watermark import Position


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


class FilterList(BaseModel):
    blacklist: List[str] = []
    whitelist: List[str] = []


class FilesFilterList(BaseModel):
    blacklist: List[FileType] = []
    whitelist: List[FileType] = []


class TextFilter(FilterList):
    case_sensitive: bool = False
    regex: bool = False


class Style(str, Enum):
    BOLD = "bold"
    ITALICS = "italics"
    CODE = "code"
    STRIKE = "strike"
    PLAIN = "plain"
    PRESERVE = "preserve"


STYLE_CODES = {"bold": "**", "italics": "__", "code": "`", "strike": "~~", "plain": ""}

# define plugin configs


class Filters(BaseModel):
    check: bool = False
    users: FilterList = FilterList()
    files: FilesFilterList = FilesFilterList()
    text: TextFilter = TextFilter()


class Format(BaseModel):
    check: bool = False
    style: Style = Style.PRESERVE


class MarkConfig(BaseModel):
    check: bool = False
    image: str = "image.png"
    position: Position = Position.centre
    frame_rate: int = 15


class OcrConfig(BaseModel):
    check: bool = False


class Replace(BaseModel):
    check: bool = False
    text: Dict[str, str] = {}
    text_raw: str = ""
    regex: bool = False


class Caption(BaseModel):
    check: bool = False
    header: str = ""
    footer: str = ""

class Sender(BaseModel):
    check: bool = False
    user_type: int = 0  # 0:bot, 1:user
    BOT_TOKEN: str = ""
    SESSION_STRING: str = ""

class PluginConfig(BaseModel):
    filter: Filters = Filters()
    fmt: Format = Format()
    mark: MarkConfig = MarkConfig()
    ocr: OcrConfig = OcrConfig()
    replace: Replace = Replace()
    caption: Caption = Caption()
    sender: Sender = Sender()


# List of plugins that need to load asynchronously
ASYNC_PLUGIN_IDS = ['sender']