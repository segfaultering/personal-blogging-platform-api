from datetime import date

import psycopg

from models import ArticleResponse

type Row = tuple[int, str, str | None, datetime.date]

def get_db_conn() -> pyscopg.Connection:
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
        pulish_date=publish_date
    )


