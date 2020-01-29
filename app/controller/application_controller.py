from flask import render_template


class ApplicationController:

    def __init__(self, request):
        self.params = request.args

    def home(self):
        return render_template('base.html', title='Home')

    def pages(self):
        page_slug = self.params['slug']
        if page_slug:
            return render_template('pages/'+page_slug+'.html')

    def not_found(self):
        return render_template('base.html', title='Home', error='GIBBES NICH!!'), 404