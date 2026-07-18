import asyncio
import database.db


from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers.start import router as start_router
from handlers.admin import router as admin_router
from handlers.movie import router as movie_router
from handlers.user import router as user_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(admin_router)
dp.include_router(movie_router)
dp.include_router(user_router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())