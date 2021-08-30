"""helper functions for the bot."""
import logging
from typing import List

from telethon import events

from tgcf import config
from tgcf.config import Forward


def admin_protect(org_func):
    """Decorate to restrict non admins from accessing the bot."""

    async def wrapper_func(event):
        """Wrap the original function."""
        logging.info(f"Applying admin protection for {event.sender_id}! Admins are {config.ADMINS}")
        if event.sender_id not in config.ADMINS:
            await event.respond(const.BotMessages.user_not_admin)
            raise events.StopPropagation
        return await org_func(event)

    return wrapper_func


def get_args(text: str) -> str:
    """Return the part of message following the command."""
    splitted = text.split(" ", 1)

    if not len(splitted) == 2:
        splitted = text.split("\n", 1)
        if not len(splitted) == 2:
            return ""

    prefix, args = splitted
    args = args.strip()
    logging.info(f"Got command {prefix} with args {args}")
    return args


def display_forwards(forwards: List[Forward]) -> str:
    """Return a string that beautifully displays all current forwards."""
    if len(forwards) == 0:
        return const.BotMessages.display_forwards_empty
    forward_str = const.BotMessages.forward_str_title
    for forward in forwards:
        forward_str = (
                forward_str
                + f"\n\n```\n{const.BotMessages.forward_str_source} {forward.source}\n{const.BotMessages.forward_str_destination} {forward.dest}\n```\n"
        )

    return forward_str


def remove_source(source, forwards: List[Forward]) -> List[Forward]:
    """Remove a source from forwards."""
    for i, forward in enumerate(forwards):
        if forward.source == source:
            del forwards[i]
            return forwards
    raise ValueError(const.BotMessages.remove_source_not_exists)


def get_command_prefix():
    if config.is_bot is None:
        raise ValueError("config.is_bot is not set!")
    return "/" if config.is_bot else r"\."
