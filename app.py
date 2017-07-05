# -*- coding: utf-8 -*-
import settings
import database
from urlconf import UrlResolver


db = database.FeedbackDatabase(
    sqlite_file_path=settings.DATABASE['SQLITE_FILE_PATH'],
    dump_file_path=settings.DATABASE['DUMP_FILE_PATH'],
)

url_resolver = UrlResolver()


@url_resolver.get('/comments/')
def comments_list_view(request):
    return UrlResolver.Response(
        status='200 OK',
        headers=[],
        body='Dummy comments list view'
    )


def wsgi_handler(request, start_response):
    response = url_resolver.get_response(request)
    response.headers.append(('Content-Length', str(len(response.body))))
    start_response(response.status, response.headers)
    return [response.body]
