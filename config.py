import os
# import pymysql

class Config:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    ERROR_404_HELP = False

    OPBEAT = {
        'ORGANIZATION_ID': os.getenv('OPBEAT_ORG_ID'),
        'APP_ID': os.getenv('OPBEAT_APP_ID'),
        'SECRET_TOKEN': os.getenv('OPBEAT_SECRET_TOKEN'),
        'INCLUDE_PATHS': ['demo']
    }


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    # DB URL variable set by heroku
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/githubDoc?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/githubDoc?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
