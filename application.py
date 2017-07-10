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
    return util.http_success_response(
        data=site_generator.get_comment_form_page(),
    )


@url_resolver.post('/comment/')
def create_comment(request):
    # Extract posted data
    data = util.extract_post_data(request)
    comment = FeedbackDatabase.Comment(
        id=None,
        first_name=util.escape_variable(data, 'first_name'),
        middle_name=util.escape_variable(data, 'middle_name'),
        last_name=util.escape_variable(data, 'last_name'),
        region_id=util.escape_variable(data, 'region_id'),
        city_id=util.escape_variable(data, 'city_id'),
        phone_number=util.escape_variable(data, 'phone_number'),
        email=util.escape_variable(data, 'email'),
        feedback_text=util.escape_variable(data, 'feedback_text'),
    )

    # Check that comment is valid
    if not all([comment.first_name, comment.last_name, comment.feedback_text]):
        return util.http_bad_request_response()
    if comment.city_id:
        if int(comment.city_id) not in [city.id for city in db.get_cities_by_region(comment.region_id)]:
            return util.http_bad_request_response()
    if comment.phone_number:
        if not settings.PHONE_NUMBER_REGEX.match(comment.phone_number):
            return util.http_bad_request_response()
    if comment.email:
        if not settings.EMAIL_REGEX(comment.email):
            return util.http_bad_request_response()

    # Create a comment object and return successful response
    db.create_comment(comment)
    return util.http_redirect_response('/comment/thanks/')


@url_resolver.post('/comment/(?P<comment_id>\d+)/delete/')
def delete_comment(request, comment_id):
    db.delete_comment(comment_id)
    return util.http_redirect_response('/view/')


@url_resolver.get('/comment/thanks/')
def comment_thanks_page(request):
    return util.http_success_response(
        data=site_generator.get_thanks_page(),
    )


@url_resolver.get('/view/')
def comments_list_view(request):
    return util.http_success_response(
        data=site_generator.get_comments_list_page(),
    )


@url_resolver.get('/region/(?P<region_id>\d+)/cities/')
def region_cities_list(request, region_id):
    return util.json_success_response(
        data={
            'cities': [city._asdict() for city in db.get_cities_by_region(region_id)]
        }
    )


@url_resolver.get('/stat/')
def regions_summary_statistics(request):
    return util.http_success_response(
        data=site_generator.get_regions_statistics_summary_page(),
    )


@url_resolver.get('/stat/region/(?P<region_id>\d+)/')
def region_detailed_statistics(request, region_id):
    return util.http_success_response(
        data=site_generator.get_region_detailed_statistics_page(region_id),
    )


def wsgi_handler(request, start_response):
    response = url_resolver.get_response(request)
    body = response.body.encode('utf-8')
    response.headers.append(('Content-Length', str(len(body))))
    response.headers.append(('Content-Type', 'text/html; charset=utf-8'))
    start_response(response.status, response.headers)
    return [body]
