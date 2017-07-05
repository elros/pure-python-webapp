import re
from collections import namedtuple


class UrlResolver:

    Response = namedtuple('Response', ['status', 'headers', 'body'])
    UrlConfItem = namedtuple('UrlConfItem', ['method', 'regex', 'handler'])

    def __init__(self):
        self._urlconf = []

    def get_response(self, request):
        handler, args = self._get_matching_handler(
            url=request['PATH_INFO'],
            method=request['REQUEST_METHOD']
        )
        return handler(request, **args)

    def get(self, url_regex):
        return self._get_wrapper_for_http_method('GET', url_regex)

    def post(self, url_regex):
        return self._get_wrapper_for_http_method('POST', url_regex)

    def _get_matching_handler(self, url, method):
        for item in self._urlconf:
            match = item.regex.match(url)
            if match and item.method == method:
                return item.handler, match.groupdict()
        return self.get_default_handler(), {}

    def get_default_handler(self):
        return lambda request: UrlResolver.Response(
                status='404 Not Found',
                headers=[],
                body='Page not found.',
            )

    def _get_wrapper_for_http_method(self, http_method, url_regex):
        def wrapper(func):
            urlconf_item = UrlResolver.UrlConfItem(
                method=http_method,
                regex=re.compile('^' + url_regex + '$'),
                handler=func,
            )
            self._urlconf.append(urlconf_item)
            return func
        return wrapper