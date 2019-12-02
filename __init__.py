from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def base():
    return render_template('base.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)
