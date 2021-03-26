from flask import Blueprint
from flask import Flask

bp = Blueprint('api', __name__, url_prefix='/api')

from .import views