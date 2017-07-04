# -*- coding: utf-8 -*-
import sqlite3
import os.path
from collections import namedtuple

import util


class FeedbackDatabase:

    Comment = namedtuple('Comment', ['id', 'first_name', 'middle_name',
        'last_name', 'region_id', 'city_id', 'phone_number', 'email'])
    Region = namedtuple('Region', ['id', 'name'])
    City = namedtuple('City', ['id', 'name', 'region_id'])

    def __init__(self, sqlite_file_path, dump_file_path):
        self._backend = SqliteBackend()
        self._backend.open_db_or_load_dump(sqlite_file_path, dump_file_path)

    def add_comment(self, comment):
        pass

    def get_regions_list(self):
        pass

    def get_cities_by_region(self, region_id):
        pass


class SqliteBackend:

    def __init__(self, db_file_path):
        self._connection = None

    def __del__(self):
        if self._connection:
            self._connection.close()

    def connect(self, db_file_path):
        self._connection = sqlite3.connect(db_file_path)

    def open_db_or_load_dump(self, sqlite_file_path, dump_file_path):
        db_existed_before_connection = os.path.isfile(sqlite_file_path)
        self.connect(sqlite_file_path)
        if not db_existed_before_connection:
            self._backend.load_dump(dump_file_path)

    def insert(self, table_name, fields_values):
        self._connection.execute('''
                INSERT INTO {table_name}({fields})
                VALUES ({values})
            '''.format(
                table_name=table_name,
                fields=util.to_quoted_list(fields_values),
                values=util.to_quoted_list(fields_values),
            )
        )

    def select(self, table_name, fields_list):
        return self._connection.execute('''
                SELECT {fields}
                FROM {table_name}
            '''.format(
                fields=util.to_quoted_list(fields_list, quotes='"'),
                table_name=table_name,
            )
        )

    def select_with_eq_filter(self, table_name, fields_list):
        return self._connection.execute('''
                SELECT {fields}
                FROM {table_name}
                WHERE {filter_field} = {filter_value}
            '''.format(
                fields=util.to_quoted_list(fields_list, quotes='"'),
                table_name=table_name,
            )
        )

    def load_dump(dump_file_path):
        dump = open(dump_file_path, 'rt').read()
        self._connection.executescript(dump)
