from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    APP_NAME: str = "SHL Assessment Agent"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Mistral
    MISTRAL_API_KEY: str
    MODEL_NAME: str = "mistral-small-latest"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()