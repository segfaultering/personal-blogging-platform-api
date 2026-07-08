from datetime import datetime

import psycopg

from models import ArticleRequest, ArticleResponse


type Row = tuple[int, str, str, datetime]


def return_notes(conn: psycopg.Connection) -> list[ArticleResponse]:
    "Return all notes in the db."
    query = "SELECT * FROM article;" 

    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute(query)
            rows = cur.fetchall()

    return [__sql_to_pydantic(row) for row in rows]


def return_note(conn: psycopg.Connection,
                article: GET_ArticleRequest) -> ArticleResponse:
    "Returns a singular article from its id"
    query = """
        SELECT * FROM article 
        WHERE id = %s;
    """
    values = article.article_id  

    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute(query, values)
    
    return __sql_to_pydantic(cur.fetchone())


def create_note(conn: psycopg.Connection,
                article: POST_ArticleRequest) -> ArticleResponse:

    create_query = """
        INSERT INTO article (title, content, date)
        VALUES (%s, %s);
    """
    retrieve_query = 
    values = (article.title, article.content)

    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute(query, values)



def __sql_to_pydantic(row: Row) -> ArticleResponse:  
    "Converts SQL row for an article to Pydantic."
    article_id, title, content, publish_date = row
    return ArticleResponse(
        article_id=article_id,
        title=title,
        content=content,
        publish_date=publish_date
    )




