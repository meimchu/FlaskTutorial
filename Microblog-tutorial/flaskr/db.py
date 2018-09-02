import sqlite3
import os
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def init_db_command():
    print 'Initialized the database.'
    root_path = os.path.split(__file__)[0]
    db_path = os.path.join(root_path, 'instance/flaskr.sqlite')
    db = sqlite3.connect(db_path)

    if not os.path.exists(db_path):
        cursor = db.cursor()

        schema_path = os.path.join(root_path, 'schema.sql')

        sq_list = []
        sq_command = ''
        with open(schema_path, 'r') as f:
            for line in f:
                if line.endswith(';\n') or line.endswith(';'):
                    sq_command += line
                    sq_command = sq_command.replace('\n', '')
                    sq_list.append(sq_command)
                    sq_command = ''

                else:
                    sq_command += line

        for i in sq_list:
            cursor.execute(i)