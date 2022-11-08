from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv #load dotenv(.env file) into environmental variables
import os # allow us to access enviromental variables

# set up database
db = SQLAlchemy()
migrate = Migrate() 
load_dotenv()


def create_app(testing=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # DB config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        #grab the connection string from envrionmental variables
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')

    # connecting our db to app and migrate 
    db.init_app(app)
    migrate.init_app(app, db)

    # import model Breakfast
    from app.models.breakfast import Breakfast
    from app.models.menu import Menu


    # register blueprint
    from .routes.breakfast import breakfast_bp
    app.register_blueprint(breakfast_bp)

    from.routes.menu import menu_bp
    app.register_blueprint(menu_bp)

    return app