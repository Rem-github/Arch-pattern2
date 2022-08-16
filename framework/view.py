from framework.response import Response


class View:

    def get(self, request, *args, **kwargs) -> Response:
        pass

    def post(self, request, *args, **kwargs) -> Response:
        pass



def notFound404():

    return '404 WHAT', '404 PAGE Not Found', [('Content-Type', 'text/html')]
