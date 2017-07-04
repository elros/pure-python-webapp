# -*- coding: utf-8 -*-
import unittest

import util
from url_resolver import UrlResolver


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

    pass


if __name__ == '__main__':
    unittest.main()
