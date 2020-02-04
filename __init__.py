from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from app.config.router import Router

app = Flask(__name__)
#app.config.from_envvar('FLASK_ENV')
Bootstrap(app)
mail = Mail(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def base(path):
    return Router().process(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0')