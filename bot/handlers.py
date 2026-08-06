from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.service import process_voice, process_text
from bot.buttons import get_summary

router = Router()

@router.message(F.voice.duration <= 300)
async def transcriptions(message: Message, state: FSMContext, bot: Bot):
    if message.voice is None:
        await message.reply("Something went wrong. Please send voice message again")
        return

    voice_id = message.voice.file_id

    text_from_voice = await process_voice(file_id=voice_id, bot=bot)

    if message.voice.duration >= 90:
        await state.update_data(transcribed_text=text_from_voice['message'])
        await message.answer(text=text_from_voice['message'], reply_markup=get_summary())
        return 

    await message.answer(text_from_voice['message'])

@router.callback_query(F.data == "button_summary")
async def button_summary(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    user_data = await state.get_data()
    transcribed_text = user_data.get("transcribed_text")

    if not transcribed_text:
        await callback.message.answer("Something went wrong. Please send voice message again")
        return

    text_summary = await process_text(transcribed_text)
    await callback.message.answer(str(text_summary["message"]))
    await state.clear()