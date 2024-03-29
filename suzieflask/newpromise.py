import functools
from datetime import datetime

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for, escape
)
from flask_wtf import RecaptchaField, FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.fields.html5 import DateField, DecimalRangeField
from wtforms.validators import InputRequired, NumberRange

import hashlib
from suzieflask.db import DBSession
from suzieflask.dbmodels import Promise

class PromiseForm(FlaskForm):
    task = TextField('What did the admin promise?', validators=[InputRequired()])
    progress = DecimalRangeField('How much progress has been made so far?',validators=[NumberRange(min=0,max=10)])
    startDate = DateField('When was this promised?', validators=[InputRequired()])
    endDate = DateField('When is/was this supposed to be completed?')
    details = TextAreaField('More detailed version of what the admin said. Provide at least one reference', validators=[InputRequired()])
    references = TextAreaField('Reference statements', validators=[InputRequired()])

    recaptcha = RecaptchaField()
    submit = SubmitField('Add')



bp = Blueprint('new', __name__, url_prefix="/")
@bp.route('/new', methods=('GET', 'POST'))
def new():
    form = PromiseForm(request.form)
    if request.method == 'POST' and form.validate():

        print("Type of the input", type(form.startDate.data), form.startDate.data)
        newPromise = Promise(
            #generate a unique ID for the task by hashing the concatenation of the taskname, 
            #details and references (it may be possible to have two tasks with the same name)
            taskID= hashlib.sha256(bytes(str(form.task.data) + str(form.details.data) + str(form.references.data), encoding='utf-8')).hexdigest(),
            task=form.task.data,
            progress=round(form.progress.data, 2),
            startdate=form.startDate.data,
            enddate=form.endDate.data,
            details=form.details.data,
            references=form.references.data,
            approved=False
        )
        #add to sql db
        session = DBSession()
        session.add(newPromise)
        session.commit()
        session.close()
        return render_template('newpromise.html', form=PromiseForm(), complete=True, home=url_for('home'))
    flash(form.errors)
    return render_template('newpromise.html', form=PromiseForm(), complete=False)

        