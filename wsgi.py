from app import url_resolver


def wsgi_handler(request, start_response):
    response = url_resolver.get_response(request)
    body = response.body.encode('utf-8')
    response.headers.append(('Content-Length', str(len(body))))
    response.headers.append(('Content-Type', 'text/html; charset=utf-8'))
    start_response(response.status, response.headers)
    return [body]