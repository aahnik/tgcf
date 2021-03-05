import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION_STRING = os.getenv('TG_SESSION_STRING')
BOT_TOKEN = os.getenv('BOT_TOKEN')


# during clean up last these many messages will be kept

