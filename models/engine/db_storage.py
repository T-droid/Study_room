#!/usr/bin/python3
"""blueprint of the storage engine"""

from models.base import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import os



class DB_storage:
    """defines the db storage system"""
    __engine = None
    __session = None
    def __init__(self):
        """initialisation method"""
        db_user = os.environ['MY_SQL_USER'] if 'MY_SQL_USER' in os.environ else None
        db_pwd = os.environ['MY_SQL_PWD'] if 'MY_SQL_PWD' in os.environ else None
        db_host = os.environ['MY_SQL_HOST'] if 'MY_SQL_HOST' in os.environ else None
        db_name = os.environ['MY_SQL_NAME'] if 'MY_SQL_NAME' in os.environ else None
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(db_user, db_pwd, db_host, db_name))
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def save(self):
        """saves all changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes object"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads the database session"""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """creates new object"""
        self.__session.add(obj)

    def close(self):
        """disposes of the current session if active"""
        self.__session.remove()

    