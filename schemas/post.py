from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: str
    body: str | None = None
    image: str | None = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True