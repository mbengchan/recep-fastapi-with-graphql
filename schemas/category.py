from typing import Optional

import strawberry
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: str | None = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    slug: str

    class Config:
        orm_mode = True

@strawberry.type
class CategoryType:
    id: str
    slug: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

@strawberry.input
class CategoryInput(BaseModel):
    name: str
    description: Optional[str] = None