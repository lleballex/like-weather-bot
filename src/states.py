from aiogram.dispatcher.filters.state import StatesGroup, State


class CityChanging(StatesGroup):
    title_wait = State()