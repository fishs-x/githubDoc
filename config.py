import os


# import pymysql

class Config:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = "587"
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    MAIL_RECIPIENTS = os.getenv('MailRecipients').split(',')
    ERROR_404_HELP = False


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', '')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/githubDoc?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
