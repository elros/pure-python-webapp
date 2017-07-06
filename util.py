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