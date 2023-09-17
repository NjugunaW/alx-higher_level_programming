#!/usr/bin/python3
'''A script that creates the State “California” with the City “San Francisco” from the database
hbtn_0e_100_usa: (100-relationship_states_cities.py)
'''
import sys
from sqlalchemy import create_engine
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
        state_1 = State(name='California')
        city_1 = City(name='San Francisco')
        state_1.cities.append(city_1)
        session.add(state_1)
        session.commit()