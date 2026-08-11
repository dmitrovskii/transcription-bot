from aiogram import Router, Bot, F
from aiogram.filters import Command 
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.service import process_voice, process_text
from bot.buttons import get_summary, get_language_keyboard
from bot.database import lang_manager

router = Router()

@router.message(F.voice.duration <= 300)
async def transcriptions(message: Message, state: FSMContext, bot: Bot):
    if message.voice is None:
        await message.reply("Something went wrong. Please try sending the voice message again.")
        return

    voice_id = message.voice.file_id

    lang_code = lang_manager.get_languge(message.from_user.id)
    text_from_voice = await process_voice(file_id=voice_id, language_code=lang_code, bot=bot)

    if message.voice.duration >= 90:
        await state.update_data(transcribed_text=text_from_voice['message'])
        await message.reply(text=text_from_voice['message'], reply_markup=get_summary())
        return 

    await message.reply(text_from_voice['message'])

@router.message(Command("language"))
async def language(message: Message):
    await message.answer(text="Please choose your preferred language: \n• Auto-detect: automatically identifies the language, though specifying a exact language yields slightly better accuracy.", reply_markup=get_language_keyboard())

@router.callback_query(F.data.startswith("lang_"))
async def language_choice(callback: CallbackQuery):
    await callback.answer()

    selected_lang = callback.data.split("_")[1] 
    await lang_manager.set_language(callback.from_user.id, selected_lang)
    await callback.message.answer(f"Language switched to: {selected_lang.upper()}")

@router.callback_query(F.data == "button_summary")
async def button_summary(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    user_data = await state.get_data()
    transcribed_text = user_data.get("transcribed_text")

    if not transcribed_text:
        await callback.message.answer("Something went wrong. Please try sending the voice message again.")
        return

    text_summary = await process_text(transcribed_text)
    await callback.message.reply(str(text_summary["message"]))
    await state.clear()