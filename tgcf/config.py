"""Load all user defined config and env vars."""

import logging
import os
import sys
from typing import Any, Dict, List, Optional, Union

from dotenv import load_dotenv
from pydantic import BaseModel, validator  # pylint: disable=no-name-in-module
from pymongo import MongoClient
from telethon import TelegramClient
from telethon.sessions import StringSession

from tgcf import storage as stg
from tgcf.const import CONFIG_FILE_NAME
from tgcf.plugin_models import PluginConfig

pwd = os.getcwd()
env_file = os.path.join(pwd, ".env")

load_dotenv(env_file)


class Forward(BaseModel):
    """Blueprint for the forward object."""

    # pylint: disable=too-few-public-methods
    con_name: str = ""
    use_this: bool = True
    source: Union[int, str] = ""
    dest: List[Union[int, str]] = []
    offset: int = 0
    end: Optional[int] = 0

    agent: int = 0  # the agent id to use for this connection
    plugin_cfg: int = 0  # the plugin configuration id to use for this connection


class LiveSettings(BaseModel):
    """Settings to configure how tgcf operates in live mode."""

    # pylint: disable=too-few-public-methods
    sequential_updates: bool = False
    delete_sync: bool = False
    delete_on_edit: Optional[str] = ".deleteMe"


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


# class LoginConfig(BaseModel):

#     API_ID: int = 0
#     API_HASH: str = ""


#     user_type: int = 0  # 0:bot, 1:user
#     phone_no: int = 91
#     USERNAME: str = ""
#     SESSION_STRING: str = ""
#     BOT_TOKEN: str = ""


class TgAPIConfig(BaseModel):
    API_ID: int = 0
    API_HASH: str = ""


class AgentLoginConfig(BaseModel):
    alias: str = ""
    user_type: int = 0  # 0:bot, 1:user
    phone_no: int = 91
    USERNAME: str = ""
    SESSION_STRING: str = ""
    BOT_TOKEN: str = ""
    is_active: bool = False


class AgentForwardingConfig(BaseModel):
    show_forwarded_from: bool = False
    mode: int = 0  # 0: live, 1:past
    live: LiveSettings = LiveSettings()
    past: PastSettings = PastSettings()
    pid:int = 0


class LoginConfig(BaseModel):
    tg: TgAPIConfig = TgAPIConfig()
    agents: List[AgentLoginConfig] = [AgentLoginConfig()]


class BotMessages(BaseModel):
    start: str = "Hi! I am alive"
    bot_help: str = "For details visit github.com/aahnik/tgcf"


class Config(BaseModel):
    """The blueprint for tgcf's whole config."""

    # pylint: disable=too-few-public-
    pids: List[int] = []
    theme: str = "light"
    login_cfg: LoginConfig = LoginConfig()
    admins: List[Union[int, str]] = []
    forwards: List[Forward] = []
    agent_fwd_cfg: List[AgentForwardingConfig] = [AgentForwardingConfig()]
    plugin_cfgs: List[PluginConfig] = [PluginConfig()]
    bot_messages = BotMessages()


def write_config_to_file(config: Config):
    with open(CONFIG_FILE_NAME, "w", encoding="utf8") as file:
        file.write(config.json())


def detect_config_type() -> int:
    if os.getenv("MONGO_CON_STR"):
        if MONGO_CON_STR:
            logging.info("Using mongo db for storing config!")
            client = MongoClient(MONGO_CON_STR)
            stg.mycol = setup_mongo(client)
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


def read_config(count=1) -> Config:
    """Load the configuration defined by user."""
    if count > 3:
        logging.warning("Failed to read config, returning default config")
        return Config()
    if count != 1:
        logging.info(f"Trying to read config time:{count}")
    try:
        if stg.CONFIG_TYPE == 1:
            with open(CONFIG_FILE_NAME, encoding="utf8") as file:
                return Config.parse_raw(file.read())
        elif stg.CONFIG_TYPE == 2:
            return read_db()
        else:
            return Config()
    except Exception as err:
        logging.warning(err)
        stg.CONFIG_TYPE = detect_config_type()
        return read_config(count=count + 1)


