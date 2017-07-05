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
        self._backend = SQLiteBackend()
        self._backend.open_db_or_load_dump(sqlite_file_path, dump_file_path)

    def add_comment(self, comment):
        # TODO
        pass

    def get_regions_list(self):
        # TODO
        pass

    def get_cities_by_region(self, region_id):
        # TODO
        pass


class SQLiteBackend:

    def __init__(self):
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
            self.load_dump(dump_file_path)

    def select(self, table_name, fields):
        sql_template = '''
            SELECT {fields}
            FROM {table_name}
        '''
        sql = sql_template.format(
            fields=util.to_quoted_list(fields, quotes='"'),
            table_name=table_name,
        )
        return self._connection.execute(sql)

    def insert(self, table_name, fields):
        sql_template = '''
            INSERT INTO {table_name}({fields})
            VALUES ({values})
        '''
        sql = sql_template.format(
            table_name=table_name,
            fields=util.to_quoted_list(fields.keys()),
            values=util.to_quoted_list(fields.values()),
        )
        return self._connection.execute(sql)

    def select_with_eq_filter(self, table_name, fields_list, filter_field, filter_value):
        return self._connection.execute('''
                SELECT {fields}
                FROM {table_name}
                WHERE {filter_field} = {filter_value}
            '''.format(
                fields=util.to_quoted_list(fields_list, quotes='"'),
                table_name=table_name,
                filter_field=filter_field,
                filter_value=filter_value,
            )
        )

    def load_dump(self, dump_file_path):
        dump = open(dump_file_path, 'rt').read()
        self._connection.executescript(dump)
