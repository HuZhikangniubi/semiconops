from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    environment: str = "development"
    app_name: str = "SemiconOps"
    app_version: str = "0.0.1"
    database_url: str = "postgresql+psycopg://semiconops:change_me@localhost:5432/semiconops"
    model_config = SettingsConfigDict(env_file=".env", env_prefix="SEMICONOPS_", extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings()
