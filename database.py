from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

DB = 'sqlite:///./database.db'
Base = declarative_base()

engine = create_engine(DB)
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(autoFlush=False, bind=engine)
session = scoped_session(Session)

