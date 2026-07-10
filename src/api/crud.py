from datetime import date

import psycopg
from fastapi import HTTPException, status

from src.api.models import ArticleCreate, ArticleResponse, ArticleUpdate
from src.api.utils import sql_to_pydantic


def return_articles(conn: psycopg.Connection) -> list[ArticleResponse]:
    "Return all articles in the db."
    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute("""
                SELECT * FROM article;
            """)

            return [sql_to_pydantic(row) for row in cur.fetchall()]


def return_article(conn: psycopg.Connection,
                article_id: int) -> ArticleResponse:
    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute("""
                SELECT * FROM article
                WHERE id = %s
            """, (article_id,))
            
            if not (row := cur.fetchone()):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="The requested resource was not found!"
                )
           
            return sql_to_pydantic(row)


def create_article(conn: psycopg.Connection,
                payload: ArticleCreate) -> ArticleResponse:

    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute("""
                INSERT INTO article (title, content, publish_date)
                VALUES (%s, %s, %s);
            """, (payload.title, payload.content, date.today()))

            cur.execute("""
                SELECT * FROM article
                WHERE title = %s;
            """, (payload.title,))

            return sql_to_pydantic(cur.fetchone())


def edit_article(conn: psycopg.Connection,
                 payload: ArticleUpdate,
                 article_id: int) -> ArticleResponse: 

    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute("""
                SELECT * FROM article
                WHERE id = %s;
            """, (article_id,))
            
            row = cur.fetchone()
            if not (row):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="The requested resource was not found!"
                )

            if (payload.title and payload.content):
                cur.execute("""
                    UPDATE article SET
                    title = %s, content = %s
                    WHERE id = %s;
                """, (payload.title, payload.content, article_id))

            elif payload.title:
                cur.execute("""
                    UPDATE article SET 
                    title = %s 
                    WHERE id = %s;
                """, (payload.title, article_id))
            
            else:
                cur.execute("""
                    UPDATE article SET
                    content = %s 
                    WHERE id = %s;
                """, (payload.content, article_id))

            cur.execute("""
                SELECT * FROM article 
                WHERE id = %s;
            """, (article_id,))

            return sql_to_pydantic(cur.fetchone())  


def delete_article(conn: psycopg.Connection,
                   article_id: int) -> None:
    with conn.cursor() as cur:
        with conn.transaction():
            cur.execute("""
                SELECT EXISTS 
                (SELECT 1 FROM article WHERE id = %s);
            """, (article_id,))
            
            if not (cur.fetchone()):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="The resource to be deleted was not found!")

            cur.execute("""
                DELETE FROM article WHERE id = %s;
            """, (article_id,))
    




