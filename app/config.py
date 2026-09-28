import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Lowercase attributes (main.py thevapaduradhu)
    app_name: str = os.getenv("APP_NAME", "FitBuddy")
    app_env: str = os.getenv("APP_ENV", "development")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./fitbuddy.db")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    workout_model: str = os.getenv("WORKOUT_MODEL", "gemini-2.5-flash")
    nutrition_model: str = os.getenv("NUTRITION_MODEL", "gemini-2.5-flash")
    admin_token: str = os.getenv("ADMIN_TOKEN", "fitbuddy-admin-token")

    # Uppercase aliases (safe-ku)
    APP_NAME: str = app_name
    APP_ENV: str = app_env
    DATABASE_URL: str = database_url
    GEMINI_API_KEY: str = gemini_api_key
    WORKOUT_MODEL: str = workout_model
    NUTRITION_MODEL: str = nutrition_model
    ADMIN_TOKEN: str = admin_token

settings = Settings()