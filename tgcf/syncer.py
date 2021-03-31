from telethon import client


# client = get_client()

def syncer():
    client.start()
    client.run_until_disconnected()
