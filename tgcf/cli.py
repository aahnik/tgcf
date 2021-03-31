''' This module implements the command line interface for tgcf,
using the modern and robust `typer`.
'''


from tgcf import __version__
from typing import Optional
import logging

import typer
from dotenv import load_dotenv

import os
load_dotenv('.env')

FAKE = bool(os.getenv('FAKE_TGCF'))
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


@app.command()
def main(
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

    config: str = typer.Option(
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
    ''' tgcf is a powerful tool for forwarding telegram messages or live syncing. Make sure you have API_ID and API_HASH in your .env file inside the current directory.
    '''

    if not FAKE:
        print('Real working')
    else:
        # when the env var FAKE_TELEWATER is truthy, then no real work is done
        # this is for CLI testing purposes
        print(f'name is {name} and token is {token}')

# AAHNIK 2021
