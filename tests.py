# -*- coding: utf-8 -*-
import unittest

import util


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

    def test_normal_urlconf(self):
        pass

    def test_default_handler(self):
        pass

    def test_urlconf_miss(self):
        pass


class TestDatabase(unittest.TestCase):

    pass


if __name__ == '__main__':
    unittest.main()
