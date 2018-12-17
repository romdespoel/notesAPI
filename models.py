from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DB = 'sqlite:///./database.db'
Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    body = Column(String(80))
    date = Column(String(80))
    archived = Column(Boolean)


engine = create_engine(DB)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

