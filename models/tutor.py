#!/usr/bin/python3
"""tutor details template"""

import hashlib
from models.base import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Tutor(BaseModel, Base):
    """class to define tutor"""
    __tablename__ = 'tutor'
    first_name = Column(String(43), nullable=True)
    last_name = Column(String(43), nullable=True)
    email = Column(String(120), nullable=False)
    phone_number = Column(String(25), nullable=False)
    _password = Column('password', String(128), nullable=False)
    student = relationship("Student", backref="tutor", cascade="all, delete-orphan")
    subject = relationship("Subject", backref="tutor", cascade="all,  delete-orphan")

    def __init__(self):
        """initialisation of the object"""
        super().__init__()

    @property
    def password(self):
        """password getter"""
        return self._password
    
    @password.setter
    def password(self, pwd):
        """sets password"""
        self._password = hashlib.md5(pwd.encode()).hexdigest()
