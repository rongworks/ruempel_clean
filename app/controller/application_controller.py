from flask import render_template


class ApplicationController:

    def __init__(self, request):
        pass

    def home(self):
        return render_template('base.html', title='Home')

    def not_found(self):
        return render_template('base.html', title='Home', error='GIBBES NICH!!'), 404