from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "postgresql://kejtqvxkjmoedf:553ae1b9e2d55e048ad62b5e12027494f77619b75bc7271f6ddacf6be31963b7@ec2-52-203-164-61.compute-1.amazonaws.com/d57fbsc4odolv7"
        self.session = None

    def get_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
