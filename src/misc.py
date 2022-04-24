from pyowm import OWM
from peewee import SqliteDatabase
from aiogram import Bot, Dispatcher
from pyowm.utils.config import get_default_config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from os import getenv


bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

db = SqliteDatabase('db.sqlite3')

owm_config = get_default_config()
owm_config['language'] = 'ru'
owm = OWM(getenv('OWM_TOKEN'), owm_config).weather_manager()


COMMANDS = {
    'weather': '🌦 Погода',
    'change_city': '🏙 Сменить город',
    'back': '⬅️ Назад',
    'settings': '⚙️ Настройки',
}
