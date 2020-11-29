from configparser import ConfigParser
from dotenv import load_dotenv
import os
import logging

load_dotenv()

API_ID = os.getenv('api_id')
API_HASH = os.getenv('api_hash')

assert API_ID and API_HASH

configur = ConfigParser()
configur.read('config.ini')

forwards = configur.sections()




def get_forward(forward: str) -> tuple:
    try:
        from_chat = configur.get(forward, 'from')
        to_chat = configur.get(forward, 'to')
        offset = configur.getint(forward, 'offset')
        return from_chat, to_chat, offset
    except Exception as err:
        logging.exception(
            'The content of %s does not follow format. See the README.md file for more details. \n\n %s', forward, str(err))
        quit()


def update_offset(forward: str, new_offset: str) -> None:
    try:
        configur.set(forward, 'offset', new_offset)
        with open('config.ini', 'w') as cfg:
            configur.write(cfg)
    except Exception as err:
        logging.exception(
            'Problem occured while updating offset of %s \n\n %s', forward, str(err))


if __name__ == "__main__":
    # testing
    for forward in forwards:
        print(forward, get_forward(forward))
