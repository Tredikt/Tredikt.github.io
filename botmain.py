from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, WebAppData

from class_bot import MyBot
from utils.db_api.database import DataBase
from config import TOKEN, db_name


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
db = DataBase(db_name)

my_bot = MyBot(bot=bot, dp=dp, db=db)
my_bot.run()