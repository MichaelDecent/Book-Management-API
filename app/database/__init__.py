#!/usr/bin/python3
"""
initialize the models package
"""
from app.database.storage import DBStorage


storage = DBStorage()

storage.reload()
