from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from app.config.router import Router

app = Flask(__name__)
Bootstrap(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def base(path):
    return Router().process(request)

