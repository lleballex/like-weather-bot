from misc import dp
from models import User
from .main import add_city
from misc import COMMANDS as CMDS
from keyboards import get_weather_kb

from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(commands='weather', state='*')
@dp.message_handler(lambda msg: msg.text == CMDS['weather'])
async def weather(message, state):
    await state.finish()

    user, _ = User.get_or_create(user_id=message.from_user.id)
    weather = user.get_weather()

    if weather:
        await message.answer(weather, reply_markup=get_weather_kb())
    else:
        await add_city(message)


@dp.callback_query_handler(lambda query: query.data.startswith('weather:'))
async def change_day(query):
    await query.answer()

    day_change = int(query.data.replace('weather:', ''))
    user = User.get(user_id=query.from_user.id)
    weather = user.get_weather(day_change)

    if weather:
        try:
            await query.message.edit_text(weather, reply_markup=get_weather_kb(day_change))
        except MessageNotModified:
            pass
    else:
        await add_city(message)