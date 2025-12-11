# app/core/config.py

import os
from functools import lru_cache


class Settings:
    """
    Simple settings class without Pydantic dependency.
    อ่านค่าได้จาก environment variable ถ้ามี
    ถ้าไม่มีก็ใช้ค่า default ตามที่กำหนดไว้ด้านล่าง
    """

    PROJECT_NAME: str = "EV Service Center Management API"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_ME_TO_A_RANDOM_SECRET")
    ALGORITHM: str = "HS256"

    # นาทีที่ token มีอายุ (ค่า default = 1 วัน)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440")
    )

    # ค่า default ใช้ SQLite ไฟล์ ev_service.db ในโฟลเดอร์โปรเจ็กต์
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ev_service.db")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
