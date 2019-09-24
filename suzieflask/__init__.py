import os

from flask import Flask, render_template
from suzieflask.db import DBSession, init_db_command, getColumnNames, getNRows
from suzieflask import config
from flask_wtf import CSRFProtect

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'suzietracker.sqlite'),
    )

    app.config.from_object(config.Development)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        #do we not want to handle this?
        pass

    @app.route('/')
    def home():
        columns = getColumnNames()
        rows = getNRows()
        return render_template("home.html", tableColumns=columns, rows=rows)


    @app.route('/about')
    def about():
        return ""
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        DBSession.remove()

    app.cli.add_command(init_db_command)

    from . import newpromise, detailedtask, login
    app.register_blueprint(newpromise.bp)
    app.register_blueprint(detailedtask.taskBP)
    app.register_blueprint(login.loginBP)

    CSRFProtect().init_app(app)
    
    return app