def write_config(config: Config, persist=True):
    """Write changes in config back to file."""
    if stg.CONFIG_TYPE == 1 or stg.CONFIG_TYPE == 0:
        write_config_to_file(config)
    elif stg.CONFIG_TYPE == 2:
        if persist:
            update_db(config)


def get_env_var(name: str, optional: bool = False) -> str:
    """Fetch an env var."""
    var = os.getenv(name, "")

    while not var:
        if optional:
            return ""
        var = input(f"Enter {name}: ")
    return var


async def get_id(client: TelegramClient, peer):
    return await client.get_peer_id(peer)


async def load_active_forwards(agent_id: int, forwards: List[Forward]) -> List[Forward]:
    active_forwards: List[Forward] = []
    for forward in forwards:
        if forward.agent != agent_id:
            continue
        if not forward.use_this:
            continue
        active_forwards.append(forward)
    return active_forwards


async def load_from_to(
    agent_id: int,
    client: TelegramClient,
    forwards: List[Forward],
) -> Dict[int, Dict[str, List[int] | int]]:
    """Convert a list of Forward objects to a mapping.
    The active connections of current agent are included.

    Args:
        client: Instance of Telegram client (logged in)
        forwards: List of Forward objects

    Returns:
        Dict: key = chat id of source
                value = dict
                dest: List of chat ids of destinations
                pcgf: id of plugin config to use

    Notes:
    -> The Forward objects may contain username/phn no/links
    -> But this mapping strictly contains signed integer chat ids
    -> Chat ids are essential for how storage is implemented
    -> Storage is essential for edit, delete and reply syncs
    """
    from_to_dict: dict = {}

    async def _(peer):
        return await get_id(client, peer)

    for forward in forwards:
        if forward.agent != agent_id:
            continue
        if not forward.use_this:
            continue
        source = forward.source
        if not isinstance(source, int) and source.strip() == "":
            continue
        src = await _(forward.source)
        # from_to_dict[src] = {
        #     "dest": [], # the list of destination entities
        #     "pcfg": 0 # id of the plugin config to use
        # }
        from_to_dict[src] = {}
        from_to_dict[src]["dest"] = [await _(dest) for dest in forward.dest]
        from_to_dict[src]["pcfg"] = forward.plugin_cfg
    logging.info(f"From to dict is {from_to_dict}")
    return from_to_dict


async def load_admins(client: TelegramClient):
    for admin in CONFIG.admins:
        ADMINS.append(await get_id(client, admin))
    logging.info(f"Loaded admins are {ADMINS}")
    return ADMINS


def setup_mongo(client):

    mydb = client[MONGO_DB_NAME]
    mycol = mydb[MONGO_COL_NAME]
    if not mycol.find_one({"_id": 0}):
        mycol.insert_one({"_id": 0, "author": "tgcf", "config": Config().dict()})

    return mycol


def update_db(cfg):
    stg.mycol.update_one({"_id": 0}, {"$set": {"config": cfg.dict()}})


def read_db():
    obj = stg.mycol.find_one({"_id": 0})
    cfg = Config(**obj["config"])
    return cfg


PASSWORD = os.getenv("PASSWORD", "tgcf")
ADMINS: List = []

MONGO_CON_STR = os.getenv("MONGO_CON_STR")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "tgcf-config")
MONGO_COL_NAME = os.getenv("MONGO_COL_NAME", "tgcf-instance-0")

stg.CONFIG_TYPE = detect_config_type()
CONFIG = read_config()

if PASSWORD == "tgcf":
    logging.warn(
        "You have not set a password to protect the web access to tgcf.\nThe default password `tgcf` is used."
    )
from_to: Dict[int, Dict[str, int | List[int]]] = {}
is_bot: Optional[bool] = None
logging.info("config.py got executed")


def get_SESSION(
    agent_id: int, login_cfg: LoginConfig = CONFIG.login_cfg, default: str = "tgcf_bot"
):
    # TODO: validate agent_id
    agent = login_cfg.agents[agent_id]
    if agent.SESSION_STRING and agent.user_type == 1:
        logging.info("using session string")
        SESSION = StringSession(agent.SESSION_STRING)
    elif agent.BOT_TOKEN and agent.user_type == 0:
        logging.info("using bot account")
        SESSION = default + str(agent_id)
    else:
        logging.warning("Login information not set!")
        sys.exit()
    logging.info(SESSION)
    return SESSION
