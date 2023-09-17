#!/usr/bin/python3
'''A script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
        result = session.query(State).order_by(State.id.asc()).all()
        for state in result:
            print('{}: {}'.format(state.id, state.name))
            for city in state.cities:
                print('\t{}: {}'.format(city.id, city.name))
        session.close()
