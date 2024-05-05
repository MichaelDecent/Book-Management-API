#!/usr/bin/python3
"""
Contains class BaseModel
"""
from app import database
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel as Model
import uuid

Base = declarative_base()


class BaseModel:
    """This is a Base Model class from which other classes will be derived from"""

    id = Column(String(60), nullable=False, primary_key=True)

    def __init__(self, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())

    def __repr__(self):
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def save(self):
        """saves a new instance to the storage"""
        database.storage.new(self)
        database.storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        database.storage.delete(self)


class PydanticBaseModel(Model):
    """defines the model of the class Base Model"""

    id: str
