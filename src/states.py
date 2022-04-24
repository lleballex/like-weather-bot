from aiogram.dispatcher.filters.state import StatesGroup, State


class CityChanging(StatesGroup):
    title_wait = State()

# class CityAdding(StatesGroup):
#     title_wait = State()


# class CitiesView(StatesGroup):
#     action_wait = State()