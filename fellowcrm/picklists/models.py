from datetime import datetime
from fellowcrm import db
from flask_login import current_user


class Picklist(db.Model):
    id = db.Column(db.Integer, db.Sequence('picklist_id_seq'), primary_key=True)
    type = db.Column(db.String(100), nullable=False, default='LOV_TYPE')
    name = db.Column(db.String(100))
    name_lang = db.Column(db.String(100))
    lang = db.Column(db.String(5), nullable=False, default='enu')
    
    is_active = db.Column(db.Boolean, default=True)
    translate = db.Column(db.Boolean, default=True)
    order = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @staticmethod
    def picklist_list_query():
        if current_user.is_admin:
            return Picklist.query
        

    @staticmethod
    def get_label(Picklist):
        return Picklist.name

    @staticmethod
    def get_picklist(picklist_id):
        return Picklist.query.filter_by(id=picklist_id).first()
    
    @staticmethod
    def get_picklist_by_typ(type):
        return Picklist.query.filter_by(type=type)

    def __repr__(self):
        return f"Picklist('{self.name}')"

