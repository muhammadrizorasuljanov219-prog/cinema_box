from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.movie_state import AddMovie, DeleteMovie
from database.db import add_movie as save_movie
from database.db import get_movie, delete_movie

router = Router()

# =======================
# KINO QO'SHISH
# =======================

@router.message(F.text == "➕ Кино қўшиш")
async def add_movie_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("🎬 Кино кодини киритинг:")
    await state.set_state(AddMovie.code)


@router.message(AddMovie.code)
async def get_code(message: Message, state: FSMContext):
    await state.update_data(code=message.text)
    await message.answer("🎬 Кино номини киритинг:")
    await state.set_state(AddMovie.name)


@router.message(AddMovie.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("🎭 Жанрини киритинг:")
    await state.set_state(AddMovie.genre)


@router.message(AddMovie.genre)
async def get_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await message.answer("📅 Чиққан йилини киритинг:")
    await state.set_state(AddMovie.year)


@router.message(AddMovie.year)
async def get_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await message.answer("⭐ IMDb рейтингини киритинг:")
    await state.set_state(AddMovie.imdb)


@router.message(AddMovie.imdb)
async def get_imdb(message: Message, state: FSMContext):
    await state.update_data(imdb=message.text)
    await message.answer("📹 Энди кино видеосини юборинг:")
    await state.set_state(AddMovie.video)


@router.message(AddMovie.video, F.video)
async def get_video(message: Message, state: FSMContext):
    data = await state.get_data()

    save_movie(
        data["code"],
        data["name"],
        data["genre"],
        data["year"],
        data["imdb"],
        message.video.file_id
    )

    await message.answer("✅ Кино муваффақиятли сақланди!")
    await state.clear()


# =======================
# KINO O'CHIRISH
# =======================

@router.message(F.text == "🗑 Кино ўчириш")
async def delete_movie_start(message: Message, state: FSMContext):
    await message.answer("🗑 Ўчириладиган кино кодини киритинг:")
    await state.set_state(DeleteMovie.code)


@router.message(DeleteMovie.code)
async def delete_movie_finish(message: Message, state: FSMContext):
    movie = get_movie(message.text)

    if movie is None:
        await message.answer("❌ Бу код бўйича кино топилмади.")
        return

    delete_movie(message.text)

    await message.answer("✅ Кино муваффақиятли ўчирилди.")
    await state.clear()