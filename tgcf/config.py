# a custom config parser

import logging
import os
import sys
from typing import Dict, List, Optional, Union

import yaml
from pydantic import BaseModel
from telethon.sessions import StringSession

CONFIG_FILE_NAME = "tgcf.config.yml"
CONFIG_ENV_VAR_NAME = "TGCF_CONFIG"


class Forward(BaseModel):
    source: Union[int, str]
    dest: List[Union[int, str]]
    offset: Optional[int] = 0


class LiveSettings(BaseModel):
    delete_sync: Optional[bool] = False


class Config(BaseModel):
    forwards: List[Forward]
    show_forwarded_from: Optional[bool] = False
    live: Optional[LiveSettings] = LiveSettings()

    plugins: Optional[Dict] = {}


def detect_config_type() -> int:
    # return 1 when tgcf.config.yml
    # 2 when env var
    # else terminate
    tutorial_link = "Learn more http://bit.ly/configure-tgcf"

    if CONFIG_FILE_NAME in os.listdir():
        logging.info(f"{CONFIG_FILE_NAME} detected.")
        return 1
    elif os.getenv("TGCF_CONFIG"):
        logging.info(f"env var {CONFIG_ENV_VAR_NAME} detected.")
        if not ".env" in os.listdir():
            return 2
        else:
            logging.warning(
                f"If you can create files in your system, you should use tgcf.config.yml and not .env to define configuration. {tutorial_link}"
            )
            sys.exit(1)
    else:
        logging.warning(f"Configuration not found! {tutorial_link}")
        sys.exit(1)


CONFIG_TYPE = detect_config_type()


def read_config_file() -> Config:
    if CONFIG_TYPE == 1:
        with open(CONFIG_FILE_NAME) as file:
            config_dict = yaml.full_load(file)
    elif CONFIG_TYPE == 2:
        config_env_var = os.getenv("TGCF_CONFIG")
        config_dict = yaml.full_load(config_env_var)
    else:
        logging.warning("This should never happen!")

    try:
        config = Config(**config_dict)
    except Exception as err:
        print(err)
        sys.exit(1)
    else:
        logging.info(config)
        return config


def update_config_file(config: Config):
    if CONFIG_TYPE == 1:
        with open(CONFIG_FILE_NAME, "w") as file:
            yaml.dump(config.dict(), file)
    elif CONFIG_TYPE == 2:
        logging.warning("Could not update config! As env var is used")


def get_env_var(name: str, optional=False):
    var = os.getenv(name)

    while not var:
        if optional:
            break
        var = input(f"Enter {name}: ")
    return var


API_ID = get_env_var("API_ID")
API_HASH = get_env_var("API_HASH")
USERNAME = get_env_var("USERNAME", optional=True)
SESSION_STRING = get_env_var("SESSION_STRING", optional=True)

if SESSION_STRING:
    SESSION = StringSession(SESSION_STRING)
else:
    SESSION = "tgcf"

CONFIG = read_config_file()

logging.info("config.py got executed")
