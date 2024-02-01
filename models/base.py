#!/usr/bin/python3
"""base model"""

import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """defines the basemodel"""
    def __init__(self):
        """initialisation method"""
        self.id = Column(String(43), default=str(uuid.uuid4()))
        self.created_at = Column(DateTime, default=datetime.now(), nullable=False)
