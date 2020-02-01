from flask import render_template


class ApplicationController:

    def __init__(self, request):
        self.params = request.args
        self.pages_set = ['test']
        self.layout = "base"

    def home(self):
        return render_template('pages/home.html', title='Home', layout=self.layout)

    def pages(self):
        page_slug = self.params['slug']
        if self.__is_valid_page(page_slug) :
            return render_template('pages/' + page_slug + '.html', layout=self.layout)
        else:
            return self.not_found()


    def not_found(self):
        return render_template('base.html', title='Home', error='GIBBES NICH!!'), 404

    def __is_valid_page(self, slug):
        return slug in self.pages_set