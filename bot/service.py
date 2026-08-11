from openai import AsyncOpenAI
from config import config
from aiogram import Bot

client_audio = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=config.groq_token
)

client_text = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=config.groq_token
)

async def process_voice(file_id: str, language_code: str, bot: Bot):
    file = await bot.download(file=file_id)

    params = {
        "file": ("voice.ogg", file.read()),  # type: ignore
        "model": "whisper-large-v3-turbo",
        "response_format": "text",
    }

    if language_code and language_code != "auto":
        params["language"] = language_code

    transcription = await client_audio.audio.transcriptions.create(**params)

    return {"message": transcription}

async def process_text(transcribed_text: str):
    response = await client_text.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "assistant",
                "content": "Summarize the following text. Constraint 1: Respond ONLY in the same language as the input text. Constraint 2: Keep it very brief (max 4-5 sentences or plain bullet points). Constraint 3: Do NOT use Markdown (no bolding, no asterisks, no hashes). Constraint 4: Focus only on the core idea, ignore all fluff and filler words. Perspective: Use third-person perspective ONLY (refer to the speaker as 'автор', 'користувач', 'человек' or 'людина'). 3. NEVER address the reader or the speaker as 'you' ('ты', 'вы', 'ти', 'ви')." 
            },
            {
                "role": "user", "content": transcribed_text
            }
        ],
        temperature=0.3
    )
    return {"message": response.choices[0].message.content}