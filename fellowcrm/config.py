from .config_vars import *


class Config(object):
    DEBUG = False
    TESTING = False
    RBAC_USE_WHITE = True
    PYTHON_VER_MIN_REQUIRED = '3.5.0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['en', 'de']


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = DEV_SECRET_KEY

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DEV_DB_USER}:{DEV_DB_PASS}@{DEV_DB_HOST}/{DEV_DB_NAME}'

class DigitalocenDEV(Config):
    DEV_DB_USER = "crm_dev"
    DEV_DB_USER = "g1tzcq3vwm9kyu1f"
    TESTING = True
    SECRET_KEY = 'your_secret_key'
    DEV_DB_PASS = "db-postgresql-fra1-28416-do-user-1010676-0.b.db.ondigitalocean.com"
    port = 25061
    DEV_DB_NAME = "crm_dev"
    sslmode = "require"
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://crm_dev:g1tzcq3vwm9kyu1f@db-postgresql-fra1-28416-do-user-1010676-0.b.db.ondigitalocean.com:25061/crm_dev?sslmode=require'

class TestConfig(Config):
    TESTING = True
    SECRET_KEY = TEST_SECRET_KEY
    SQLALCHEMY_DATABASE_URI = f'postgresql://{TEST_DB_USER}:{TEST_DB_PASS}@{TEST_DB_HOST}/{TEST_DB_NAME}'


class ProductionConfig(Config):
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'





