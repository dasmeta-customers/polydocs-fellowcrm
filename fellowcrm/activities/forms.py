from fellowcrm.activities.models import Activity

from fellowcrm.picklists.models import Picklist
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email
from wtforms_sqlalchemy.fields import QuerySelectField

from fellowcrm.users.models import User


class NewActivity(FlaskForm):
    types = QuerySelectField('Type', query_factory=Picklist.get_picklist_by_typ('Test'), get_pk=lambda a: a.id,
                                 get_label=Picklist.get_label,allow_blank=True, blank_text='')
    #type = StringField('Picklist Type', validators=[DataRequired(message='Picklist Type is mandatory')])
    name = StringField('Picklist Name', validators=[DataRequired(message='Picklist name is mandatory')])
    
    submit = SubmitField('Create New Picklist')
