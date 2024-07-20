from .models import TelegramChanell, LastMessages

def get_news_channels(client):
    channels = TelegramChanell.objects.all()
    last_messages = {}
    for channel in channels:
        entity = client.get_entity(channel.id)
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
                'date': message_data['datetime']
            }
        )