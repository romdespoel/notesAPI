from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base

DB = 'sqlite:///./database.db'
Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    body = Column(String(80))
    date = Column(String(80))

engine = create_engine(DB)
if not database_exists(engine.url):
    create_database(engine.url)
