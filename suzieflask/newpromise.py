import functools
from datetime import datetime

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
)
from flask_wtf import RecaptchaField, FlaskForm
from wtforms import TextField, DateField
import hashlib
from suzieflask.db import DBSession
from suzieflask.dbmodels import Promise

class PromiseForm(FlaskForm):
    task = TextField('Task - What did the admin promise?')


bp = Blueprint('new', __name__, url_prefix="/")
@bp.route('/new', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        task = request.form['task']
        progress = request.form['progress']
        dateIn = datetime.strptime(request.form['date'], "%Y-%m-%d")
        details = request.form['details']
        references = request.form['references']


        error = None

        if not task:
            error = "Task required"
        if not progress:
            error = "Progress required"
        if not dateIn:
            error = "Date required"
        if error is None:
            newPromise = Promise(
                taskID= hashlib.sha256(bytes(task, encoding='utf-8')).hexdigest(),
                task=task,
                progress=progress,
                date=dateIn,
                details=details,
                references=references
            )
            #add to sql db
            session = DBSession()
            session.add(newPromise)
            session.commit()
            session.close()
            #return redirect(url_for('home'))

    return render_template('newpromise.html', recaptcha=RecaptchaField())

        