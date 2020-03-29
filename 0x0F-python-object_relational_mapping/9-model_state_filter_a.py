#!/usr/bin/python3
# lists all State objects that contain the letter a from the database.

import slqalchemy
import sys
from sqlachemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, state

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for item in session.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id):
        print("{}: {}".format(item.id, item.name))

    session.close()
