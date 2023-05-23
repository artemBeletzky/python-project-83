import os

import psycopg2
from dotenv import load_dotenv
from flask import g

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_USER_PASSWORD = os.getenv("DB_USER_PASSWORD")


class Database:
    def __init__(self):
        self.db_name = DB_NAME
        self.db_user = DB_USER
        self.db_user_password = DB_USER_PASSWORD
        self.db_host = DB_HOST
        self.db_port = DB_PORT

    def get_connection(self):
        if "db" not in g:
            try:
                g.db = psycopg2.connect(
                    dbname=self.db_name,
                    user=self.db_user,
                    password=self.db_user_password,
                    host=self.db_host,
                    port=self.db_port,
                )
            except Exception as e:
                # TODO add logging
                raise e
            finally:
                if "db" not in g:
                    g.db.close()
        return g.db

    @staticmethod
    def teardown_db():
        db = g.pop("db", None)
        if db is not None:
            db.close()
