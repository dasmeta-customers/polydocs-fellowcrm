from fellowcrm.picklists.models import Picklist
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email
from wtforms_sqlalchemy.fields import QuerySelectField

from fellowcrm.users.models import User


class NewPicklist(FlaskForm):
    types = QuerySelectField('Type', query_factory=Picklist.get_picklist_by_typ, get_pk=lambda a: a.id,
                                 get_label=Picklist.get_label,allow_blank=True, blank_text='LOV_TYPE')
    #type = StringField('Picklist Type', validators=[DataRequired(message='Picklist Type is mandatory')])
    name = StringField('Picklist Name', validators=[DataRequired(message='Picklist name is mandatory')])
    lang = StringField('Picklist Lang')
    
    name_lang = StringField('Language-Independent')
    order = IntegerField('Order')

    is_active = BooleanField('Picklist is active')
    translate = BooleanField('Translation')
    submit = SubmitField('Create New Picklist')


def filter_accounts_adv_filters_query():
    return [
        {'id': 1, 'title': 'Active'},
        {'id': 2, 'title': 'Inactive'},
        {'id': 3, 'title': 'Created Today'},
        {'id': 4, 'title': 'Created Yesterday'},
        {'id': 5, 'title': 'Created In Last 7 Days'},
        {'id': 6, 'title': 'Created In Last 30 Days'}
    ]

class PicklistTyp(FlaskForm):
    assignees = QuerySelectField(query_factory=User.user_list_query, get_pk=lambda a: a.id,
                                 get_label=User.get_label, allow_blank=True, blank_text='[-- Select Owner --]')

class FilterAccounts(FlaskForm):
    txt_search = StringField()
    assignees = QuerySelectField(query_factory=User.user_list_query, get_pk=lambda a: a.id,
                                 get_label=User.get_label, allow_blank=True, blank_text='[-- Select Owner --]')
    advanced_user = QuerySelectField(query_factory=filter_accounts_adv_filters_query,
                                     get_pk=lambda a: a['id'],
                                     get_label=lambda a: a['title'],
                                     allow_blank=True, blank_text='[-- advanced filter --]')

    submit = SubmitField('Filter Accounts')
