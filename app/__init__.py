from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_moment import Moment
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'You do not have access to this page. Login in first please!'
login_manager.login_message_category = 'warning'

def create_app(config_class=Config): 
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    login_manager.init_app(app)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.billboard import bp as billboard_bp
    app.register_blueprint(billboard_bp)

    from app.blueprints.blog import bp as blog_bp
    app.register_blueprint(blog_bp)

    from app.blueprints.shop import bp as shop_bp
    app.register_blueprint(shop_bp)
    
    from app.blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    # Needs app context
    with app.app_context():
        # from app import views
        from .import context_processors

    from app import views

    return app