#!/usr/bin/python3
'''
Deletes all states containing letter a
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    for instance in session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id):
        session.delete(instance)

    session.commit()
    session.close()
