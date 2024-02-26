from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from utils.db_api.database import DataBase

from aiogram.types import Message
from aiogram.dispatcher.dispatcher import FSMContext

from blanks.bot_markup import menu

from handlers.callback_handler import callback_handler


class MyBot:
    def __init__(self, bot: Bot, dp: Dispatcher, db: DataBase):
        self.bot = bot
        self.dp = dp
        self.db = db

    async def start_handler(self, message: Message, state: FSMContext):
        chat = message.chat.id
        tg_id = message.from_user.id
        username = message.from_user.username

        markup = ReplyKeyboardMarkup()
        markup.add(KeyboardButton("Открыть магазин", web_app=WebAppInfo(url="https://tredikt.github.io/")))

        await self.bot.send_message(
            chat_id=chat,
            text="Привет!",
            reply_markup=markup
        )

    async def text_handler(self, message: Message, state: FSMContext):
        tg_id = message.from_user.id
        m_id = message.message_id
        chat_type = message.chat.type

    def register_handlers(self):
        self.dp.register_callback_query_handler(callback=callback_handler, state="*")

        self.dp.register_message_handler(callback=self.start_handler, commands=["start"], state="*")
        self.dp.register_message_handler(callback=self.text_handler, state="*", content_types=["text"])

    def run(self):
        self.register_handlers()
        executor.start_polling(dispatcher=self.dp, skip_updates=True)