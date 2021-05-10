import yaml
from telethon import events

from tgcf import config

from .utils import display_forwards, get_args, remove_source,admin_protect

@admin_protect
async def forward_command_handler(event):
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
        print(parsed_args)
        forward = config.Forward(**parsed_args)
        print(forward)
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
        print(parsed_args)
        source_to_remove = parsed_args.get("source")
        print(source_to_remove)
        config.CONFIG.forwards = remove_source(source_to_remove, config.CONFIG.forwards)
        print(config.CONFIG.forwards)
        config.from_to = config.load_from_to(config.CONFIG.forwards)

        await event.respond("Success")
        config.update_config_file(config.CONFIG)
    except ValueError as err:
        print(err)
        await event.respond(str(err))

    finally:
        raise events.StopPropagation


async def start_command_handler(event):
    await event.respond("I am alive!")


async def help_command_handler(event):
    await event.respond(
        "Please read the documentation at https://github.com/aahnik/tgcf"
    )
