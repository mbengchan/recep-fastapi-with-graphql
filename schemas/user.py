from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    about: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True