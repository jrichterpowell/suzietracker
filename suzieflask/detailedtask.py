import functools
from datetime import datetime

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
)
from suzieflask.db import DBSession
from suzieflask.dbmodels import Promise

taskBP = Blueprint('detailedTask', __name__, url_prefix="/")
@taskBP.route('/task/<taskID>')
def detailedTask(taskID):
    session = DBSession()
    #should only return one object, since ID's are unique (unless we manage to produce a SHA256 collision of course hehe)
    queryResult = session.query(Promise).filter(Promise.taskID == taskID).first()
    print(queryResult.__dict__)

    if queryResult == None:
        return render_template("invalidID.html")
    else:
        #split references
        queryResult.references = queryResult.references.split('|')
        return render_template('detailedtask.html', taskdata=queryResult)

