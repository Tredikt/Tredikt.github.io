from aiogram import Bot
from utils.db_api.database import DataBase
from config import TOKEN, db_name


def get_bot_and_db():
    bot = Bot(TOKEN)
    db = DataBase(db_name)
    return bot, db