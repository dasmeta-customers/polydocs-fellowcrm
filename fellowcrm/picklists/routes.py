from flask import Blueprint, session
from flask_login import current_user, login_required
from flask import render_template, flash, url_for, redirect, request
from sqlalchemy import or_, text
from datetime import date, timedelta

from fellowcrm import db
from .models import Picklist
from fellowcrm.common.paginate import Paginate
from fellowcrm.common.filters import CommonFilters
from .forms import NewPicklist

from fellowcrm.rbac import check_access
from wtforms import Label

picklists = Blueprint('picklists', __name__)

@picklists.route("/picklist", methods=['GET', 'POST'])
@login_required
@check_access('picklists', 'view')
def get_picklists_view():
    query = Picklist.query.filter().order_by(Picklist.date_created.desc())
    return render_template("picklists/picklist_list.html", title="Picklist View",
                        picklists=Paginate(query=query))


@picklists.route("/picklists/edit/<int:picklist_id>", methods=['GET', 'POST'])
@login_required
@check_access('picklists', 'update')
def update_picklist(picklist_id):
    picklist = Picklist.get_picklist(picklist_id)
    if not picklist:
        return redirect(url_for('picklists.get_picklists_view'))

    form = NewPicklist()
    if request.method == 'POST':
        if form.validate_on_submit():
            picklist.type = form.types.data
            picklist.name = form.name.data
            picklist.lang = form.lang.data
            picklist.order = form.order.data
            picklist.name_lang = form.name_lang.data
            picklist.is_active = form.is_active.data
            picklist.translate = form.translate.data
            
            db.session.commit()
            flash('The Picklist has been successfully updated', 'success')
            return redirect(url_for('picklists.get_picklists_view', picklist_id=picklist.id))
        else:
            print(form.errors)
            flash('Picklists update failed! Form has errors', 'danger')
    elif request.method == 'GET':
        form.type.data = picklist.types
        form.name.data = picklist.name
        form.name_lang.data = picklist.name_lang
        
        form.lang.data = picklist.lang
        form.order.data = picklist.order
        form.name_lang.data = picklist.name_lang

        form.is_active.data = picklist.is_active
        form.translate.data = picklist.translate

        form.submit.label = Label('update_picklist', 'Update Picklist')
    return render_template("picklists/new_picklist.html", title="Update Picklist", form=form)


@picklists.route("/picklists/new", methods=['GET', 'POST'])
@login_required
@check_access('picklists', 'create')
def new_picklist():
    form = NewPicklist()
    if request.method == 'POST':
        if form.validate_on_submit():
            picklist = Picklist(
                               name=form.name.data,
                               type=form.types.data,
                               lang=form.lang.data,
                               is_active=form.is_active.data,
                               translate=form.translate.data,
                               order=form.order.data,
                               name_lang=form.name_lang.data
                              )

            

            db.session.add(picklist)
            db.session.commit()
            flash('Picklist has been successfully created!', 'success')
            return redirect(url_for('picklists.get_picklists_view'))
        else:
            for error in form.errors:
                print(error)
            flash('Your form has errors! Please check the fields', 'danger')
    return render_template("picklists/new_picklist.html", title="New Picklist", form=form)



@picklists.route("/picklists/del/<int:picklist_id>")
@login_required
@check_access('picklists', 'delete')
def delete_picklist(picklist_id):
    Picklist.query.filter_by(id=picklist_id).delete()
    db.session.commit()
    flash('Picklist removed successfully!', 'success')
    return redirect(url_for('picklists.get_picklists_view'))



@picklists.route("/picklists/<int:picklist_id>")
@login_required
@check_access('picklists', 'view')
def get_picklist_view(picklist_id):
    picklist = Picklist.query.filter_by(id=picklist_id).first()
    return render_template("picklists/picklist_view.html", title="View Picklist", picklist=picklist)
