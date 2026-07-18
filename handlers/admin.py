from aiogram import Router , F
from aiogram.filters import Command
from aiogram.types import Message
from database.db import users_count, movies_count
from aiogram.fsm.context import FSMContext
from states.movie_state import Broadcast
from database.db import get_all_users
from aiogram import Bot
from aiogram.fsm.context import FSMContext

from config import ADMIN_ID
from keyboards.admin_keyboard import admin_menu

router = Router()


@router.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Сиз админ эмассиз!")
        return

    await message.answer(
        "🔐 Cinema Box админ панели",
        reply_markup=admin_menu()
    )
@router.message(F.text == "📊 Статистика")
async def statistics(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        f"""📊 Cinema Box статистикаси

👤 Фойдаланувчилар: {users_count()}
🎬 Кинолар: {movies_count()}
"""
    )

@router.message(F.text == "📢 Реклама")
async def broadcast_start(message: Message, state: FSMContext):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer("📢 Юбориладиган хабарни ёзинг:")

    await state.set_state(Broadcast.text)
@router.message(Broadcast.text)
async def broadcast_send(message: Message, state: FSMContext, bot: Bot):

    users = get_all_users()

    success = 0

    for user in users:
        try:
            await bot.send_message(user[0], message.text)
            success += 1
        except:
            pass

    await message.answer(
        f"✅ Реклама {success} та фойдаланувчига юборилди."
    )

    await state.clear()


@router.message(F.text == "❌ Бекор қилиш")
async def cancel(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        "✅ Амал бекор қилинди.",
        reply_markup=admin_menu()
    )