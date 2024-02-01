#!/usr/bin/python3
"""blueprint of student details"""

import hashlib
from base import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Student(BaseModel, Base):
    """class to define a student"""
    __tablename__ = "student"
    first_name = Column(String(123), nullable=True)
    last_name = Column(String(123), nullable=True)
    email = Column(String(120), nullable=False)
    phone_number = Column(String(25), nullable=False)
    _password = Column('password', String(125), nullable=False)
    tutor_id = Column(String(123), ForeignKey('tutor.id'), nullable=False)
    subject = relationship("Subject", backref="student", cascade="all delete-orphan")

    def __init__(self):
        """initialisation of the object"""
        super().__init__()

    @property
    def password(self):
        """password getter"""
        return self._password
    
    @property.setter
    def password(self, pwd):
        """sets password"""
        self._password = hashlib.md5(pwd.encode()).hexdigest()