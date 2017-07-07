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

    def get_comments_list(self):
        cursor = self._backend.select(
            table_name='comment',
            fields=FeedbackDatabase.Comment._fields,
        )
        for comment_fields in cursor:
            yield FeedbackDatabase.Comment(*comment_fields)

    def get_regions_list(self):
        cursor = self._backend.select(
            table_name='region',
            fields=FeedbackDatabase.Region._fields,
        )
        for region_fields in cursor:
            yield FeedbackDatabase.Region(*region_fields)

    def get_cities_by_region(self, region_id):
        cursor = self._backend.select_with_eq_filter(
            table_name='city',
            fields_list=FeedbackDatabase.City._fields,
            filter_field='region_id',
            filter_value=region_id,
        )
        for city_fields in cursor:
            print city_fields
            yield FeedbackDatabase.City(*city_fields)

    def get_region_name(self, region_id):
        if region_id is None:
            return None
        cursor = self._backend.select_with_eq_filter(
            table_name='region',
            fields_list=['name'],
            filter_field='id',
            filter_value=int(region_id),
        )
        data = cursor.fetchone()
        if data:
            return data[0]
        else:
            return None

    def get_city_name(self, city_id):
        if city_id is None:
            return None
        cursor = self._backend.select_with_eq_filter(
            table_name='region',
            fields_list=['name'],
            filter_field='id',
            filter_value=int(city_id),
        )
        data = cursor.fetchone()
        if data:
            return data[0]
        else:
            return None