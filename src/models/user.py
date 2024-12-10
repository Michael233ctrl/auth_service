from typing import Any, Optional
from datetime import datetime
from pydantic import EmailStr
from odmantic import ObjectId, Field

from src.db.base_class import Base


def datetime_now_sec():
    return datetime.now().replace(microsecond=0)


class User(Base):
    created: datetime = Field(default_factory=datetime_now_sec)
    modified: datetime = Field(default_factory=datetime_now_sec)
    full_name: str = Field(default="")
    email: EmailStr
    hashed_password: Any = Field(default=None)
    is_active: bool = Field(default=False)
    is_superuser: bool = Field(default=False)
    refresh_tokens: list[ObjectId] = Field(default_factory=list)