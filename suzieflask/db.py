#Modified boilerplate from sqlalchemy documentation

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import click
from flask import current_app, g
from flask.cli import with_appcontext
from suzieflask.dbmodels import Promise, Base

engine = create_engine('sqlite:///test.db', convert_unicode=True)
DBSession = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def initDB():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def getColumnNames():
    return ['Promise','Progress', 'Start Date', 'End Date (Projected)']

def getNRows(N=100):
    session = DBSession()
    rows = session.query(Promise).filter(Promise.approved == True).all()
    return [
    (r.taskID, r.task,
    [ 
    r.progress,
    r.startdate,
    r.enddate
    ])
    for r in rows]

def getDetailedPromise(id=0):
    session = DBSession()
    row = session.query(Promise.taskID == id)


@click.command('init-db')
@with_appcontext
def init_db_command():
    initDB()
    click.echo('Init new database.')