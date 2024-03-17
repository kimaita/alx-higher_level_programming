#!/usr/bin/pythn3
"""lists all State objects, and corresponding City objects, 
contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    with Session(engine) as session:
        stmt = select(State).order_by('id')
        
        for state in session.scalars(stmt):
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")
