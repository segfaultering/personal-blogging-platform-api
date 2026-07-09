from fastapi import HTTPException, FastAPI, Depends, Path, status
import psycopg

import config
from utils import get_db_conn
from models import ArticleCreate, ArticleResponse

from datetime import date


# Connection type
type Connection = Annotated[psycopg.Connection, Depends(get_db_conn)]

app = FastAPI()


# GET
@app.get("/article/", status_code=status.HTTP_200_OK)
def return_all_articles(db_conn: Connection) -> list[ArticleResponse]
    with db_conn.cursor() as cur:
        with db_conn.transaction():
            cur.execute("""
                SELECT * FROM article;
            """)

            return [sql_to_pydantic(row) for row in cur.fetchall()]

@app.get("/article/{article_id}", status_code=status.HTTP_200_OK)
def return_article(db_conn: Connection, article_id: int) -> ArticleResponse:
    with db_conn.cursor() as cur:
        with db_conn.transaction():
            cur.execute("""
                SELECT * FROM article
                WHERE id = %s
            """, (article_id,))
            
            if not (any(row := cur.fetchone())):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="The requested resource was not found!"
                )
           
            return sql_to_pydantic(row)
            

# POST
@app.post("/article/, status_code=status.HTTP_201_CREATED)
def create_article(payload: ArticleCreate) -> ArticleResponse:
    











