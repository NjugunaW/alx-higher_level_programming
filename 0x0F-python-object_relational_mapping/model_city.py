#!/usr/bin/python3
"""A script that prints all City objects from the database hbtn_0e_14_usa:
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base


class City(Base):
    '''Reps a row in a cities table.
    '''
    __tablename__ = "cities"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(length=128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
    state = relationship('State', back_populates='cities')