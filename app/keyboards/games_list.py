from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def menu_games() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎰 50/50",
                callback_data="main_game:50/50",
                style="primary"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔫 Русская рулетка",
                callback_data="main_game:roullete",
                style="success"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎲 Кости",
                callback_data="main_game:Dice",
                style="danger"
            )
        ],
        [
            InlineKeyboardButton(
                text="Меню",
                callback_data="main_game:back_to_menu",
                style="default"
            )
        ]
    ])
# primary - синий
# success - зеленый
# danger - красный
# default - дефолт