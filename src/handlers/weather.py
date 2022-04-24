from misc import dp
from models import User
from .main import add_city
from misc import COMMANDS as CMDS


@dp.message_handler(commands='weather', state='*')
@dp.message_handler(lambda msg: msg.text == CMDS['weather'])
async def weather(message, state):
    await state.finish()

    user, _ = User.get_or_create(user_id=message.from_user.id)
    weather = user.get_weather()

    if weather:
        await message.answer(weather)
    else:
        await add_city(message)