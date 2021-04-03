''' This module implements the command line interface for tgcf,
using the modern and robust `typer`.
'''


from tgcf import __version__
from typing import Optional
import logging
from enum import Enum
import typer
from dotenv import load_dotenv
from tgcf.main import start_past, start_live
import os
load_dotenv('.env')

FAKE = bool(os.getenv('FAKE'))
app = typer.Typer(add_completion=False)


class Mode(str, Enum):
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
                                    help='Choose the mode in which you want to run tgcf.'),
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
        start_past()
    else:
        start_live()


# AAHNIK 2021
