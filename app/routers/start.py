from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.keyboards.menu_keyboard import main_menu_keyboard
from app.service import user_service



router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    telegram_id = message.from_user.id
    firstname = message.from_user.first_name
    lastname = message.from_user.last_name
    balance = 1000
    await user_service.UserService.register_new_user(
        telegram_id=telegram_id,
        firstname=firstname,
        lastname=lastname,
        balance=balance
    )
    await message.answer(f'Привет {message.from_user.first_name}', reply_markup=main_menu_keyboard())