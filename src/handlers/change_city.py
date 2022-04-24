from misc import dp
from .main import menu
from .weather import weather
from models import User, City
from states import CityChanging
from misc import COMMANDS as CMDS
from keyboards import main_kb, get_change_city_kb


@dp.message_handler(commands='change_city', state='*')
@dp.message_handler(lambda msg: msg.text == CMDS['change_city'])
async def change_city(message):
    user, _ = User.get_or_create(user_id=message.from_user.id)
    await CityChanging.title_wait.set()
    await message.answer('Какой город тебя интересует?',
                         reply_markup=get_change_city_kb(user.cities[::-1]))


@dp.message_handler(lambda msg: msg.text == CMDS['back'], state=CityChanging.title_wait)
async def to_menu(message, state):
    await menu(message, state)


@dp.message_handler(state=CityChanging.title_wait)
async def change_city_process(message, state):
    city = City.find(message.text)

    if city:
        User.get(user_id=message.from_user.id).activate_city(city)
        await message.answer('Ради тебя я сбегал туда и измерил температуру',
                             reply_markup=main_kb)
        await weather(message, state)
    else:
        await message.answer('Хм... Не могу найти твой город, попробуй что-нибудь другое')