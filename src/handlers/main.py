from misc import dp
from models import User
from keyboards import main_kb
from states import CityChanging


async def add_city(message):
    await CityChanging.title_wait.set()
    await message.answer('Привет! Напише мне название города')


@dp.message_handler(commands='start', state='*')
async def start(message, state):
    await state.finish()
    user, is_created = User.get_or_create(user_id=message.from_user.id)

    if is_created:
        await add_city(message)
    else:
        await message.answer('Мы уже здоровались', reply_markup=main_kb)


@dp.message_handler(commands='menu', state='*')
async def menu(message, state):
    await state.finish()
    await message.answer('Что будете заказывать?', reply_markup=main_kb)


@dp.message_handler(commands='help', state='*')
async def help(message, state):
    await state.finish()
    await message.answer('Привет! Я умею узнавать погоду в любой точке мира, хочешь проверить?\n\n'
                         'Если у тебя пропала клавиатура, /menu тебе поможет. '
                         'Или можешь воспользоваться одной из этих команд:\n\n'
                         '/start - Запуск бота\n'
                         '/menu - Меню\n'
                         '/help - Помощь\n'
                         '/weather - Узнать погоду\n'
                         '/change_city - Сменить город\n'
                         '/settings - Настройки\n')