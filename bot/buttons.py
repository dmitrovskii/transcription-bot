from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_summary():
    builder = InlineKeyboardBuilder() 
    builder.add(
        InlineKeyboardButton(text="⬇️ Стислий зміст", callback_data="button_summary")
    )
    return builder.as_markup()