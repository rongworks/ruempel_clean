from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return app.send_static_file('startbootstrap_landingpage/index.html')


if __name__ == '__main__':
    app.run()
