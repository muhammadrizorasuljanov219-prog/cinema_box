from aiogram.fsm.state import State, StatesGroup

class AddMovie(StatesGroup):
    code = State()
    name = State()
    genre = State()
    year = State()
    imdb = State()
    video = State()


class DeleteMovie(StatesGroup):
    code = State()


class Broadcast(StatesGroup):
    text = State()