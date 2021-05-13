"""A bot to controll settings for tgcf live mode."""

import yaml
from telethon import events

from tgcf import config, const
from tgcf.bot.utils import admin_protect, display_forwards, get_args, remove_source


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
            raise ValueError(
                f"{notes}\n{display_forwards(config.CONFIG.forwards)}")

        parsed_args = yaml.safe_load(args)
        print(parsed_args)
        forward = config.Forward(**parsed_args)
        print(forward)
        remove_source(forward.source,config.CONFIG.forwards)
        config.CONFIG.forwards.append(forward)
        config.from_to = config.load_from_to(config.CONFIG.forwards)

        await event.respond("Success")
        config.update_config_file(config.CONFIG)
    except ValueError as err:
        print(err)
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
            raise ValueError(
                f"{notes}\n{display_forwards(config.CONFIG.forwards)}")

        parsed_args = yaml.safe_load(args)
        print(parsed_args)
        source_to_remove = parsed_args.get("source")
        print(source_to_remove)
        config.CONFIG.forwards = remove_source(
            source_to_remove, config.CONFIG.forwards)
        print(config.CONFIG.forwards)
        config.from_to = config.load_from_to(config.CONFIG.forwards)

        await event.respond("Success")
        config.update_config_file(config.CONFIG)
    except ValueError as err:
        print(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation


async def set_command_handler(event):
    pass
    # TODO: allow changing the configuration values


async def start_command_handler(event):
    """Handle the /start command."""
    await event.respond(const.BotMessages.start)


async def help_command_handler(event):
    """Handle the /help command."""
    await event.respond(const.BotMessages.bot_help)


BOT_EVENTS = {
    "bot_start": (start_command_handler, events.NewMessage(pattern="/start")),
    "bot_forward": (forward_command_handler, events.NewMessage(pattern="/forward")),
    "bot_remove": (remove_command_handler, events.NewMessage(pattern="/remove")),
    "bot_help": (help_command_handler, events.NewMessage(pattern="/help")),
}
