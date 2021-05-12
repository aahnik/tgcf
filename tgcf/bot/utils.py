"""helper functions for the bot."""
from typing import List

from telethon import events

from tgcf import config
from tgcf.config import Forward


def admin_protect(org_func):
    """Decorate to restrict non admins from accessing the bot."""
    if config.CONFIG.admins == []:
        return org_func

    async def wrapper_func(event):
        """Wrap the original function."""
        if event.sender_id not in config.CONFIG.admins:
            await event.respond("You are not authorized.")
            raise events.StopPropagation
        return await org_func(event)

    return wrapper_func


def get_args(text: str):
    """Return the part of message following the command."""
    splitted = text.split(" ", 1)

    if not len(splitted) == 2:
        return ""

    prefix, args = splitted
    print(prefix)
    args = args.strip()
    print(args)
    return args


def display_forwards(forwards: List[Forward]):
    """Return a string that beautifully displays all current forwards."""
    if len(forwards) == 0:
        return "Currently no forwards are set"
    forward_str = "This is your configuration"
    for forward in forwards:
        forward_str = (
            forward_str
            + f"\n\n```\nsource: {forward.source}\ndest: {forward.dest}\n```\n"
        )

    return forward_str


def remove_source(source, forwards: List[Forward]):
    """Remove a source from forwards."""
    for i, forward in enumerate(forwards):
        print(forward)
        print(type(forward.source))
        print(type(source))
        if forward.source == source:
            del forwards[i]
            return forwards
    raise ValueError("The source does not exist")
