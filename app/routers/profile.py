from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from app.states.deposit_state import DepositState
from app.states.withdraw_state import WithdrawState

from app.service.user_service import UserService
from app.keyboards.profile import profile_keyboard
from app.keyboards.menu_keyboard import main_menu_keyboard
from app.keyboards.games_list import menu_games


router = Router()

# Кнопка профиль
@router.callback_query(lambda query: query.data == 'main_menu:profile')
async def menu_profile(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    firstname = callback.from_user.first_name
    balance = await UserService.get_balance(telegram_id)
    await callback.answer()
    await callback.message.edit_text(f"""
    Имя: {firstname}\nБаланс: {balance} p.\n
""", reply_markup=profile_keyboard())

# Кнопка игры
@router.callback_query(lambda query: query.data == 'main_menu:game')
async def menu_profile_game(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(f"Игры\n", reply_markup=menu_games())

# Кнопка пополнить баланс
@router.callback_query(lambda query: query.data == 'profile:deposit')
async def menu_profile_deposit(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите сумму для пополнения")
    await state.set_state(DepositState.amount)
    await callback.answer()
# Обработка состояния для депозита
@router.message(DepositState.amount)
async def get_amount_for_dep(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    telegram_id = message.from_user.id
    data = await state.get_data()
    if not data["amount"].isdigit():
        await message.answer("Введите сумму цирами (100, 500, 1000)")
        return

    result = await UserService.deposit(telegram_id=telegram_id, amount=int(data["amount"]))
    balance = await UserService.get_balance(telegram_id=telegram_id)
    await message.answer(f"Баланс пополнен\nВаш баланс: {balance} p.", reply_markup=profile_keyboard())
    await state.clear()

# # Кнопка вывода
@router.callback_query(lambda query: query.data == 'profile:withdraw')
async def menu_profile_deposit(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите сумму для вывода")
    await state.set_state(WithdrawState.amount)
    await callback.answer()
# Обработка состояния для вывода
@router.message(WithdrawState.amount)
async def get_amount_for_withdraw(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    telegram_id = message.from_user.id
    data = await state.get_data()
    if not data["amount"].isdigit():
        await message.answer("Введите сумму цирами (100, 500, 1000)")
        return
    await state.clear()
    try:
        result = await UserService.withdraw(telegram_id=telegram_id, amount=int(data["amount"]))
        balance = await UserService.get_balance(telegram_id=telegram_id)
        await message.answer(f"Деньги выведены\nВаш баланс: {balance} p.", reply_markup=profile_keyboard())
    except ValueError as error:
        await message.answer(f"Ошибка: {error}", reply_markup=main_menu_keyboard())
        return

# Кнопка назад рофиле
@router.callback_query(lambda query: query.data == 'profile:back')
async def menu_profile_back(callback: CallbackQuery):
    await callback.answer()

    await callback.message.edit_text(
        f'Привет {callback.from_user.first_name}',
        reply_markup=main_menu_keyboard()
    )