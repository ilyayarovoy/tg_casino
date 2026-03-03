from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def fifty_fifty_game() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="1️⃣",
                callback_data="fifty_fifty_game:1"
            ),
            InlineKeyboardButton(
                text="2️⃣",
                callback_data="fifty_fifty_game:2"
            )
        ],
        [
            InlineKeyboardButton(
                text="Назад",
                callback_data="fifty_fifty_game:back"
            )
        ]
    ])
# primary - синий
# success - зеленый
# danger - красный
# default - дефолт