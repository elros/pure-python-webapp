# -*- coding: utf-8 -*-
from collections import namedtuple

from database.sqlite_backend import SQLiteBackend


class FeedbackDatabase:

    Comment = namedtuple('Comment', ['id', 'first_name', 'middle_name',
        'last_name', 'region_id', 'city_id', 'phone_number', 'email', 'feedback_text'])
    Region = namedtuple('Region', ['id', 'name'])
    City = namedtuple('City', ['id', 'name', 'region_id'])

    def __init__(self, sqlite_file_path, dump_file_path):
        self._backend = SQLiteBackend()
        self._backend.open_db_or_load_dump(sqlite_file_path, dump_file_path)

    def add_comment(self, comment):
        self._backend.insert(
            table_name='comment',
            fields=comment._asdict(),
        )

    def get_comments_count(self):
        cursor = self._backend.select(
            table_name='comment',
            fields=['id']
        )
        return len(list(cursor))

    def get_regions_list(self):
        return self._backend.select(
            table_name='region',
            fields=['name'],
        )

    def get_cities_by_region(self, region_id):
        # TODO
        pass


