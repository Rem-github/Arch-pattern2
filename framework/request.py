class Request:

    def __init__(self, environ):
        self.method = environ.get('REQUEST_METHOD').lower()
        self.path = environ.get('PATH_INFO')
        self.querystring = self._get_query_string(environ)
        self.headers = self._get_headers(environ)
        self.data = self._parse_input_data(self._get_wsgi_input_data(environ))


    def _get_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers

    def _get_query_string(self, environ):
        query_strings = {}
        qs = environ.get('QUERY_STRING')
        if qs:
            ql = qs.split('&')
            for el in ql:
                key, value = el.split('=')
                if key not in query_strings:
                    query_strings[key] = list(value)
                else:
                    query_strings[key].append(value)
        return query_strings


    def _get_wsgi_input_data(self, environ) -> str:
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data.decode(encoding='utf-8')


    def _parse_input_data(self, wsgi_data):
        result = {}
        if wsgi_data:
            params = wsgi_data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result
