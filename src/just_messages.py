from aiogram import Router, types, F
from aiogram.filters import Command

messages_router = Router()

HELLO_MESSAGE = ("Привет! \nЭто бот, который поможет тебе с резюме. \nПроанализировав его, он даст тебе советы по "
                 "улучшению. \nПросто отправь файл (*.pdf)")

MESSAGE_404 = "Что-то непонятное :("


@messages_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(HELLO_MESSAGE)


@messages_router.message(F.text)
async def cmd_start(message: types.Message):
    await message.answer(MESSAGE_404)
