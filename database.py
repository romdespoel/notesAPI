from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models import DB

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB))
session = scoped_session(Session)