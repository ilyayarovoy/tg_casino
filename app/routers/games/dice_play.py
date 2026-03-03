import random

from aiogram import Router
from aiogram.types import CallbackQuery

from app.service.user_service import UserService
from app.keyboards.menu_keyboard import main_menu_keyboard
from app.keyboards.games.dice_keyboard import dice_game



router = Router()


def get_generate_dice_number():
    number = random.randint(1, 12)
    return number

# Игра Кости
@router.callback_query(lambda query: query.data == 'main_game:Dice')
async def games_ice(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    balance = await UserService.get_balance(telegram_id)
    await callback.answer()
    await callback.message.edit_text("Играем в кости\n"
                                     f"Баланс: {balance}", reply_markup=dice_game())

# Кинуть кости
@router.callback_query(lambda query: query.data == 'dice_game:roll_dice')
async def games_roll_dice_(callback: CallbackQuery):

    telegram_id = callback.from_user.id
    balance = await UserService.get_balance(telegram_id)

    bot_roll_dice = get_generate_dice_number()
    user_roll_dice = get_generate_dice_number()

    if user_roll_dice > bot_roll_dice:
        await UserService.increase_balance_by_2(telegram_id=telegram_id, balance=balance)
        new_balance = await UserService.get_balance(telegram_id=telegram_id)
        await callback.message.edit_text(f"Выпало у вас: {user_roll_dice}\n"
                                         f"Выпало у бота: {bot_roll_dice}\n\n"
                                         f"✅ Удача! Баланс: {new_balance}", reply_markup=dice_game())
    elif user_roll_dice < bot_roll_dice:
        await UserService.reduce_balance_by_2(telegram_id=telegram_id, balance=balance)
        new_balance = await UserService.get_balance(telegram_id=telegram_id)
        await callback.message.edit_text(f"Выпало у вас: {user_roll_dice}\n"
                                         f"Выпало у бота:{bot_roll_dice}\n\n"
                                         f"❌ Не удача! Баланс: {new_balance}", reply_markup=dice_game())
    else:
        await callback.message.edit_text(f"Выпало у вас: {user_roll_dice}\n"
                                         f"Выпало у бота:{bot_roll_dice}\n\n"
                                         f"О как 🫢 Баланс: {balance}", reply_markup=dice_game())
# Вернуть в главное меню
@router.callback_query(lambda query: query.data == 'main_game:back_to_menu')
async def games_fifty_fifty_back_to_menu(callback: CallbackQuery):
    await callback.message.edit_text("Меню", reply_markup=main_menu_keyboard())
