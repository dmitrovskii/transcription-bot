import sys
from pathlib import Path
from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
ENV = BASE_DIR / '.env'

class Settings(BaseSettings):
    bot_token: str
    groq_token: str

    model_config = SettingsConfigDict(
        env_file=ENV,
        env_file_encoding='utf-8'
    )

try:
    config = Settings() # type: ignore
except ValidationError as e:
    print("\n[ENV ERROR] Check the .env file. Missing required environment variables:")

    for error in e.errors(): 
        field_name = str(error["loc"][0])
        print(f"    - {field_name.upper()}")

    print("\n>>> Stop.")
    sys.exit(1)