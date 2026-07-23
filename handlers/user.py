from aiogram import Router, F
from aiogram.types import Message

from database.db import get_movie
from aiogram.filters import StateFilter

router = Router()


@router.message(F.text)
async def send_movie(message: Message):

    movie = get_movie(message.text)

    if movie:
        await message.answer_video(
            video=movie[0],
            caption="🎬 Ёқимли томоша!"
        )
    else:
        await message.answer("❌ Бу код бўйича кино топилмади.")


@router.message(StateFilter(None), F.text)
async def send_movie(message: Message):
    ...