from aiogram import Router, F, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from just_messages import MESSAGE_404
from parser import read_pdf_file
from gigachat_api import resume_check

handlers_router = Router()
USERS_RESUMES = dict()
JOB_TITLES = ["Python-Разработчик", "Go-Разработчик", "Kotlin-Разработчик", "Java-Разработчик", "Frontend-Разработчик",
              "Swift-Разработчик", "C#-Разработчик", "Backend-Разработчик", "Разработчик игр", "ML", "DS", "DevOps",
              "ROS", "Архитектор ПО", "Бизнес-аналитик", "Тестировщик"]
GET_DOCUMENT_TEXT = "Пожалуйста, выбери специальность"
BIG_FILE = "Прости, но файл слишком большой"


class ResumeCbDt(CallbackData, prefix="job_titles"):
    job_title: str


@handlers_router.message(F.document)
async def get_file(message: Message):
    if ".pdf" in message.document.file_name:
        try:
            await message.bot.download(file=message.document.file_id,
                                       destination=message.document.file_id + message.document.file_name)
            USERS_RESUMES[message.from_user.id] = message.document.file_id + message.document.file_name
            rows_num = 8
            inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=JOB_TITLES[i],
                                                                                          callback_data=ResumeCbDt(
                                                                                              job_title=JOB_TITLES[
                                                                                                  i]).pack()) for i in
                                                                     range((len(JOB_TITLES) // rows_num) * j,
                                                                           (len(JOB_TITLES) // rows_num) * (j + 1))] for
                                                                    j in range(rows_num)])
            await message.answer(text=GET_DOCUMENT_TEXT, reply_markup=inline_keyboard)
        except TelegramBadRequest:
            await message.answer(text=BIG_FILE)
    else:
        await message.answer(MESSAGE_404)


@handlers_router.callback_query(ResumeCbDt.filter())
async def callback_job_title(callback: types.CallbackQuery, callback_data: ResumeCbDt):
    await callback.message.bot.edit_message_reply_markup(chat_id=callback.from_user.id,
                                                         message_id=callback.message.message_id, reply_markup=None)
    if callback_data.job_title in JOB_TITLES:
        resume_text = read_pdf_file(USERS_RESUMES[callback.message.chat.id])
        result = resume_check(callback_data.job_title, resume_text)
        await callback.message.answer(text=result)
    else:
        await callback.message.answer(MESSAGE_404)
