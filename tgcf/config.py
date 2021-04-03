# a custom config parser

import os
from typing import List, Optional

import yaml
from pydantic import BaseModel
from telethon.sessions import StringSession

CONFIG_FILE = 'tgcf.config.yml'


class Forward(BaseModel):
    source: int
    dest: List[int]
    offset: Optional[int] = 0


class Config(BaseModel):
    forwards: List[Forward]


def read_config():
    with open(CONFIG_FILE) as file:
        config_dict = yaml.full_load(file)
        try:
            config = Config(**config_dict)
        except Exception as err:
            print(err)
            quit(1)
        else:
            return config


def update_config(config: Config):
    with open(CONFIG_FILE, 'w') as file:
        yaml.dump(config.dict(), file)


def env_var(name: str, optional=False):
    var = os.getenv(name)

    while not var:
        if optional:
            break
        var = input(f'Enter {name}: ')
    return var


API_ID = env_var('API_ID')
API_HASH = env_var('API_HASH')
USERNAME = env_var('USERNAME', optional=True)
SESSION_STRING = env_var('SESSION_STRING', optional=True)

if SESSION_STRING:
    SESSION = StringSession(SESSION_STRING)
else:
    SESSION = 'tgcf'

CONFIG = read_config()
