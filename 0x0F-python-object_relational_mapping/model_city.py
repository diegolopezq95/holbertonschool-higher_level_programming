#!/usr/bin/python3
""" This module create Class Base.
See:
    ./6-model_state.py test file
"""


import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from model_state import State


class City(Base):
    """
    class City that inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state_id"), nullable=False)
