from openai import AsyncOpenAI
from config import config
from aiogram import Bot

client_audio = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=config.groq_token
)

async def process_voice(file_id: str, bot: Bot):
    file = await bot.download(file=file_id)\

    transcription = await client_audio.audio.transcriptions.create(
        file=("voice.ogg", file.read()),
        model="whisper-large-v3-turbo",
        response_format="text",
        language="ru",
        prompt="Ну кароче, бля, пиздец"
    )

    return {"message": transcription}