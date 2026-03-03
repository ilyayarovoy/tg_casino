from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Профиль",
                callback_data="main_menu:profile",
                style="primary"
            )
        ],
        [
            InlineKeyboardButton(
                text="Игры",
                callback_data="main_menu:game",
                style="success"
            )
        ]
    ])
# primary - синий
# success - зеленый
# danger - красный
# default - дефолт