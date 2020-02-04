import pytest
from flask import Flask, request
from flask_mail import Mail

from app.config.router import Router

app = Flask(__name__)
mail = Mail(app)
app.testing = True

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def base(path):
    return Router().process(request)

@pytest.fixture(scope='module')
def flask_app():
    return app
@pytest.fixture(scope='module')
def client():
    with app.test_client() as c:
        yield c