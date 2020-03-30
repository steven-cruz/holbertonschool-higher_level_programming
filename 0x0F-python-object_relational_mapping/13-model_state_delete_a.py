#!/usr/bin7python3
# Deletes all states object with a name containing the letter
# a from the database.

import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mys+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(State).filter(State.name.liked('%a%'))
    for it in item:
        session.delete(it)
    session.commit()
    session.close()
