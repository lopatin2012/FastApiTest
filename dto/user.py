from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name: str
    datetime_create: datetime
    value: int = 0
    total_time: int = 0
    is_moderator: bool = False
    is_admin: bool = False

