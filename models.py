from sqlalchemy import Column, String, Integer
from database import Base

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    body = Column(String(80))
    date = Column(String(80))


