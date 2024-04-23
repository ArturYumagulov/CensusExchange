from datetime import datetime
from typing import Any

from pydantic import BaseModel, Json


class Roles(BaseModel):
    id: int
    name: str
    permissions: Json[Any]


class User(BaseModel):
    id: int
    email: str
    username: str
    hashed_password: str
    date_joined: datetime
    last_created: datetime
    is_active: bool
    is_superuser: bool
    is_verified: bool
    roles_id: Roles
