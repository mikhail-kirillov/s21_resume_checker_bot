import asyncio
import json
import logging
from just_messages import messages_router
from handlers import handlers_router
from aiogram import Bot, Dispatcher


with open("config.json") as json_file:
    telegram_token = (json.load(json_file))["auth"]["telegram"]["token"]


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=telegram_token)
    dp = Dispatcher()
    dp.include_routers(messages_router)
    dp.include_router(handlers_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
