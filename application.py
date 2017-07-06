# -*- coding: utf-8 -*-
import settings
import util
from database.feedback_db import FeedbackDatabase
from templates.feedback_site import FeedbackSiteGenerator
from urlconf.url_resolver import UrlResolver


db = FeedbackDatabase(
    sqlite_file_path=settings.DATABASE['SQLITE_FILE_PATH'],
    dump_file_path=settings.DATABASE['DUMP_FILE_PATH'],
)

url_resolver = UrlResolver()

site_generator = FeedbackSiteGenerator(db)


@url_resolver.get('/comment/')
def comment_form_view(request):
    return util.html_success_response(
        data=site_generator.get_comment_form_page(),
    )


@url_resolver.post('/comment/')
def create_comment(request):
    return util.html_success_response('')


@url_resolver.get('/view/')
def comments_list_view(request):
    return util.html_success_response(
        data=site_generator.get_comments_list_page(),
    )


@url_resolver.get('/region/(?P<region_id>\d+)/cities/')
def region_cities_list(request, region_id):
    return util.json_success_response(
        data={
            'cities': [city._asdict() for city in db.get_cities_by_region(region_id)]
        }
    )


def wsgi_handler(request, start_response):
    response = url_resolver.get_response(request)
    body = response.body.encode('utf-8')
    response.headers.append(('Content-Length', str(len(body))))
    response.headers.append(('Content-Type', 'text/html; charset=utf-8'))
    start_response(response.status, response.headers)
    return [body]
