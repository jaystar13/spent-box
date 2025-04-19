from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "SpentBox"
    API_VERSION: str = "v1"

    # 예시 환경변수
    DATABASE_URL: str = "sqlite:///./spentbox.db"

    class Config:
        env_file = ".env"


settings = Settings()
