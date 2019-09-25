from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date, create_engine,Boolean

Base = declarative_base()
class Promise(Base):
    __tablename__ = 'promises'

    taskID = Column(String, primary_key=True)
    task = Column(String)
    progress = Column(Float)
    startdate = Column(Date)
    enddate = Column(Date)
    details = Column(String)
    references = Column(String)
    approved = Column(Boolean)

    def __repr__(self):
        return "Task {}".format(str(self.taskID))

class User(Base):
    __tablename__='users'
    username = Column(String, primary_key=True)
    password = Column(String)
    dateCreated = Column(Date)

    def __userid__():
        return 