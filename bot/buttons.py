from aiogram import Bot
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_summary():
    builder = InlineKeyboardBuilder() 
    builder.add(
        InlineKeyboardButton(text="⬇️ Стислий зміст", callback_data="button_summary")
    )
    return builder.as_markup()

def get_language_keyboard():
    builder = InlineKeyboardBuilder() 
    builder.add(
        InlineKeyboardButton(text="EN", callback_data="lang_en"),
        InlineKeyboardButton(text="UA", callback_data="lang_uk"),
        InlineKeyboardButton(text="Auto", callback_data="lang_auto")
    )
    return builder.as_markup()