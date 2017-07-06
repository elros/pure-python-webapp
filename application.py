# -*- coding: utf-8 -*-
import settings
from database.feedback_db import FeedbackDatabase
from templates.feedback_site import FeedbackSiteGenerator
from urlconf.url_resolver import UrlResolver


db = FeedbackDatabase(
    sqlite_file_path=settings.DATABASE['SQLITE_FILE_PATH'],
    dump_file_path=settings.DATABASE['DUMP_FILE_PATH'],
)

url_resolver = UrlResolver()

site_generator = FeedbackSiteGenerator()


@url_resolver.get('/comment/')
def comments_list_view(request):
    return UrlResolver.Response(
        status='200 OK',
        headers=[],
        body=site_generator.get_comment_page(),
    )


def wsgi_handler(request, start_response):
    response = url_resolver.get_response(request)
    body = response.body.encode('utf-8')
    response.headers.append(('Content-Length', str(len(body))))
    response.headers.append(('Content-Type', 'text/html; charset=utf-8'))
    start_response(response.status, response.headers)
    return [body]