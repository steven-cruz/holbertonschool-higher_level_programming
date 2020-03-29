#!/usr/bin7python3
# changes the name of a State object from the database


import slqalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_sate import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(State).filter_by(id=2).first()
    item.name = 'New Mexico'
    session.commit()
    session.close()
