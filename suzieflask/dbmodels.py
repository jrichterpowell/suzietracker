from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date, create_engine

Base = declarative_base()
class Promise(Base):
    __tablename__ = 'promises'

    taskID = Column(String, primary_key=True)
    task = Column(String)
    progress = Column(Float)
    date = Column(Date)
    details = Column(String)
    references = Column(String)

    def __repr__(self):
        return "Task {}".format(str(self.taskID))