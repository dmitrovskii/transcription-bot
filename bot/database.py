import aiosqlite

class LanguageManager:
    def __init__(self, db_path: str = "bot.db") -> None:
        self.db_path = db_path
        self._cache: dict[int, str] = {}

    async def init_db(self) -> None:
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    language_code TEXT NOT NULL DEFAULT 'uk'
                );        
            """)
            await db.commit()

            async with db.execute("SELECT user_id, language_code FROM users") as cursor:
                rows = await cursor.fetchall()
                self._cache = {row[0]: row[1] for row in rows}

    def get_languge(self, user_id: int) -> str:
        return self._cache.get(user_id, 'auto')

    async def set_language(self, user_id: int, languge_code: str) -> None:
        self._cache[user_id] = languge_code

        async with aiosqlite.connect(self.db_path) as db: 
            await db.execute("""
                INSERT INTO users (user_id, language_code)
                VALUES (?, ?)
                ON CONFLICT(user_id) DO UPDATE SET language_code = excluded.language_code;
        """, (user_id, languge_code))
            await db.commit()

lang_manager = LanguageManager()