from flask import render_template, session, url_for, redirect, Blueprint, request
from fellowcrm import db, bcrypt
import os
import sys
from flask import current_app
from tzlocal import get_localzone

from fellowcrm.settings.models import Currency, TimeZone, AppConfig
from fellowcrm.leads.models import LeadSource, LeadStatus, Lead
from fellowcrm.accounts.models import Account
from fellowcrm.contacts.models import Contact
from fellowcrm.deals.models import DealStage, Deal
from fellowcrm.users.models import Role, Resource, User

from fellowcrm.install.forms import NewSystemUser, CurrencyTz, FinishInstall
from fellowcrm.install.data.currency_timezone import INSERT_SQL
from fellowcrm.install.data.sample_data import SAMPLE_DATA

upgrade = Blueprint('upgrade', __name__)


@upgrade.route("/upgrade", methods=['GET', 'POST'])
def sys_upgrade_info():

    # create empty tables
    #db.create_all()

  
    return render_template("upgrade/sys_info.html", title="System Information",
                           system_info=os.uname(), py_ver=sys.version)



@current_app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('upgrade.sys_info'))

