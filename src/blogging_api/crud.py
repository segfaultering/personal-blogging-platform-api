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
        VALUES (%s, %s, %s);
    """
    retrieve_query = """
        SELECT * FROM article
        WHERE title = %s;
    """
    insert_values = (article.title, article.content, datetime.date())
    retrieve_values = (article.title)

    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute(insert_query, insert_values)
            cur.execute(retrieve_query, retrieve_values)

            return __sql_to_pydantic(cur.fetchone())


def edit_article(conn: psycopg.Connection,
                 article: PUT_ArticleRequest) -> ArticleResponse: 
    put_query = """
        UPDATE article SET 
        title = %s AND content = %s WHERE
        id = %s;
    """
    retrieve_query = """
        SELECT * FROM article
        WHERE id = %s;
    """
    put_values = (article.title, article.content, article.article_id)
    retrieve_values = (article.article_id)

    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute(put_query, put_values)
            cur.execute(retrieve_query, retrieve_values)
            
            return __sql_to_pydantic(cur.fetchone())


def delete_article(conn: psycopg.Connection,
                   article: DELETE_ArticleRequest) -> None:
    query = """
        DELETE FROM article 
        WHERE id = %s;
    """
    values = (article.article_id,)

    with cur.cursor() as cur:
        with cur.transaction():
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




