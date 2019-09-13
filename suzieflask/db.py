#Modified boilerplate from sqlalchemy documentation

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import click
from flask import current_app, g
from flask.cli import with_appcontext

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
DBSession = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()

def initDB():
    from suzieflask.dbmodels import Promise
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

@click.command('init-db')
@with_appcontext
def init_db_command():
    initDB()
    click.echo('Init new database.')