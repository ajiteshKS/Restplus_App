import pytest
import repackage
repackage.up()
# from mypackage.mymodule import myfunction
from app import create_app,db


@pytest.yield_fixture(scope='session')
def flask_app():
    app = create_app('test')
    with app.app_context():
        yield app
        # db.drop_all()
        # db.session.rollback()

@pytest.fixture(scope='session')
def flask_app_client(flask_app):
    # flask_app.response_class = utils.JSONResponse
    return flask_app.test_client()




