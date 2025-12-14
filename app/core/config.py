# app/core/config.py

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

# หาไฟล์ .env ที่ root โปรเจ็กต์ (โฟลเดอร์เดียวกับ requirements.txt, app/)
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

# สำคัญ: override=True เพื่อให้ .env ชนะ env ที่ระบบเคย set ไว้
load_dotenv(dotenv_path=ENV_PATH, override=True)


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "EV Service Center Management API")

    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_ME_TO_A_RANDOM_SECRET")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))

    # เลือก backend ด้วย DB_BACKEND
    DB_BACKEND: str = os.getenv("DB_BACKEND", "mysql").lower()

    # แยก URL ตาม backend
    MYSQL_URL: str = os.getenv(
        "MYSQL_URL",
        "mysql+pymysql://root:@localhost:3306/ev_service_db",
    )

    POSTGRES_URL: str = os.getenv(
        "POSTGRES_URL",
        "postgresql+psycopg2://appuser:secret123@localhost:5432/appdb",
    )

    @property
    def DATABASE_URL(self) -> str:
        if self.DB_BACKEND == "postgres":
            return self.POSTGRES_URL
        return self.MYSQL_URL


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
