import os 
from dotenv import load_dotenv

from telethon import TelegramClient, sync

load_dotenv()
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
client = TelegramClient('session_name', api_id, api_hash)

async def get_news_chanells():
    me = client.get_me()

while True: 
    print('a')