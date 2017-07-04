# -*- coding: utf-8 -*-
import settings
import database
from url_resolver import UrlResolver


db = database.FeedbackDatabase(
    sqlite_file_path=settings.DATABASE['SQLITE_FILE_PATH'],
    dump_file_path=settings.DATABASE['DUMP_FILE_PATH'],
)

url_resolver = UrlResolver()


def wsgi_handler(request, start_response):
    response = url_resolver.get_response(request)
    response.headers.append(('Content-Length', str(len(response.body))))
    start_response(response.status, response.headers)
    return [response.body]
