import pytest
from flask import Flask, request

from app.config.router import Router

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def base(path):
    return Router().process(request)

@pytest.fixture(scope='module')
def flask_app():
    with app as a:
        yield a
@pytest.fixture(scope='module')
def client():
    with app.test_client() as c:
        yield c