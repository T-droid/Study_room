#!/usr/bin/python3
"""blueprint do define subject"""

from models.base import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Subject(BaseModel, Base):
    """class to define subject"""
    __tablename__ = 'subject'
    subject_name = Column(String(43), nullable=True)
    student = relationship("Student", backref="subject", cascade="all, delete-orphan")
    tutor = relationship("Tutor", backref="subject", cascade="all, delete-orphan")