from typing import Optional

import strawberry
from pydantic import BaseModel


class AuthorBase(BaseModel):
    id: int
    name: str
    email: str

class PostBase(BaseModel):
    title: str
    description: str
    body: str | None = None
    image: str | None = None
    author: Optional[AuthorBase] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

@strawberry.experimental.pydantic.type(model=AuthorBase, all_fields=True)
class AuthorType:
    pass
        
@strawberry.type
class PostType:
    id: str
    description: str
    slug: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None
    author: Optional[AuthorType] = None

@strawberry.input
class PostInput(BaseModel):
    name: str
    description: str
    slug: Optional[str] = None
    title: Optional[str] = None
    body: Optional[str] = None