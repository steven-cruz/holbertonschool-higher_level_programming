#!/usr/bin/python3
# """ Start link class to table in database """"

import sqlalchemy import create_engine
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, state


if __name__ = "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_pping=True)
    Base.metadata.create_all(engine)
    Session = sessionmarker(bind=engine)
    session = Seccion()
    for item in session.query(State).order_by(State.id):
        print("{}: {}".format(item.id, item.name))
