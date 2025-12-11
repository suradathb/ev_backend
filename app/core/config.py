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

    # 🟢 ใช้ MySQL (เชื่อมกับ phpMyAdmin)
    # แก้ user / password / dbname ให้ตรงกับเครื่องคุณ
    # ตัวอย่างนี้: user=root, ไม่มี password, database=ev_service_db, host=localhost, port=3306
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost:3306/ev_service_db",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
