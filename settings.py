# -*- coding: utf-8 -*-
import os.path
import re

# Development server parameters
DEV_SERVER_HOST = 'localhost'
DEV_SERVER_PORT = 8051

# Sqlite database settings
DATABASE = {
    'SQLITE_FILE_PATH': 'feedback_app.db',
    'DUMP_FILE_PATH': os.path.join('sql', 'load_db.sql'),
}

# JavaScript folder
JS_PATH = os.path.join('.', 'js')

# Valid phone number format
PHONE_NUMBER_REGEX = re.compile('^\(\d+\)\d+$')

# Valid email format
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")