from datetime import date

import psycopg

from src.api.models import ArticleResponse

type Row = tuple[int, str, str | None, date] | None

def get_db_conn() -> psycopg.Connection:
    conn = psycopg.connect("dbname=blogging user=mohsin", autocommit=True)
    try:
        yield conn
    
    finally:
        conn.close()

def sql_to_pydantic(row: Row) -> ArticleResponse:
    article_id, title, content, publish_date = row
    return ArticleResponse(
        article_id=article_id,
        title=title,
        content=content,
        publish_date=publish_date
    )


