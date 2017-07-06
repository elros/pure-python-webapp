# -*- coding: utf-8 -*-
import json
from urlparse import parse_qs
import cgi

from urlconf.url_resolver import UrlResolver


def to_quoted_list(items, quotes='\'', sep=', '):
    quoted = lambda s: quotes + str(s) + quotes
    return sep.join(quoted(item) for item in items)


def html_success_response(data):
    return UrlResolver.Response(
        status='200 OK',
        headers=[
            ('Content-Type', 'text/html; charset=utf-8'),
        ],
        body=unicode(data),
    )


def http_404_response():
    return UrlResolver.Response(
        status='404 Not Found',
        headers=[
            ('Content-Type', 'text/html; charset=utf-8'),
        ],
        body=u'Запрашиваемая страница не найдена.',
    )


def http_redirect_response(url):
    return UrlResolver.Response(
        status='302 Found',
        headers=[
            ('Location', url),
        ],
        body='',
    )


def json_success_response(data):
    return UrlResolver.Response(
        status='200 OK',
        headers=[
            ('Content-Type', 'text/json; charset=utf-8'),
        ],
        body=json.dumps({
            'success': True,
            'data': data,
        }, ensure_ascii=False)
    )


def extract_post_data(request):
    try:
        request_body_size = int(request.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0

    request_body = request['wsgi.input'].read(request_body_size)
    return parse_qs(request_body)


def escape(posted_data):
    return cgi.escape(posted_data)


def escape_variable(posted_data, var_name):
    if var_name in posted_data:
        return escape(posted_data[var_name][0]).decode('utf-8')
    else:
        return None