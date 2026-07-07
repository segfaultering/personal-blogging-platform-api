import psycopg
from fastapi import FastAPI

import blogging_api.config as config


def startup():
    """Initializes the project environment"""
    config.CONN = __return_conn()
    __create_schema(config.CONN)
    config.APP = FastAPI()


def __return_conn() -> psycopg.Connection:
    return psycopg.connect("dbname=blogging user=mohsin", autocommit=True)

def __create_schema(conn):
    """Initializes the schema for the database."""
    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute("""
                CREATE TABLE IF NOT EXISTS article (
                    id SERIAL PRIMARY KEY,
                    title TEXT UNIQUE NOT NULL,
                    content TEXT,
                    publish_date DATE NOT NULL
                );
        """)






