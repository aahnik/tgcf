import logging
from settings import API_ID, API_HASH
from telethon import TelegramClient, client, events
from forwarder import _
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

SENT_VIA = f'\n__Sent via__ `{str(__file__)}`'

client = TelegramClient('forwarder', API_ID, API_HASH)


@client.on(events.NewMessage(outgoing=True, pattern=r'\.id'))
async def chat_id_handler(event):
    chat_id = event.chat_id
    await event.edit(str(chat_id))


@client.on(events.NewMessage(outgoing=True, pattern=r'\.info'))
async def chat_info_handler(event):
    chat_info = await event.get_chat()
    await event.edit(str(chat_info))


async def main():
    await client.send_message('me', f'''Hi! 
        \n**Telegram Chat Forward** is made by @AahnikDaw.
        \nPlease star 🌟 on [GitHub](https://github.com/aahnik/telegram-chat-forward).
        \nYou can send `.id` to any chat/group/channel to get its chat id.
        \nTo get full info, send `.info`.
        \nYou may first try it here 😃 
        {SENT_VIA}''', link_preview=False)

if __name__ == "__main__":
    client.start()
    client.loop.run_until_complete(main())
    print('''If this script is succesfully running, 
    you will see a new message in your Saved Messages. 
    Open your Telegram App and send .id to any chat, to get the chat id.
    To get all info send .info
    \nPress Ctrl + C to stop the process.''')
    client.run_until_disconnected()
