# -*- coding: utf-8 -*-
import unittest

import settings
import util
from urlconf import UrlResolver
from templates import HTMLGenerator
from database import FeedbackDatabase


class TestUtilities(unittest.TestCase):

    def test_quoted_list_normal_case(self):
        data = ['one', 2, 'three']
        quoted = util.to_quoted_list(data)
        self.assertEqual(quoted, "'one', '2', 'three'")

    def test_quoted_list_empty_list(self):
        data = []
        quoted = util.to_quoted_list(data)
        self.assertEqual(quoted, '')

    def test_quoted_list_custom_parameters(self):
        data = [4, 'five', 6]
        quoted = util.to_quoted_list(
            items=data,
            quotes='/',
            sep='_'
        )
        self.assertEqual(quoted, '/4/_/five/_/6/')


class TestUrlResolver(unittest.TestCase):

    def test_default_handler(self):
        url_resolver = UrlResolver()

        fake_request = {
            'PATH_INFO': '/fake/',
            'REQUEST_METHOD': 'GET',
        }

        fake_response = url_resolver.get_response(fake_request)
        default_response = url_resolver.get_default_handler()(fake_request)

        self.assertEqual(fake_response, default_response)

    def test_normal_urlconf(self):
        url_resolver = UrlResolver()

        @url_resolver.get('/user/(?P<id>\d+)')
        def user_getter(request, id):
            return UrlResolver.Response(
                status='200 OK',
                headers=[],
                body='details for user #%s' % (id),
            )

        response = url_resolver.get_response(
            request={
                'PATH_INFO':  '/user/42',
                'REQUEST_METHOD': 'GET',
            }
        )

        self.assertEqual(response.body, 'details for user #42')

    def test_urlconf_miss(self):
        url_resolver = UrlResolver()

        @url_resolver.get('/user/(?P<id>\d+)')
        def user_getter(request, id):
            return UrlResolver.Response(
                status='200 OK',
                headers=[],
                body='details for user #%s' % (id),
            )

        miss_response = url_resolver.get_response(
            request={
                'PATH_INFO': '/missing-path/42',
                'REQUEST_METHOD': 'GET',
            }
        )

        default_response = url_resolver.get_default_handler()(
            request={
                'PATH_INFO': '/fake/',
                'REQUEST_METHOD': 'GET',
            }
        )

        self.assertEqual(miss_response, default_response)


class TestDatabase(unittest.TestCase):

    def test_comment_creation(self):
        db = FeedbackDatabase(
            sqlite_file_path=':memory:',
            dump_file_path=settings.DATABASE['DUMP_FILE_PATH'],
        )
        db.add_comment(FeedbackDatabase.Comment(
            id=None,
            first_name=u'Иван',
            middle_name=u'Иванович',
            last_name=u'Иванов',
            region_id=1,
            city_id=1,
            phone_number=u'(861)2334455',
            email=u'ivan@ivanov.com',
            feedback_text=u'Тестовый отзыв',
        ))
        self.assertEqual(db.get_comments_count(), 1)
        db.add_comment(FeedbackDatabase.Comment(
            id=None,
            first_name=u'Пётр',
            middle_name=u'Петрович',
            last_name=u'Петров',
            region_id=1,
            city_id=2,
            phone_number=u'(861)2998877',
            email=u'petr@petrov.com',
            feedback_text=u'Другой тестовый отзыв',
        ))
        self.assertEqual(db.get_comments_count(), 2)

        select_cursor = db._backend.select('comment', ['last_name'])
        last_names = sorted(last_name for (last_name,) in select_cursor)
        required_list = sorted([u'Иванов', u'Петров'])
        self.assertEqual(last_names, required_list)


class TestHTMLGenerator(unittest.TestCase):

    def test_partial_html_paragraphs(self):
        gen = HTMLGenerator()
        gen.p('Paragraph 1')
        gen.p('Paragraph 2')
        partial_html = str(gen)
        required_html = '<p>Paragraph 1</p>\n<p>Paragraph 2</p>\n'
        self.assertEqual(partial_html, required_html)

    def test_partial_html_links(self):
        gen = HTMLGenerator()
        gen.a('Text 1', 'www.link1.com')
        gen.a('Text 2', 'www.link2.com')
        partial_html = str(gen)
        required_html = '<a href="www.link1.com">Text 1</a>\n' \
            '<a href="www.link2.com">Text 2</a>\n'
        self.assertEqual(partial_html, required_html)

    def test_partial_html_mixed_tags(self):
        gen = HTMLGenerator()
        gen.h1('Page title')
        gen.p('Paragraph 1')
        gen.a('Link 1', 'www.link1.com')
        gen.p('Paragraph 2')
        gen.a('Link 2', 'www.link2.com')
        partial_html = str(gen)
        required_html = '<h1>Page title</h1>\n' \
            '<p>Paragraph 1</p>\n' \
            '<a href="www.link1.com">Link 1</a>\n' \
            '<p>Paragraph 2</p>\n' \
            '<a href="www.link2.com">Link 2</a>\n'
        self.assertEqual(partial_html, required_html)

    def test_full_html_page(self):
        gen = HTMLGenerator()
        gen.h1('Page title')
        gen.p('Paragraph 1')
        gen.a('Link 1', 'www.link1.com')
        gen.p('Paragraph 2')
        gen.a('Link 2', 'www.link2.com')
        full_html = gen.get_full_html()
        required_html = '<html><head></head><body>' \
                        '<h1>Page title</h1>\n' \
                        '<p>Paragraph 1</p>\n' \
                        '<a href="www.link1.com">Link 1</a>\n' \
                        '<p>Paragraph 2</p>\n' \
                        '<a href="www.link2.com">Link 2</a>\n' \
                        '</body></html>'
        self.assertEqual(full_html, required_html)

    def test_list_tags(self):
        pass

    def test_form_tag(self):
        pass


if __name__ == '__main__':
    unittest.main()
