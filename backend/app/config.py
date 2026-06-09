from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Lisa"
    mode: str = "dev"
    chat_native: bool = True
    dashboard_enabled: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
