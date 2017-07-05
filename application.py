# -*- coding: utf-8 -*-
import database
import settings
from templates.feedback_site import FeedbackSiteGenerator
from urlconf.url_resolver import UrlResolver

db = database.FeedbackDatabase(
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


