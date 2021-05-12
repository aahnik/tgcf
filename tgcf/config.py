"""Load all user defined config and env vars."""

import logging
import os
import sys
from typing import Dict, List, Optional, Union

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, validator  # pylint: disable=no-name-in-module
from telethon.sessions import StringSession

from tgcf.const import CONFIG_ENV_VAR_NAME, CONFIG_FILE_NAME

load_dotenv()


class Forward(BaseModel):
    """Blueprint for the forward object."""

    # pylint: disable=too-few-public-methods
    source: Union[int, str]
    dest: List[Union[int, str]]
    offset: Optional[int] = 0
    end: Optional[int] = None


class LiveSettings(BaseModel):
    """Settings to configure how tgcf operates in live mode."""

    # pylint: disable=too-few-public-methods
    delete_sync: bool = False
    delete_on_edit: Optional[str] = None


class PastSettings(BaseModel):
    """Configuration for past mode."""

    # pylint: disable=too-few-public-methods
    delay: Optional[float] = 0

    @validator("delay")
    def validate_delay(cls, val):  # pylint: disable=no-self-use,no-self-argument
        """Check if the delay used by user is values. If not, use closest logical values."""
        if val not in range(0, 101):
            logging.warning("delay must be within 0 to 100 seconds")
            if val > 100:
                val = 100
            if val < 0:
                val = 0
        return val


class Config(BaseModel):
    """The blueprint for tgcf's whole config."""

    # pylint: disable=too-few-public-methods
    forwards: List[Forward] = []
    show_forwarded_from: bool = False
    live: LiveSettings = LiveSettings()
    past: PastSettings = PastSettings()
    admins: List[int] = []

    plugins: Optional[Dict] = {}


def detect_config_type() -> int:
    """Return 0 when no config found, 1 when tgcf.config.yml, 2 when env var, else terminate."""
    tutorial_link = "Learn more http://bit.ly/configure-tgcf"

    if CONFIG_FILE_NAME in os.listdir():
        logging.info(f"{CONFIG_FILE_NAME} detected.")
        return 1
    if os.getenv("TGCF_CONFIG"):
        logging.info(f"env var {CONFIG_ENV_VAR_NAME} detected.")
        if not ".env" in os.listdir():
            return 2

        logging.warning(
            f"If you can create files in your system,\
            you should use tgcf.config.yml and not .env to define configuration. {tutorial_link}"
        )
        sys.exit(1)
    else:
        return 0


CONFIG_TYPE = detect_config_type()


def read_config() -> Config:
    """Load the configuration defined by user."""
    if CONFIG_TYPE == 1:
        with open(CONFIG_FILE_NAME) as file:
            config_dict = yaml.full_load(file)
    elif CONFIG_TYPE == 2:
        config_env_var = os.getenv("TGCF_CONFIG")
        config_dict = yaml.full_load(config_env_var)
    else:
        return Config()

    try:
        if config_dict:
            config = Config(**config_dict)
        else:
            config = Config()
    except Exception as err:
        print(err)
        sys.exit(1)
    else:
        logging.info(config)
        return config


def update_config_file(config: Config):
    """Write changes in config back to file."""
    if CONFIG_TYPE == 1 or CONFIG_TYPE == 0:
        with open(CONFIG_FILE_NAME, "w") as file:
            yaml.dump(config.dict(), file)
    elif CONFIG_TYPE == 2:
        logging.warning("Could not update config! As env var is used")


def get_env_var(name: str, optional=False):
    """Fetch an env var."""
    var = os.getenv(name, "")

    while not var:
        if optional:
            return ""
        var = input(f"Enter {name}: ")
    return var


API_ID = get_env_var("API_ID")
API_HASH = get_env_var("API_HASH")
USERNAME = get_env_var("USERNAME", optional=True)
SESSION_STRING = get_env_var("SESSION_STRING", optional=True)
BOT_TOKEN = get_env_var("BOT_TOKEN", optional=True)

if SESSION_STRING:
    SESSION = StringSession(SESSION_STRING)
elif BOT_TOKEN:
    SESSION = "tgcf_bot"
else:
    SESSION = "tgcf_user"

CONFIG = read_config()


def load_from_to(forwards: List[Forward]):
    """Load a from -> to mapping."""
    from_to_dict = {}
    for forward in forwards:
        from_to_dict[forward.source] = forward.dest
    return from_to_dict


from_to = load_from_to(CONFIG.forwards)

logging.info("config.py got executed")
