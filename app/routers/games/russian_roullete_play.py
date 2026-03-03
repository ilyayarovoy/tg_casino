import random

from aiogram import Router
from aiogram.types import CallbackQuery

from app.service.user_service import UserService
from app.keyboards.games_list import menu_games
from app.keyboards.games.russian_roulette_keyboard import russian_roulette



router = Router()


def russian_roulette_spin():
    return random.randint(1, 6)  # 1 из 6 — пуля

# Игра Кости
@router.callback_query(lambda query: query.data == 'main_game:roullete')
async def game_russian_roulette(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    balance = await UserService.get_balance(telegram_id)

    await callback.answer()
    await callback.message.edit_text(
        "🔫 Русская рулетка\n\n"
        "1 патрон в барабане из 6\n"
        "Выигрыш x2\n\n"
        f"Баланс: {balance}",
        reply_markup=russian_roulette()
    )

@router.callback_query(lambda query: query.data == 'russian_roulette:shoot')
async def russian_roulette_shoot(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    balance = await UserService.get_balance(telegram_id)

    spin = russian_roulette_spin()

    if spin == 1:  # пуля
        await UserService.reduce_balance_by_2(
            telegram_id=telegram_id,
            balance=balance
        )
        new_balance = await UserService.get_balance(telegram_id)

        await callback.message.edit_text(
            "💥 БАХ!\n\n"
            "Ты проиграл...\n"
            f"Баланс: {new_balance}",
            reply_markup=russian_roulette()
        )
    else:
        await UserService.increase_balance_by_2(
            telegram_id=telegram_id,
            balance=balance
        )
        new_balance = await UserService.get_balance(telegram_id)

        await callback.message.edit_text(
            "😮 Повезло!\n\n"
            "Патрон не выстрелил!\n"
            f"Баланс: {new_balance}",
            reply_markup=russian_roulette()
        )


# Вернуть в главное меню
@router.callback_query(lambda query: query.data == 'russian_roulette:back')
async def games_fifty_fifty_back_to_menu(callback: CallbackQuery):
    await callback.message.edit_text("Меню", reply_markup=menu_games())
