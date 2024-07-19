# celery.py
import os
from celery import Celery
from django.conf import settings
from fetcher.parse import get_news_channels  # Import the task from parse.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_bot.settings')

app = Celery('news_bot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.config_from_object(settings)

app.conf.update({
    'beat_schedule': {
        "get-news-channels": {
            "task": get_news_channels,  # Use the imported task
            "schedule": "*/2 * * * *",  # Run every 2 minutes
        },
    }
})