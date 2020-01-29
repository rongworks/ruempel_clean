from app.controller.application_controller import ApplicationController


class Router:
    def process(self, request):
        if(request.path == '/'):
            return ApplicationController(request).home()
        else:
            return ApplicationController(request).not_found()