import asyncio
from settings import API_ID, API_HASH
from telethon import TelegramClient
from forwarder import _


async def get_chat_id(ref=None):
    async with TelegramClient('forwarder', API_ID, API_HASH) as client:
        if not ref:
            ref = input('Enter link/phone/username/id to get chat info: ')
        try:
            entity = await client.get_entity(_(ref))
            print(type(entity))
            print(f'id is {entity.id}')
            print(f'\nEntity object \n{entity.stringify()}')
        except ValueError:
            print('Could not get')
        except Exception as err:
            print(f'''Something went wrong. Please contact the developer Aahnik Daw.
                    Chat with Aahnik on Telegram, click on this 👇 link
                    
                    https://telegram.me/AahnikDaw 
                    
                    Error details: \n {err}''')

if __name__ == "__main__":
    asyncio.run(get_chat_id())
