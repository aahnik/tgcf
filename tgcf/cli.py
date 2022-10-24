"""This module implements the command line interface for tgcf."""

import asyncio
import logging
import os
import platform
import sys
import time
from enum import Enum
from typing import Optional

import typer
from dotenv import load_dotenv
from pyfiglet import Figlet
from rich import console, traceback
from rich.logging import RichHandler
from verlat import latest_release

from tgcf import __version__

load_dotenv(".env")

FAKE = bool(os.getenv("FAKE"))
app = typer.Typer(add_completion=False)

con = console.Console()


def topper():
    fig = Figlet(font="speed")
    rendered = fig.renderText("tgcf")
    time_passed = 0

    while time_passed < 5:
        cmd = "clear" if os.name == "posix" else "cls"
        os.system(cmd)
        if time_passed % 2 == 0:
            print(rendered)
        else:
            con.print(rendered)
        time.sleep(0.5)
        time_passed += 1
    version_check()
    print("\n")


class Mode(str, Enum):
    """tgcf works in two modes."""

    PAST = "past"
    LIVE = "live"


def verbosity_callback(value: bool):
    """Set logging level."""
    traceback.install()
    if value:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[
            RichHandler(
                rich_tracebacks=True,
                markup=True,
            )
        ],
    )
    topper()
    logging.info("Verbosity turned on! This is suitable for debugging")
    nl = "\n"
    logging.info(
        f"""Running tgcf {__version__}\
    \nPython {sys.version.replace(nl,"")}\
    \nOS {os.name}\
    \nPlatform {platform.system()} {platform.release()}\
    \n{platform.architecture()} {platform.processor()}"""
    )


def version_callback(value: bool):
    """Show current version and exit."""

    if value:
        con.print(__version__)
        raise typer.Exit()


def version_check():
    latver = latest_release("tgcf").version
    if __version__ != latver:
        con.print(
            f"tgcf has a newer release {latver} availaible!\
            \nVisit http://bit.ly/update-tgcf",
            style="bold yellow",
        )


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
    """The ultimate tool to automate custom telegram message forwarding.

    Source Code: https://github.com/aahnik/tgcf

    For updates join telegram channel @aahniks_code
    """
    if FAKE:
        logging.critical(f"You are running fake with {mode} mode")
        sys.exit(1)

    if mode == Mode.PAST:
        from tgcf.past import forward_job  # pylint: disable=import-outside-toplevel

        asyncio.run(forward_job())
    else:
        from tgcf.live import start_sync  # pylint: disable=import-outside-toplevel

        asyncio.run(start_sync())


# AAHNIK 2021
