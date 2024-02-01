#!/usr/bin/python3
"""blueprint to define reviews"""

from base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """class to define reviews"""
    __tablename__ = 'review'
    text = Column(String(1024), nullable=False)
    student_id = Column(String(64), ForeignKey('student.id'), nullable=False)
    tutor_id = Column(String(64), ForeignKey('tutor.id'), nullable=False)

    def __init__(self):
        """initialising the object"""
        super().__init__()