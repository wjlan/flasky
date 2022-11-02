import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.breakfast import Breakfast

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    # with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
    # convention --flask.test_client() 

@pytest.fixture
def two_breakfasts(app):
    breakfast1 = Breakfast(name="french toast", prep_time=15, rating=3.0)
    breakfast2 = Breakfast(name="oatmeal", prep_time=5, rating=2.0)
        
    db.session.add(breakfast1)
    db.session.add(breakfast2)
    db.session.commit()
