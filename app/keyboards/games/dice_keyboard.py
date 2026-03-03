from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def dice_game() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎲 Кинуть кость",
                callback_data="dice_game:roll_dice"
            ),
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