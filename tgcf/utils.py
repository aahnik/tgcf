"""Utility functions to smoothen your life."""

from tgcf.config import CONFIG


async def send_message(client, *args):
    """Forward or send a copy, depending on config."""
    # show forwarded from
    if CONFIG.show_forwarded_from:
        return await client.forward_messages(*args)
    return await client.send_message(*args)
