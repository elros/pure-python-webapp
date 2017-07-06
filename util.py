# -*- coding: utf-8 -*-
import json

from urlconf.url_resolver import UrlResolver


def to_quoted_list(items, quotes='\'', sep=', '):
    quoted = lambda s: quotes + str(s) + quotes
    return sep.join(quoted(item) for item in items)


def html_success_response(data):
    return UrlResolver.Response(
        status='200 OK',
        headers=[
            ('Content-Type', 'text/html; charset=utf-8')
        ],
        body=unicode(data),
    )


def get_http404_response():
    return UrlResolver.Response(
        status='404 Not Found',
        headers=[
            ('Content-Type', 'text/html; charset=utf-8')
        ],
        body=u'Запрашиваемая страница не найдена.',
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