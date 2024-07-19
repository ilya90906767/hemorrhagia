from celery import shared_task
from django.conf import settings

from .models import TelegramChanell, LastMessages
from .fetcher_main import client  # Import the client variable from fetcher_main.py

@shared_task
def get_news_channels():
    channels = TelegramChanell.objects.all()
    last_messages = {}
    for channel in channels:
        entity = client.get_entity(channel.telegram_id)
        message = client.get_messages(entity, limit=1)[0]
        last_messages[channel.id] = {
            'text': message.text,
            'source': channel.name,
            'datetime': message.date.isoformat()
        }
    
    for channel_id, message_data in last_messages.items():
        LastMessages.objects.update_or_create(
            channel_id=channel_id,
            defaults={
                'text': message_data['text'],
                'datetime': message_data['datetime']
            }
        )