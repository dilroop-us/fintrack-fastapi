from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    secret_key: str = "dev-secret-change-me"
    access_token_expire_minutes: int = 60 * 24
    database_url: str = "sqlite:///./fintrack.db"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
