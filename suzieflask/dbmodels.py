from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date, create_engine

Base = declarative_base()
class Promise(Base):
    __tablename__ = 'promises'

    id = Column(Integer, primary_key=True)
    task = Column(String)
    progress = Column(Float)
    date = Column(Date)
    details = Column(String)
    references = Column(String)