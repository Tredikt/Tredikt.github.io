from aiogram.types import CallbackQuery
from aiogram.dispatcher.dispatcher import FSMContext

from utils.functions.get_bot_and_db import get_bot_and_db


async def callback_handler(call: CallbackQuery, state: FSMContext):
    bot, db = get_bot_and_db()
    tg_id = call["from"]["id"]
    callback = call.data
    m_id = call.message.message_id