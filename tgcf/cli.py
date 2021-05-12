"""This module implements the command line interface for tgcf."""

import asyncio
import logging
import os
import sys
from enum import Enum
from typing import Optional

import typer
from dotenv import load_dotenv

from tgcf import __version__

load_dotenv(".env")

FAKE = bool(os.getenv("FAKE"))
app = typer.Typer(add_completion=False)


class Mode(str, Enum):
    """tgcf works in two modes."""

    PAST = "past"
    LIVE = "live"


def version_callback(value: bool):
    """Show current version and exit."""
    if value:
        print(__version__)
        raise typer.Exit()


def verbosity_callback(value: bool):
    """Set logging level."""
    if value:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level)
    logging.info("Verbosity turned on. \nThis is suitable for debugging.\n")


@app.command()
def main(
    mode: Mode = typer.Argument(
        ..., help="Choose the mode in which you want to run tgcf.", envvar="TGCF_MODE"
    ),
    verbose: Optional[bool] = typer.Option(  # pylint: disable=unused-argument
        None,
        "--loud",
        "-l",
        callback=verbosity_callback,
        envvar="LOUD",
        help="Increase output verbosity.",
    ),
    version: Optional[bool] = typer.Option(  # pylint: disable=unused-argument
        None,
        "--version",
        "-v",
        callback=version_callback,
        help="Show version and exit.",
    ),
):
    """Tgcf is a powerful tool for forwarding telegram messages from source to destination.

    Don't forget to star  https://github.com/aahnik/tgcf

    Telegram Channel https://telegram.me/tg_cf
    """
    if FAKE:
        print(f"mode = {mode}")
        sys.exit(1)

    if mode == Mode.PAST:
        from tgcf.past import forward_job  # pylint: disable=import-outside-toplevel

        asyncio.run(forward_job())
    else:
        from tgcf.live import start_sync  # pylint: disable=import-outside-toplevel

        start_sync()


# AAHNIK 2021
