from database.dbconfig import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    __tablename__ = "users"

    # Define the columns of the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=True, unique=True)
    about = Column(String(255))
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)