from enum import Enum
from typing import Optional
from pydantic import BaseModel

CONFIG_FILE = 'tgcf.config.yml'


class Mode(str, Enum):
    past = 'past'
    live = 'live'

class Auth(BaseModel):
    API_ID: int
    API_HASH: str
    USERNAME: str
    BOT_TOKEN: Optional[str]
    PHONE_NO: Optional[str]
    SESSION_STRING: Optional[str]

