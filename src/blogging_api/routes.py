from fastapi import HTTPException

import blogging_api.config as config
from utils import sql_to_pydantic
from models import Article

from datetime import date

@config.APP.get("/article")
def get_articles() -> list[Article]:
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            cur.execute("SELECT * FROM article;")
            rows = cur.fetchall()

    return [sql_to_pydantic(row) for row in rows]


@config.APP.get("/article/{id_}")
def get_article(id_: int) -> Article:
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            cur.execute("SELECT * FROM article WHERE id = (%s)", (id_, ))
        
        if not (row := cur.fetchone()):
            raise HTTPException(status_code=404, detail="The requested resource is not found!")

    return sql_to_pydantic(row)    

@config.APP.post("/article/")
def create_article(title: str, content: str, date: date) -> Article:
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            cur.execute("""
                INSERT INTO article (title, content, date) 
                VALUES (%s, %s, %s);
            """, (title, content, date))

            cur.execute("""
                SELECT id from article WHERE 
                title = (%s) AND
                content = (%s) AND 
                date = (%s);
            """, (title, content, date))

            id_ = cur.fetchone()

    return sql_to_pydantic((id_, title, content, date))


@config.APP.delete("/article/{id_}", )
def delete_article(id_: int, status_code=204):
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            cur.execute("SELECT * FROM article WHERE id = (%s)", (id_, ))
            if not cur.fetchone():
                    raise HTTPException(status_code=404, detail="The resource to be deleted doesn't exist!")

            cur.execute("DELETE FROM article WHERE id = (%s);", (id_, ))


@config.APP.patch("/article/{id_}", status_code=200)
def edit_article(id_: int, title: str | None, content: str | None):
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():

            cur.execute("SELECT * FROM article WHERE id = (%s);", (id_, ))
            if not cur.fetchone():
                raise HTTPException(status_code=404, detail="The requested resource doesn't exist!")

            query = "UPDATE article SET"
            end = " WHERE id = (%s);"

            if title and content:
                query += " title = (%s), content = (%s)" + end
                tup = (query, (title, content, id_))

            if title:
                query += " title = (%s)" + end
                tup = (query, (title, id_))

            elif content: 
                query += " content = (%s)" + end
                tup = (query, (content, id_))

            cur.execute(*tup)








