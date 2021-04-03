''' This module implements the command line interface for tgcf,
using the modern and robust `typer`.
'''

import os
import asyncio
from enum import Enum
import logging
from typing import Optional

import typer
from dotenv import load_dotenv

from tgcf import __version__


load_dotenv('.env')

FAKE = bool(os.getenv('FAKE'))
app = typer.Typer(add_completion=False)


class Mode(str, Enum):
    '''tgcf works in two modes'''
    past = 'past'
    live = 'live'


def version_callback(value: bool):
    if value:
        print(__version__)
        raise typer.Exit()


def verbosity_callback(value: bool):
    if value:
        logging.info(
            'Verbosity turned on. \nThis is suitable for debugging.\n')
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level)


@app.command()
def main(
        mode: Mode = typer.Argument(...,
                                    help='Choose the mode in which you want to run tgcf.',
                                    envvar='TGCF_MODE'),
        verbose: Optional[bool] = typer.Option(None,
                                               '--loud', '-l',
                                               callback=verbosity_callback,
                                               envvar='LOUD',
                                               help='Increase output verbosity.'),

        version: Optional[bool] = typer.Option(None,
                                               '--version',
                                               '-v',
                                               callback=version_callback,
                                               help='Show version and exit.')

):
    ''' tgcf is a powerful tool for forwarding telegram messages from source to destination.

    Don't forget to star  https://github.com/aahnik/tgcf

    Telegram Channel https://telegram.me/tg_cf
    '''

    if FAKE:
        print(f'mode = {mode}')
        quit(1)

    if mode == mode.past:
        from tgcf.past import forward_job
        asyncio.run(forward_job())
    else:
        from tgcf.live import start_sync
        start_sync()


# AAHNIK 2021
