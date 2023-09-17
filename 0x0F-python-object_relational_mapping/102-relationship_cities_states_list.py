#!/usr/bin/python3
'''A script that lists all City objects from the database hbtn_0e_101_usa
'''
import sys
from sqlalchemy import create_engine, and_, text, tuple_
from sqlalchemy.orm import sessionmaker, relationship

from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user_name = sys.argv[1]
        pass_word = sys.argv[2]
        data = sys.argv[3]
        DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(
            user_name, pass_word, data
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        qstn = session.query(City).join(State).order_by(City.id.asc())
        for city in qstn.all():
            print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
