from typing import Annotated

from fastapi import FastAPI, Depends, Path, status
import psycopg

from src.api.utils import get_db_conn
from src.api.models import ArticleCreate, ArticleUpdate, ArticleResponse
import src.api.crud as crud


# Connection type
type Connection = Annotated[psycopg.Connection, Depends(get_db_conn)]

app = FastAPI()


# GET
@app.get("/article/", status_code=status.HTTP_200_OK, response_model=list[ArticleResponse])
def return_articles(db_conn: Connection) -> list[ArticleResponse]:
    return crud.return_articles(db_conn)

    
@app.get("/article/{article_id}", status_code=status.HTTP_200_OK, response_model=ArticleResponse)
def return_article(
        db_conn: Connection, 
        article_id: Annotated[int, Path(
            title="The ID of the article to fetch.",
            gt=0
        )]) -> ArticleResponse:

    return crud.return_article(db_conn, article_id)            

# POST
@app.post("/article/, status_code=status.HTTP_201_CREATED")
def create_article(db_conn: Connection, payload: ArticleCreate) -> ArticleResponse:
    return crud.create_article(db_conn, payload)

    
# DELETE
@app.delete("/article/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(
        db_conn: Connection,
        article_id: Annotated[int, Path(
            title="The id of the article to delete",
            gt=0
        )]) -> None:
    crud.delete_article(db_conn, article_id)

# PATCH
@app.patch("/article/{article_id}", status_code=status.HTTP_200_OK, response_model=ArticleResponse)
def update_article(
        db_conn: Connection, 
        payload: ArticleUpdate,
        article_id: Annotated[int, Path(
            title="The ID of the article to update.",
            gt=0
        )]) -> ArticleResponse:
    return crud.edit_article(db_conn, payload, article_id)










