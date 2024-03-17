#!/usr/bin/python3
"""This module defines an SQLAlchemy ORM class"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """SQLAlchemy ORM class representing a City"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", back_populates="cities")
