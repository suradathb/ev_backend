# app/core/config.py

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv


# หาไฟล์ .env ที่ root โปรเจ็กต์ (โฟลเดอร์เดียวกับ requirements.txt, app/)
BASE_DIR = Path(__file__).resolve().parents[2]  # .../ev_service_backend
ENV_PATH = BASE_DIR / ".env"

# โหลดค่า environment จาก .env (ถ้ามีไฟล์)
# override=False = ถ้ามี env จากระบบอยู่แล้ว จะไม่เขียนทับ
load_dotenv(dotenv_path=ENV_PATH, override=False)


class Settings:
    """
    Simple settings class without Pydantic dependency.
    อ่านค่าจาก environment variables (ซึ่งอาจมาจาก .env หรือจากระบบโดยตรง)
    """

    # -----------------------------
    # General app config
    # -----------------------------
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "EV Service Center Management API")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_ME_TO_A_RANDOM_SECRET")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

    # นาทีที่ token มีอายุ (default = 1 วัน)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440")
    )

    # -----------------------------
    # Database config
    # -----------------------------
    # เลือก backend ได้: mysql หรือ postgres (หรืออย่างอื่นถ้าคุณกำหนดเอง)
    DB_BACKEND: str = os.getenv("DB_BACKEND", "mysql").lower()

    # 🟢 MySQL (เชื่อม phpMyAdmin / XAMPP / WAMP ได้)
    MYSQL_URL: str = os.getenv(
        "MYSQL_URL",
        "mysql+pymysql://root:@localhost:3306/ev_service_db",
    )

    # 🟣 PostgreSQL
    # NOTE: ตอนนี้โค้ดโปรเจ็กต์เป็น SQLAlchemy แบบ sync
    # แนะนำใช้ driver sync เช่น postgresql+psycopg2 หรือ postgresql+psycopg
    # แต่ถ้าคุณใส่ postgresql+asyncpg ลงไปใน POSTGRES_URL
    # config ตรงนี้จะไม่บล็อก (แต่อาจต้องแก้โค้ดให้เป็น async engine เพิ่มในอนาคต)
    POSTGRES_URL: str = os.getenv(
        "POSTGRES_URL",
        "postgresql+psycopg2://appuser:secret123@localhost:5432/appdb",
    )

    @property
    def DATABASE_URL(self) -> str:
        """
        คืนค่า URL ตาม backend ที่เลือก:
        - DB_BACKEND = "postgres" → ใช้ POSTGRES_URL
        - ค่าอื่น ๆ (รวมถึง "mysql") → ใช้ MYSQL_URL
        """
        if self.DB_BACKEND == "postgres":
            return self.POSTGRES_URL
        return self.MYSQL_URL


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
