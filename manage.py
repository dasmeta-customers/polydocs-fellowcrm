from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from fellowcrm.config import DevelopmentConfig, TestConfig, ProductionConfig
from datetime import datetime
import os


from fellowcrm import create_app

app = create_app()

#app = Flask(__name__, instance_relative_config=True)

config_class = ProductionConfig()
if os.getenv('FLASK_ENV') == 'development':
    config_class = DevelopmentConfig()
elif os.getenv('FLASK_ENV') == 'production':
    config_class = ProductionConfig()
elif os.getenv('FLASK_ENV') == 'testing':
    config_class = TestConfig()

app.config.from_object(config_class)

db = SQLAlchemy(app)
migrate = Migrate(app, db)




manager = Manager(app)
manager.add_command('db', MigrateCommand)






from fellowcrm.users.models import *
from fellowcrm.leads.models import * 






class TestUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    test = db.Column(db.String(128))






if __name__ == '__main__':
    manager.run()
