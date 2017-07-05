# -*- coding: utf-8 -*-
import os.path

# Development server parameters
DEV_SERVER_HOST = 'localhost'
DEV_SERVER_PORT = 8051

# Sqlite database settings
DATABASE = {
    'SQLITE_FILE_PATH': 'feedback_app.db',
    'DUMP_FILE_PATH': os.path.join('sql', 'load_db.sql'),
}
