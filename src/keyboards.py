from misc import COMMANDS

from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
                 InlineKeyboardButton(f'Скорость ({speed})', callback_data='update:speed'),
                 InlineKeyboardButton(f'Давление ({pressure})', callback_data='update:pressure'),
                 InlineKeyboardButton(f'Расстояние ({distance})', callback_data='update:distance'))
    return keyboard


def get_setting_kb(callback_key, values):
    keyboard = InlineKeyboardMarkup()
    for key, value in values:
        keyboard.insert(InlineKeyboardButton(value, callback_data=f'{callback_key}:{key}'))
    keyboard.add(InlineKeyboardButton(COMMANDS['back'], callback_data=f'settings:back'))
    return keyboard
