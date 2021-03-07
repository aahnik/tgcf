from pydantic import BaseModel
from typing import List, Optional, Dict
import os
from dotenv import load_dotenv
import json

load_dotenv('.env')


class Forward(BaseModel):
    source: int
    dest: List[int]
    offset: int


class Config(BaseModel):
    forwards: List[Forward]
    # whitelist: Optional[List[str]] = None
    # blacklist: Optional[List[str]] = None
    # replace: Optional[Dict[str,str]] = None
    # block_duplicates: Optional[bool] = False


API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION_STRING = os.getenv('TG_SESSION_STRING')
BOT_TOKEN = os.getenv('BOT_TOKEN')

print(API_HASH, API_ID, BOT_TOKEN)


def load_config() -> Config:
    with open('config.json') as file:
        data = json.load(file)
    return Config(**data)


def write_json(config: Config):
    with open('config.json', 'w') as file:
        json.dump(config, file)


config = load_config()
