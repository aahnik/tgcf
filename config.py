from configparser import ConfigParser

configur = ConfigParser()
configur.read('config.ini')

api_id = configur.getint('user', 'api_id')
api_hash = configur.get('user', 'api_hash')

from_chat = configur.get('forward', 'from')
to_chat = configur.get('forward', 'to')
offset = configur.getint('forward', 'offset')


def update_offset(new_offset):
    configur.set('forward', 'offset', str(new_offset))
    with open('config.ini', 'w') as cfg:
        configur.write(cfg)


if __name__ == "__main__":
    # testing
    print(api_hash, api_id, from_chat, to_chat, offset)
    print(bool(offset))
    update_offset('1000')
    
