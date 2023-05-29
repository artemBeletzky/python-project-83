import os
import psycopg2


class Postgres:
    def __init__(self):
        self._connection = None

    def connect(self):
        self._connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_USER_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
        print("DB connection is established.")

    def close_conn(self, exception):
        if exception:
            raise exception
        if self._connection is not None:
            print("Closing DB connection.")
            self._connection.close()
        else:
            print("Nothing to close. There's no DB connection.")

    def fetch_data(self, query, params=None, fetchall=False):
        with self._connection.cursor() as cur:
            cur.execute(query, params)
            if fetchall:
                return cur.fetchall()
            else:
                return cur.fetchone()

    def execute_modifying_query(self, query, params=None):
        with self._connection.cursor() as cur:
            cur.execute("BEGIN;")
            cur.execute(query, params)
            self._connection.commit()
