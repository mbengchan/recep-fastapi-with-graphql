from database.dbconfig import Base
from sqlalchemy import Boolean, Column, Integer, String


class Category(Base):
    __tablename__ = "categories"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50), nullable=False)
    slug: str = Column(String(50), unique=True, nullable=False)
    description: str = Column(String(100))
    is_active: bool = Column(Boolean, default=True)