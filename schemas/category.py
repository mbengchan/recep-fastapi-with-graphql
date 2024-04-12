from pydantic import BaseModel


class CateogryBase(BaseModel):
    name: str
    description: str | None = None

class CateogryCreate(CateogryBase):
    pass

class Cateogry(CateogryBase):
    id: int

    class Config:
        orm_mode = True