#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from app import database
from app.database.models.base_model import Base
from app.database.models.books import Books
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from app.config import DATABASE_URL

classes = {"Books": Books}


class DBStorage:
    """This class interacts with the PostgreSQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""

        self.__engine = create_engine(str(DATABASE_URL))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class
        and its ID, or None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = database.storage.all(cls)
        obj = next((value for value in all_cls.values() if value.id == id), None)
        return obj
    
    def update_obj(self, cls, obj_id: int, **kwargs) -> None:
        """
        update the object’s attributes as passed in the method’s
        arguments then commit changes to the database
        """
        class_obj = self.find_obj_by(cls, id=obj_id)

        for key, value in kwargs.items():
            if not hasattr(class_obj, key):
                raise ValueError
            setattr(class_obj, key, value)

        self.__session.commit()
