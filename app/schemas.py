from typing import Optional, List
from pydantic import BaseModel


class UserBase(BaseModel):
    login: str
    info: Optional[str] = None
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
