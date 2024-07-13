import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode 

load_dotenv()   
API_TOKEN=os.getenv('TOKEN')


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # Register all the routers from handlers package

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)
