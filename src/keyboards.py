from misc import COMMANDS
from utils import get_date, localtime

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from datetime import timedelta


main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.row(COMMANDS['weather'])
main_kb.row(COMMANDS['change_city'], COMMANDS['settings'])


def get_change_city_kb(cities):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for city in cities:
        keyboard.insert(city.title)
    keyboard.add(COMMANDS['back'])
    return keyboard


def get_settings_kb(degrees, speed, pressure, distance):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(f'Температура ({degrees})', callback_data='update:degrees'),
                 InlineKeyboardButton(f'Скорость ({speed})', callback_data='update:speed'))
    keyboard.add(InlineKeyboardButton(f'Давление ({pressure})', callback_data='update:pressure'),
                 InlineKeyboardButton(f'Расстояние ({distance})', callback_data='update:distance'))
    return keyboard


def get_setting_kb(callback_key, values):
    keyboard = InlineKeyboardMarkup()
    for key, value in values:
        keyboard.insert(InlineKeyboardButton(value, callback_data=f'{callback_key}:{key}'))
    keyboard.add(InlineKeyboardButton(COMMANDS['back'], callback_data=f'settings:back'))
    return keyboard


def get_weather_kb(day_change=0):
    keyboard = InlineKeyboardMarkup()

    if day_change != 0:
        keyboard.add(InlineKeyboardButton(f'◀️ {get_date(day_change - 1)}',
                                          callback_data=f'weather:{day_change - 1}'))
    if day_change != 5:
        keyboard.insert(InlineKeyboardButton(f'{get_date(day_change + 1)} ▶️',
                                             callback_data=f'weather:{day_change + 1}'))

    return keyboard