import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import config
from bot.handlers import router

bot = Bot(token=config.bot_token)
dp = Dispatcher()

dp.include_router(router)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello! Send me a file until 5 minute.")

async def main():
    print(">>> Start...")
    try:
        await dp.start_polling(bot)
    finally:
        print(">>> Stop.")

if __name__ == "__main__":
    asyncio.run(main())