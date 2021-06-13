"""Load all user defined config and env vars."""

import logging
import os
import sys
from typing import Dict, List, Optional, Union

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, validator  # pylint: disable=no-name-in-module
from telethon import TelegramClient
from telethon.sessions import StringSession

from tgcf.const import CONFIG_ENV_VAR_NAME, CONFIG_FILE_NAME

load_dotenv()


class Forward(BaseModel):
    """Blueprint for the forward object."""

    # pylint: disable=too-few-public-methods
    source: Union[int, str]
    dest: List[Union[int, str]] = []
    offset: int = 0
    end: Optional[int] = 0


class LiveSettings(BaseModel):
    """Settings to configure how tgcf operates in live mode."""

    # pylint: disable=too-few-public-methods
    delete_sync: bool = False
    delete_on_edit: Optional[str] = None


class PastSettings(BaseModel):
    """Configuration for past mode."""

    # pylint: disable=too-few-public-methods
    delay: float = 0

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
    admins: List[Union[int, str]] = []
    forwards: List[Forward] = []
    show_forwarded_from: bool = False
    live: LiveSettings = LiveSettings()
    past: PastSettings = PastSettings()

    plugins: Dict = {}


def detect_config_type() -> int:
    """Return 0 when no config found, 1 when tgcf.config.yml, 2 when env var, else terminate."""
    tutorial_link = "Learn more http://bit.ly/configure-tgcf"

    if CONFIG_FILE_NAME in os.listdir():
        logging.info(f"{CONFIG_FILE_NAME} detected")
        return 1
    if os.getenv("TGCF_CONFIG"):
        logging.info(f"env var {CONFIG_ENV_VAR_NAME} detected")
        if not ".env" in os.listdir():
            return 2

        logging.warning(
            f"If you can create files in your system,\
            you should use tgcf.config.yml and not .env to define configuration {tutorial_link}"
        )
        sys.exit(1)
    else:
        return 0


CONFIG_TYPE = detect_config_type()


def read_config() -> Config:
    """Load the configuration defined by user."""
    if CONFIG_TYPE == 1:
        with open(CONFIG_FILE_NAME, encoding="utf8") as file:
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
        logging.exception(err)
        sys.exit(1)
    else:
        logging.info(config)
        return config


def write_config(config: Config):
    """Write changes in config back to file."""
    if CONFIG_TYPE == 1 or CONFIG_TYPE == 0:
        with open(CONFIG_FILE_NAME, "w", encoding="utf8") as file:
            yaml.dump(config.dict(), file, sort_keys=False, allow_unicode=True)
    elif CONFIG_TYPE == 2:
        logging.warning("Could not update config! As env var is used")


def get_env_var(name: str, optional: bool = False) -> str:
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


async def get_id(client: TelegramClient, peer):
    return await client.get_peer_id(peer)


async def load_from_to(
    client: TelegramClient, forwards: List[Forward]
) -> Dict[int, List[int]]:
    """Convert a list of Forward objects to a mapping.

    Args:
        client: Instance of Telegram client (logged in)
        forwards: List of Forward objects

    Returns:
        Dict: key = chat id of source
                value = List of chat ids of destinations

    Notes:
    -> The Forward objects may contain username/phn no/links
    -> But this mapping strictly contains signed integer chat ids
    -> Chat ids are essential for how storage is implemented
    -> Storage is essential for edit, delete and reply syncs
    """
    from_to_dict = {}

    async def _(peer):
        return await get_id(client, peer)

    for forward in forwards:
        src = await _(forward.source)
        from_to_dict[src] = [await _(dest) for dest in forward.dest]
    logging.info(f"From to dict is {from_to_dict}")
    return from_to_dict


ADMINS = []


async def load_admins(client: TelegramClient):
    for admin in CONFIG.admins:
        ADMINS.append(await get_id(client, admin))
    logging.info(f"Loaded admins are {ADMINS}")
    return ADMINS


from_to = {}
is_bot: Optional[bool] = None
logging.info("config.py got executed")
