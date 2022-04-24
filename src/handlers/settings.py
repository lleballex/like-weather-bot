from misc import dp
from models import User
from misc import COMMANDS as CMDS
from models import DEGREES, SPEED, PRESSURE, DISTANCE
from keyboards import get_settings_kb, get_setting_kb


FIELDS = {
    'degrees': DEGREES,
    'speed': SPEED,
    'pressure': PRESSURE,
    'distance': DISTANCE
}


async def send_settings(message, user, edit_message=False):
    kwargs = {
        'text': 'Что будем менять?',
        'reply_markup': get_settings_kb(degrees=user.get_degrees_label(),
                                        speed=user.get_speed_label(),
                                        pressure=user.get_pressure_label(),
                                        distance=user.get_distance_label())
    }

    if edit_message:
        await message.edit_text(**kwargs)
    else:
        await message.answer(**kwargs)


@dp.message_handler(commands='settings', state='*')
@dp.message_handler(lambda msg: msg.text == CMDS['settings'])
async def settings(message, state, edit_message=False):
    user, _ = User.get_or_create(user_id=message.from_user.id)
    await state.finish()
    await send_settings(message, user)


@dp.callback_query_handler(lambda q: q.data.startswith('update:') and q.data.count(':') == 1)
async def update_field(query):
    await query.answer()
    field = query.data.split(':')[1]
    keyboard = get_setting_kb(query.data, FIELDS[field])
    await query.message.edit_text('Выбирай', reply_markup=keyboard)


@dp.callback_query_handler(lambda q: q.data.startswith('update:') and q.data.count(':') == 2)
async def update_field_process(query, state):
    await query.answer()

    user = User.get(user_id=query.from_user.id)
    _, field, value = query.data.split(':')
    setattr(user, field, value)
    user.save()

    await to_settings(query, state)


@dp.callback_query_handler(lambda query: query.data == 'settings:back')
async def to_settings(query, state):
    user = User.get(user_id=query.from_user.id)
    await send_settings(query.message, user, edit_message=True)