"""Load all user defined config and env vars."""

import logging
import os
import sys
from typing import Dict, List, Optional, Union

from dotenv import load_dotenv
from pydantic import BaseModel, validator  # pylint: disable=no-name-in-module
from telethon import TelegramClient
from telethon.sessions import StringSession

from tgcf.const import CONFIG_ENV_VAR_NAME, CONFIG_FILE_NAME
from tgcf.plugin_models import PluginConfig

load_dotenv()


class Forward(BaseModel):
    """Blueprint for the forward object."""

    # pylint: disable=too-few-public-methods
    source: Union[int, str] = ""
    dest: List[Union[int, str]] = []
    offset: int = 0
    end: Optional[int] = 0


class LiveSettings(BaseModel):
    """Settings to configure how tgcf operates in live mode."""

    # pylint: disable=too-few-public-methods
    delete_sync: bool = False
    delete_on_edit: Optional[str] = ""


class PastSettings(BaseModel):
    """Configuration for past mode."""

    # pylint: disable=too-few-public-methods
    delay: int = 0

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


class LoginConfig(BaseModel):

    API_ID: int = 0
    API_HASH: str = ""
    user_type: int = 0  # 0:bot, 1:user
    phone_no: int = 91
    USERNAME: str = ""
    SESSION_STRING: str = ""
    BOT_TOKEN: str = ""


class Config(BaseModel):
    """The blueprint for tgcf's whole config."""

    # pylint: disable=too-few-public-
    pid: int = 0
    login: LoginConfig = LoginConfig()
    admins: List[Union[int, str]] = []
    forwards: List[Forward] = []
    show_forwarded_from: bool = False
    mode: int = 0  # 0: live, 1:past
    live: LiveSettings = LiveSettings()
    past: PastSettings = PastSettings()

    plugins: PluginConfig = PluginConfig()


def write_config_to_file(config: Config):
    with open(CONFIG_FILE_NAME, "w", encoding="utf8") as file:
        file.write(config.json())


def detect_config_type() -> int:
    if os.getenv("MONGO"):
        return 2
    if CONFIG_FILE_NAME in os.listdir():
        logging.info(f"{CONFIG_FILE_NAME} detected!")
        return 1

    else:
        logging.info(
            "config file not found. mongo not found. creating local config file."
        )
        cfg = Config()
        write_config_to_file(cfg)
        logging.info(f"{CONFIG_FILE_NAME} created!")
        return 1


CONFIG_TYPE = detect_config_type()


def read_config() -> Config:
    """Load the configuration defined by user."""
    if CONFIG_TYPE == 1:
        with open(CONFIG_FILE_NAME, encoding="utf8") as file:
            return Config.parse_raw(file.read())
    elif CONFIG_TYPE == 2:
        print("load data from mongodb server")
    else:
        return Config()


def write_config(config: Config):
    """Write changes in config back to file."""
    if CONFIG_TYPE == 1 or CONFIG_TYPE == 0:
        write_config_to_file(config)
    elif CONFIG_TYPE == 2:
        logging.warning("upcoming feature:write to mongo")


def get_env_var(name: str, optional: bool = False) -> str:
    """Fetch an env var."""
    var = os.getenv(name, "")

    while not var:
        if optional:
            return ""
        var = input(f"Enter {name}: ")
    return var


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
        source = forward.source
        if type(source) != int and source.strip() == "":
            continue
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


def get_SESSION():
    if CONFIG.login.SESSION_STRING and CONFIG.login.user_type == 1:
        logging.info("using session string")
        SESSION = StringSession(CONFIG.login.SESSION_STRING)
    elif CONFIG.login.BOT_TOKEN and CONFIG.login.user_type == 0:
        logging.info("using bot account")
        SESSION = "tgcf_bot"
    else:
        logging.warning("Login information not set!")
        sys.exit()
    return SESSION


PASSWORD = os.getenv("PASSWORD", "tgcf")
if PASSWORD == "tgcf":
    logging.warn(
        "You have not set a password to protect the web access to tgcf.\nThe default password `tgcf` is used."
    )
from_to = {}
is_bot: Optional[bool] = None
logging.info("config.py got executed")

with open("logs.txt", "w") as file:
    file.write("config file loaded")
