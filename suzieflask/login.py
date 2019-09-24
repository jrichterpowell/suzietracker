import functools
from datetime import datetime

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for, escape
)
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import InputRequired

import hashlib
from suzieflask.db import DBSession
from suzieflask.dbmodels import User

class LoginForm(FlaskForm):
    username = TextField('Username: ', validators=[InputRequired()])
    password = TextField('Password: ', validators=[InputRequired()])
    submit = SubmitField('GO')



loginBP = Blueprint('login', __name__, url_prefix="/")
@loginBP.route('/login', methods=('GET', 'POST'))
def login():
    print("nothing")
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username=escape(form.username.data),
        password=hashlib.sha256(bytes(form.password.data))
        
        session = DBSession()

        query = session.query(User).filter(User.username==username).first() #usernames are unique
        
        if query == None or query.password != password:
            return render_template('login.html', form=LoginForm(), error="Invalid Username / Password")

        session.clear()
        session['logged_in'] = True
        return redirect(url_for('home'))
    return render_template('login.html', form=form, error=None)

        