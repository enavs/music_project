import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')
    STRIPE_PK_TEST=os.getenv('STRIPE_PK_TEST')
    STRIPE_TEST_KEY=os.getenv('STRIPE_TEST_KEY')