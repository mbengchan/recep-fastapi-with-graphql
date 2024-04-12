from datetime import datetime

from database.dbconfig import Base
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .category import Category
from .user import User


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title: str = Column(String(50), nullable=False)
    author_id: int = Column(Integer, ForeignKey("users.id"))
    category_id: int = Column(Integer, ForeignKey("categories.id"))
    slug: str = Column(String(50), unique=True, nullable=False)
    description: str = Column(String(255), nullable=False)
    body: str = Column(String)
    image: str = Column(String)
    dateCreated: Column = Column(DateTime, default=datetime.utcnow)
    dateUpdated: Column = Column(DateTime, onupdate=datetime.utcnow)
    isPuplished: bool = Column(Boolean, default=False)

    # class Config:
    #     orm_mode = True


    category = relationship("Category", back_populates="posts")
    author = relationship("User", back_populates="posts")