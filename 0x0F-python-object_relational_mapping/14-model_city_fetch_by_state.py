#!/usr/bin/python3
'''A script that prints all City objects from the database hbtn_0e_14_usa:
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user_name = sys.argv[1]
        pass_word = sys.argv[2]
        data = sys.argv[3]
        DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(
            user_name, pass_word, data
        )
        engine = create_engine(DATABASE_URL)
        State.cities = relationship('City', back_populates='state')
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        result = session.query(City).order_by(City.id.asc()).all()
        for row in result:
            print('{}: ({}) {}'.format(row.state.name, row.id, row.name))