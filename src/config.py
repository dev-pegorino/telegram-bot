from datetime import datetime
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent
ENV_FILE = ROOT_DIR / "src" / ".env"
LOGS_DIR = ROOT_DIR / "logs"

now = datetime.now().replace(microsecond=0)
log_filename_time = now.strftime("%Y-%m-%d_%H-%M-%S")


if not ENV_FILE.exists():
    raise FileNotFoundError(f".env file not found at: {ENV_FILE}")

if not LOGS_DIR.exists():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)


class Settings(BaseSettings):
    TOKEN_BOT: SecretStr
    DB_URL: SecretStr

    COMMANDS: list[list[str]] = [
        ['start', '🔄 Restart bot | Перезагрузить бота']
    ]

    DESCRIPTION: str = """
    Бот находится в разработке!
    """

    SHORT_DESCRIPTION: str = """
    Бот находится в разработке!
    """

    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - [%(levelname)s] - %(name)s: %(message)s"
    LOG_DATE_FORMAT: str = "%d.%m.%Y %H:%M:%S"
    LOG_FILE: Path = LOGS_DIR / f"app_{log_filename_time}.log"
    
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8"
    )


settings = Settings()