import os.path
import sqlite3

import util


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
            values=', '.join(['?'] * len(fields)),
        )
        self._connection.execute(sql, fields.values())
        self._connection.commit()

    def select_with_eq_filter(self, table_name, fields_list, filter_field, filter_value):
        sql_template = '''
            SELECT {fields}
            FROM {table_name}
            WHERE {filter_field} = ?
        '''
        sql = sql_template.format(
            fields=util.to_quoted_list(fields_list, quotes='"'),
            table_name=table_name,
            filter_field=filter_field,
        )
        print sql
        return self._connection.execute(sql, filter_value)

    def load_dump(self, dump_file_path):
        dump = open(dump_file_path, 'rt').read()
        self._connection.executescript(dump)