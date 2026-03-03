from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def profile_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Пополнить баланс",
                callback_data="profile:deposit",
                style="default"
            )
        ],
        [
            InlineKeyboardButton(
                text="Вывод",
                callback_data="profile:withdraw",
                style="default"
            )
        ],
        [
            InlineKeyboardButton(
                text="Назад",
                callback_data="profile:back",
                style="default"
            )
        ]
    ])
# primary - синий
# success - зеленый
# danger - красный
# default - дефолт