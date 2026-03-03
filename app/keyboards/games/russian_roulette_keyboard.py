from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def russian_roulette() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔫 Спустить курок",
                callback_data="russian_roulette:shoot"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Назад",
                callback_data="russian_roulette:back"
            )
        ]
    ])
# primary - синий
# success - зеленый
# danger - красный
# default - дефолт