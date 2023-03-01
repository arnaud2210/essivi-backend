import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = 587
    SMTP_HOST: Optional[str] = "smtp.mailgun.org"
    SMTP_USER: Optional[str] = "postmaster@essivi-api.me"
    SMTP_PASSWORD: Optional[str] = "cf232843907fd7418043ded515b3207f-15b35dee-ce842eee"
    EMAILS_FROM_EMAIL: Optional[EmailStr] = "brad@essivi-api.me"
    EMAILS_FROM_NAME: Optional[str] = "ESSIVI-SARL"

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "../email-templates/build"
    EMAILS_ENABLED: bool = True

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    #EMAIL_TEST_USER: EmailStr = "brad@essivi-api.me"  # type: ignore
    #FIRST_SUPERUSER: EmailStr = "adjimonarnaud@gmail.com"
    #FIRST_SUPERUSER_PASSWORD: str = "naud.2002"
    USERS_OPEN_REGISTRATION: bool = True

    class Config:
        case_sensitive = True


settings = Settings()