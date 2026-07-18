from aiogram import Router, types
from aiogram.filters import CommandStart

from database.db import add_user

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    add_user(message.from_user.id)

    await message.answer(
        "🎬 Cinema Box ботга хуш келибсиз!\n\n"
        "Кино кодини юборинг."
    )