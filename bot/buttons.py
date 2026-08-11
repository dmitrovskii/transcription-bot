from aiogram import Bot
from aiogram.types import InlineKeyboardButton, BotCommand
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def setup_bot_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="🚀 Restart Bot"),
        BotCommand(command="language", description="🌐 Change language"),
    ]
    await bot.set_my_commands(commands)

def get_summary():
    builder = InlineKeyboardBuilder() 
    builder.add(
        InlineKeyboardButton(text="⭐ Summary", callback_data="button_summary")
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