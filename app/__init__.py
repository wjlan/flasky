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

    # connecting our db to app and migrate we created in line 6-7
    db.init_app(app)
    migrate.init_app(app, db)

    # import model Breakfast
    from app.models.breakfast import Breakfast

    # register blueprint
    from .routes.breakfast import breakfast_bp
    app.register_blueprint(breakfast_bp)

    return app