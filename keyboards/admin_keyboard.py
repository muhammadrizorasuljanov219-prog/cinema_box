from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Кино қўшиш")],
            [KeyboardButton(text="🗑 Кино ўчириш")],
            [KeyboardButton(text="📊 Статистика")],
            [KeyboardButton(text="📢 Реклама")],
            [KeyboardButton(text="❌ Бекор қилиш")]
        ],
        resize_keyboard=True
    )