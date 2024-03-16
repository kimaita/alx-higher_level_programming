#!/usr/bin/python3
"""This module defines SQLAlchemy ORM classes"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """SQLAlchemy ORM class representing a State"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
