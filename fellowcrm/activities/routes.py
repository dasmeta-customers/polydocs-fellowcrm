

from flask import Blueprint, session
from flask_login import current_user, login_required
from flask import render_template, flash, url_for, redirect, request, jsonify
from sqlalchemy import or_, text
from datetime import date, timedelta

from fellowcrm import db
from .models import Activity
from fellowcrm.common.paginate import Paginate
from fellowcrm.common.filters import CommonFilters
from .forms import NewActivity

from fellowcrm.rbac import check_access
from wtforms import Label

import json

activities = Blueprint('activities', __name__)


@activities.route("/activities", methods=['GET', 'POST'])
@login_required
@check_access('activity', 'view')
def get_activities_view():
    query = Activity.query.filter().order_by(Activity.date_created.desc())
    if check_access('activity', 'create') == True:
        button_create = True
    else:
        button_create = False
    return render_template("activities/activities_list.html", title="Activity View",button_create=button_create, activities=Paginate(query=query))



@activities.route("/activities/new", methods=['GET', 'POST'])
@login_required
@check_access('activity', 'create')
def new_activity():
    form = NewActivity()
    if request.method == 'POST':
        if form.validate_on_submit():
            acivity = Activity(
                name=form.name.data,
                types=form.types.data
                              )

            

            db.session.add(Activity)
            db.session.commit()
            flash(_('Picklist has been successfully created!'), 'success')
            return redirect(url_for('activities.get_activities_view'))
        else:
            for error in form.errors:
                print(error)
            flash(_('Your form has errors! Please check the fields'), 'danger')
    return render_template("activities/new_activity.html", title="New Activity", form=form)

