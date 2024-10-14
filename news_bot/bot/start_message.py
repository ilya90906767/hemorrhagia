from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile


start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет, это стартовое сообщение. Отправь мне фотографию своего товара")

    