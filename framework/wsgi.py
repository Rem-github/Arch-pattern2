from framework.request import Request
from framework.view import View, notFound404



class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        start_response(response.status, list(response.headers.items()))
        return [response.body.encode('utf-8')] if response.body else [response.body]

    def _get_view(self, request: Request):
        path = request.path
        for url in self.urls:
            if '/' + url.path == path:
                return url.view

    def _get_response(self, request: Request, view: View):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        else:
            return notFound404()
