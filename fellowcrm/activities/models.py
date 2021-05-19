import configparser
from datetime import datetime
from fellowcrm import db
from flask_login import current_user

import json 
config = configparser.ConfigParser()
config.read('acitivities.ini')

class Activity(db.Model):
    
    id = db.Column(db.Integer, db.Sequence('activity_id_seq'), primary_key=True)

    typ = db.Column(db.String(100))
    parent_typ = db.Column(db.String(100))
    name = db.Column(db.String(100))
    parent_name = db.Column(db.String(100))

    priority = db.Column(db.String(50))
    status = db.Column(db.String(50))

    description = db.Column(db.Text)

    date_due = db.Column(db.DateTime)
    date_start = db.Column(db.DateTime)
    
    
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)
    
 

    def __repr__(self):
        return f"Activity('{self.name}')"

