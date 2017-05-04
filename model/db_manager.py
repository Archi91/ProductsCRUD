import sqlite3
from os.path import isfile


class DbManager:

    @classmethod
    def execute_query(cls, query, values_tuple=None, commit=True, fetchone=False):
        if not isfile('database.db'):
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            script = open('database.sql', 'r').read()
            cur.execute(script)
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        if values_tuple:
            cur.execute(query, values_tuple)
        else:
            cur.execute(query)
        if commit:
            conn.commit()
        if fetchone:
            return cur.fetchone()
        return cur.fetchall()



