from flask import Blueprint

bp = Blueprint('billboard', __name__, url_prefix='/billboard')

from app.blueprints.billboard import views, models