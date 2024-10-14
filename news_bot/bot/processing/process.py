
from aiogram import Router


from aiogram import Bot, types

import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode 

from aiogram.types import ContentType
from aiogram import F

API_TOKEN=os.getenv('TOKEN')
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

processs_router = Router()

@processs_router.message(F.content_type == ContentType.PHOTO)
async def remove_background_handler(message: types.Message) -> None:
    file_id = message.photo[-1].file_id
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    await message.answer(f"{file_info.file_path}")