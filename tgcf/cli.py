''' This module implements the command line interface for tgcf,
using the modern and robust `typer`.
'''

from enum import Enum

from tgcf import __version__
from typing import Optional
import logging

import typer
from dotenv import load_dotenv

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
        name: str = typer.Option(...,
                                 '--name', '-n',
                                 help='Name of the bot/userbot you want to run.',
                                 envvar='NAME',
                                 prompt='Please enter the bot/userbot username'),

        token: str = typer.Option(...,
                                  '--token', '-t',
                                  help='Bot Token or Session String',
                                  envvar='TOKEN',
                                  prompt='Please paste the Bot Token or Session String \
                                (your input will be invisible)',
                                  hide_input=True),
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

    config_file: str = typer.Option(
        'tgcf.config.yml',
        help='Path of configuration file'),
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

    tgcf offers two modes of operation.

    The "past" mode is for forwarding all existing messages. (performs the job and quits).

    On the other hand the "live" mode will forward all new upcoming messages, as long as tgcf runs in the server.

    You can specify the source and destination chats in the "tgcf.config.yml" file in the format specified in the documentation.

    tgcf also supports filtering by whitelist/blacklist/mime-type/message author, text replacement, and many more features.
    '''

    if not FAKE:
        print('Real working...')
    else:
        # when the env var FAKE_TELEWATER is truthy, then no real work is done
        # this is for CLI testing purposes
        print(f'name is {name} and token is {token}')
        print(f'{API_ID} and {API_HASH}')
        print(f'mode = {mode}')
        print(f'config file path = {config_file}')

# AAHNIK 2021
