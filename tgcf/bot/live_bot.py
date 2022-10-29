"""A bot to controll settings for tgcf live mode."""

import logging

import yaml
from telethon import events

from tgcf import config, const, plugins
from tgcf.bot.utils import (
    admin_protect,
    display_forwards,
    get_args,
    get_command_prefix,
    remove_source,
)
from tgcf.config import CONFIG, write_config
from tgcf.plugin_models import Style


@admin_protect
async def forward_command_handler(event):
    """Handle the `/forward` command."""
    notes = """The `/forward` command allows you to add a new forward.
    Example: suppose you want to forward from a to (b and c)

    ```
    /forward source: a
    dest: [b,c]
    ```

    a,b,c are chat ids

    """.replace(
        "    ", ""
    )

    try:
        args = get_args(event.message.text)
        if not args:
            raise ValueError(f"{notes}\n{display_forwards(config.CONFIG.forwards)}")

        parsed_args = yaml.safe_load(args)
        forward = config.Forward(**parsed_args)
        try:
            remove_source(forward.source, config.CONFIG.forwards)
        except:
            pass
        CONFIG.forwards.append(forward)
        config.from_to = await config.load_from_to(event.client, config.CONFIG.forwards)

        await event.respond("Success")
        write_config(config.CONFIG)
    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation


@admin_protect
async def remove_command_handler(event):
    """Handle the /remove command."""
    notes = """The `/remove` command allows you to remove a source from forwarding.
    Example: Suppose you want to remove the channel with id -100, then run

    `/remove source: -100`

    """.replace(
        "    ", ""
    )

    try:
        args = get_args(event.message.text)
        if not args:
            raise ValueError(f"{notes}\n{display_forwards(config.CONFIG.forwards)}")

        parsed_args = yaml.safe_load(args)
        source_to_remove = parsed_args.get("source")
        CONFIG.forwards = remove_source(source_to_remove, config.CONFIG.forwards)
        config.from_to = await config.load_from_to(event.client, config.CONFIG.forwards)

        await event.respond("Success")
        write_config(config.CONFIG)
    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation


@admin_protect
async def style_command_handler(event):
    """Handle the /style command"""
    notes = """This command is used to set the style of the messages to be forwarded.

    Example: `/style bold`

    Options are preserve,normal,bold,italics,code, strike

    """.replace(
        "    ", ""
    )

    try:
        args = get_args(event.message.text)
        if not args:
            raise ValueError(f"{notes}\n")
        _valid = [item.value for item in Style]
        if args not in _valid:
            raise ValueError(f"Invalid style. Choose from {_valid}")
        CONFIG.plugins.fmt.style = args
        await event.respond("Success")
        write_config(CONFIG)
    except ValueError as err:
        logging.error(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation


async def start_command_handler(event):
    """Handle the /start command."""
    await event.respond(CONFIG.bot_messages.start)


async def help_command_handler(event):
    """Handle the /help command."""
    await event.respond(CONFIG.bot_messages.bot_help)


def get_events():
    _ = get_command_prefix()
    logging.info(f"Command prefix is . for userbot and / for bot")
    command_events = {
        "start": (start_command_handler, events.NewMessage(pattern=f"{_}start")),
        "forward": (forward_command_handler, events.NewMessage(pattern=f"{_}forward")),
        "remove": (remove_command_handler, events.NewMessage(pattern=f"{_}remove")),
        "style": (style_command_handler, events.NewMessage(pattern=f"{_}style")),
        "help": (help_command_handler, events.NewMessage(pattern=f"{_}help")),
    }

    return command_events
