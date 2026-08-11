import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import config
from bot.handlers import router
from bot.database import lang_manager
from bot.buttons import setup_bot_commands

bot = Bot(token=config.bot_token)
dp = Dispatcher()

dp.include_router(router)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello! Send me any voice message under 5 minutes, and I'll convert it to text.")

async def main():
    print(">>> Start...")
    try:

        await lang_manager.init_db()
        await setup_bot_commands(bot)
        await dp.start_polling(bot)

    finally:
        print(">>> Stop.")

if __name__ == "__main__":
    asyncio.run(main())