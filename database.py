from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB = 'sqlite:///./database.db'
Base = declarative_base()

engine = create_engine(DB)
Base.metadata.create_all(engine)

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB))
session = scoped_session(Session)