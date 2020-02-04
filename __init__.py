from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from app.config.router import Router

app = Flask(__name__)
Bootstrap(app)
mail = Mail(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def base(path):
    return Router().process(request)

