from aiogram import Router, Bot, F
from aiogram.types import Message
from service import process_voice

router = Router()

@router.message(F.voice.duration <= 300)
async def transcriptions(message: Message, bot: Bot):
    if message.voice is None:
        await message.reply("Something went wrong. Please send voice message again")
        return

    file_id = message.voice.file_id

    text_from_voice = await process_voice(file_id=file_id, bot=bot)
    await message.answer(text_from_voice['message'])