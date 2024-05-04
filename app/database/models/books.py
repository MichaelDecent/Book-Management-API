#!/usr/bin/python3
"""
contains class Books
"""
from app.database.models.base_model import Base, BaseModel, PydanticBaseModel
from sqlalchemy import String, Column, Integer
from pydantic import BaseModel as PydanticModel


class Books(BaseModel, Base):
    """Describes the book table"""

    __tablename__ = "books"

    title = Column(String(256), nullable=False)
    author = Column(String(256), nullable=False)
    year = Column(Integer, nullable=False)
    isbn = Column(String(256), nullable=False)

    def __init__(self, **kwargs):
        """initializes books"""
        super().__init__(**kwargs)


class BooksIn(PydanticModel):
    """defines attributes of Book Model for request body"""

    title: str
    author: str
    year: int
    isbn: str


class BooksOut(PydanticBaseModel):
    """defines attributes of Book Model for response body"""

    title: str
    author: str
    year: int
    isbn: str
