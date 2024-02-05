#!/usr/bin/python3
"""base model"""

import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()

class BaseModel(Base):
    """defines the basemodel"""
    __abstract__ = True
    id = Column(String(43), primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    def save(self):
        """updates the attribute updated at"""
        cls.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()