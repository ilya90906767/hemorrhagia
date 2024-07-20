from django.contrib import admin

from .models import TelegramChanell, LastMessages, FinalMessages

admin.site.register(TelegramChanell)
admin.site.register(LastMessages)
admin.site.register(FinalMessages)

# Register your models here
