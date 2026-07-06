import psycopg

import blogging_api.config as config


def startup():
    config.CONN = __return_conn()
    __create_schema(config.CONN)

def __return_conn() -> psycopg.Connection:
    return psycopg.connect("dbname=blogging_api user=postgres", autocommit=True)

def __create_schema(conn):
    """Initializes the schema for the database."""
    with conn.transaction():
        conn.execute("""
            CREATE TABLE IF NOT EXISTS article (
                id SERIAL PRIMARY KEY,
                title TEXT UNIQUE NOT NULL,
                content TEXT,
                publish_date DATE NOT NULL
            );
        """)






