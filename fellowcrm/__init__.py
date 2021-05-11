from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

from .config import DevelopmentConfig, TestConfig, ProductionConfig, DigitalocenDEV

# database handle
db = SQLAlchemy(session_options={"autoflush": False})

# encryptor handle
bcrypt = Bcrypt()

# manage user login
login_manager = LoginManager()

# function name of the login route that
# tells the path which facilitates authentication
login_manager.login_view = 'users.login'


def run_install(app_ctx):
    from fellowcrm.install.routes import install
    app_ctx.register_blueprint(install)
    return app_ctx




def create_app(config_class=ProductionConfig):
    app = Flask(__name__, instance_relative_config=True)

    if os.getenv('FLASK_ENV') == 'development':
        config_class = DevelopmentConfig()
    elif os.getenv('FLASK_ENV') == 'DigitalocenDEV':
        config_class = DigitalocenDEV()
    elif os.getenv('FLASK_ENV') == 'production':
        config_class = ProductionConfig()
    elif os.getenv('FLASK_ENV') == 'testing':
        config_class = TestConfig()

    app.config.from_object(config_class)
    app.url_map.strict_slashes = False
    app.jinja_env.globals.update(zip=zip)
    migrate = Migrate(app, db)




    manager = Manager(app)
    manager.add_command('db', MigrateCommand)



    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # check if the config table exists, otherwise run install
       
        engine = db.get_engine(app)
        if not engine.dialect.has_table(engine, 'app_config'):
            return run_install(app)
        else:
            from fellowcrm.settings.models import AppConfig
            row = AppConfig.query.first()
            if not row:
                return run_install(app)
    
        # application is installed so extends the config
        from fellowcrm.settings.models import AppConfig, Currency, TimeZone
        app_cfg = AppConfig.query.first()
        app.config['def_currency'] = Currency.get_currency_by_id(app_cfg.default_currency)
        app.config['def_tz'] = TimeZone.get_tz_by_id(app_cfg.default_timezone)

        # include the routes
        # from fellowcrm import routes
        from fellowcrm.main.routes import main
        from fellowcrm.users.routes import users
        from fellowcrm.leads.routes import leads
        from fellowcrm.accounts.routes import accounts
        from fellowcrm.contacts.routes import contacts
        from fellowcrm.deals.routes import deals
        from fellowcrm.settings.routes import settings
        from fellowcrm.settings.app_routes import app_config
        from fellowcrm.reports.routes import reports
        from fellowcrm.picklists.routes import picklists
        from fellowcrm.upgrade.routes import upgrade

        # register routes with blueprint
        app.register_blueprint(main)
        app.register_blueprint(users)
        app.register_blueprint(settings)
        app.register_blueprint(app_config)
        app.register_blueprint(leads)
        app.register_blueprint(accounts)
        app.register_blueprint(contacts)
        app.register_blueprint(deals)
        app.register_blueprint(reports)
        app.register_blueprint(picklists)
        app.register_blueprint(upgrade)
        return app


