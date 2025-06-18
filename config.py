import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'UIDE123!'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:donato123@localhost/novahealth_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
