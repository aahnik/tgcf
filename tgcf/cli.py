''' This module implements the command line interface for tgcf,
using the modern and robust `typer`.
'''


from tgcf import __version__
from tgcf.const import Mode
from typing import Optional
import logging
from tgcf.const import Auth
import typer
from dotenv import load_dotenv

from tgcf.main import start_past, start_live
import os
load_dotenv('.env')

FAKE = bool(os.getenv('FAKE'))
app = typer.Typer(add_completion=False)


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


def session_callback(value: str or None):
    pass


@app.command()
def main(
    mode: Mode = typer.Argument(...,
                                help='Choose the mode in which you want to run tgcf.'),



    API_ID: int = typer.Option(...,
                               '--API_ID',
                               help='API ID obtained from my.telegram.org',
                               envvar='API_ID',
                               prompt='Please paste your API ID\
                                (your input will be invisible)',
                               hide_input=True),
    API_HASH: str = typer.Option(...,
                                 '--API_HASH',
                                 help='API HASH obtained from my.telegram.org',
                                 envvar='API_HASH',
                                 prompt='Please paste your API HASH\
                                (your input will be invisible)',
                                 hide_input=True),
    session: str = typer.Option(None,
                                '--session', '-s',
                                help='Path to session file or Session String',
                                envvar='SESSION',
                                callback=session_callback,
                                hide_input=True),
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
        print(f'{API_ID} and {API_HASH}')
        print(f'mode = {mode}')
        quit(1)
    print('normal')

# AAHNIK 2021
