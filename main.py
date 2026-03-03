import asyncio
from aiogram import Bot, Dispatcher

from app.routers import start, profile
from app.routers.games import fifty_fifty_play, dice_play, russian_roullete_play

import os

TOKEN = os.getenv("BOT_TOKEN")


async def main():

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(profile.router)

    # Игры: 50/50, кости, рулетка
    dp.include_router(fifty_fifty_play.router)
    dp.include_router(dice_play.router)
    dp.include_router(russian_roullete_play.router)



    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())