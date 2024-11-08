from pathlib import Path
from pydantic import BaseModel

DB_PATH = Path(__file__).parent / "db.sqlite3"


class DBSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"


class Settings(BaseModel):
    db: DBSettings = DBSettings()
    static_dir_path: Path = "./static"

settings = Settings()
print(settings.db.url)
