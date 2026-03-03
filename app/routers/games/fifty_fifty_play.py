import random

from aiogram import Router
from aiogram.types import CallbackQuery

from app.service.user_service import UserService
from app.keyboards.games.fifty_fifty_keyboard import fifty_fifty_game
from app.keyboards.games_list import menu_games
from app.keyboards.menu_keyboard import main_menu_keyboard



router = Router()


def get_guess_number():
    number = random.randint(1, 2)
    return number

# Игра 50/50
@router.callback_query(lambda query: query.data == 'main_game:50/50')
async def games_fifty_fifty(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    balance = await UserService.get_balance(telegram_id)
    await callback.answer()
    await callback.message.edit_text(f"""
    Программа загадала число (1 или 2)!\nПопробуй угадать!\n
Баланс: {balance}
""", reply_markup=fifty_fifty_game())

# Вернуть в главное меню
@router.callback_query(lambda query: query.data == 'main_game:back_to_menu')
async def games_fifty_fifty_back_to_menu(callback: CallbackQuery):
    await callback.message.edit_text("Меню", reply_markup=main_menu_keyboard())

# Обработка 1 или 2
@router.callback_query(lambda query: query.data == 'fifty_fifty_game:1')
async def fifty_fifty_one(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    balance = await UserService.get_balance(telegram_id)
    guess_number = get_guess_number()

    if guess_number == 1:
        await UserService.increase_balance_by_2(telegram_id=telegram_id, balance=balance)
        new_balance = await UserService.get_balance(telegram_id=telegram_id)
        await callback.message.edit_text(f"✅Удача!\b Баланс: {new_balance}\n"
                                      f"Выбери (1 или 2)", reply_markup=fifty_fifty_game())
        await callback.answer()
    else:
        await UserService.reduce_balance_by_2(telegram_id=telegram_id, balance=balance)
        new_balance = await UserService.get_balance(telegram_id=telegram_id)
        await callback.message.edit_text(f"❌ Не удача!\b Баланс: {new_balance}\n"
                                         f"Выбери (1 или 2)", reply_markup=fifty_fifty_game())
        await callback.answer()

@router.callback_query(lambda query: query.data == 'fifty_fifty_game:2')
async def fifty_fifty_two(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    balance = await UserService.get_balance(telegram_id)
    guess_number = get_guess_number()

    if guess_number == 2:
        await UserService.increase_balance_by_2(telegram_id=telegram_id, balance=balance)
        new_balance = await UserService.get_balance(telegram_id=telegram_id)
        await callback.message.edit_text(f"✅Удача!\b Баланс: {new_balance}\n"
                                         f"Выбери (1 или 2)", reply_markup=fifty_fifty_game())
        await callback.answer()
    else:
        await UserService.reduce_balance_by_2(telegram_id=telegram_id, balance=balance)
        new_balance = await UserService.get_balance(telegram_id=telegram_id)
        await callback.message.edit_text(f"❌ Не удача!\b Баланс: {new_balance}\n"
                                         f"Выбери (1 или 2)", reply_markup=fifty_fifty_game())
        await callback.answer()
# Кнопка назад

@router.callback_query(lambda query: query.data == 'fifty_fifty_game:back')
async def fifty_fifty_back(callback: CallbackQuery):
    await callback.message.edit_text(f"Игры", reply_markup=menu_games())
    await callback.answer()