from fastapi import FastAPI, Depends, Path, status
import psycopg

from utils import get_db_conn
from models import ArticleCreate, ArticleUpdate, ArticleResponse
import crud

from datetime import date


# Connection type
type Connection = Annotated[psycopg.Connection, Depends(get_db_conn)]

app = FastAPI()


# GET
@app.get("/article/", status_code=status.HTTP_200_OK)
def return_articles(db_conn: Connection) -> list[ArticleResponse]
    return crud.return_articles(db_conn)

    
@app.get("/article/{article_id}", status_code=status.HTTP_200_OK)
def return_article(
        db_conn: Connection, 
        article_id: Annotated[int, Path(
            title="The ID of the article to fetch.",
            gt=0
        )]) -> ArticleResponse:

    crud.return_article(db_conn, article_id)            

# POST
@app.post("/article/, status_code=status.HTTP_201_CREATED")
def create_article(db_conn: Connection, payload: ArticleCreate) -> ArticleResponse:
    crud.create_article(db_conn, payload)

    
# DELETE
@app.delete("/article/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(db_conn: Connection, 
                   article_id: Annotated[int, Path(
                                title="The id of the article to delete",
                                gt=0
                            ))) -> None: 
    with db_conn.cursor() as cur:
        with db_conn.transaction():
            cur.execute("""
                SELECT EXISTS 
                (SELECT 1 FROM article WHERE id = %s);
            """, (article_id,))
            
            if not (cur.fetchone()):
                raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                                    detail="The resource to be deleted was not found!")

            cur.execute("""
                DELETE FROM article WHERE id = %s;
            """, (article_id,))

@app.patch("/article/{article_id}", status_code=status.HTTP_200_OK)
def update_article(
        db_conn: Connection, 
        payload: ArticleUpdate,
        article_id: Path(
            title="The ID of the article to update."
            gt=0
        )) -> ArticleResponse:
    with db_conn.cursor() as cur:
        with db_conn.transaction()
            cur.execute("""
                SELECT EXISTS(
                    SELECT 1 FROM article 
                    WHERE id = %s
                );
            """, (article_id,))
            
            if not (cur.fetchone()):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="The requested resource was not found!"
                )

            cur.execute("""
                UPDATE article SET 
                title = %s AND content = %s
                WHERE id = %s;
            """, (payload.title, payload.content, article_id))

            cur.execute("""
                SELECT * FROM article 
                WHERE id = %s;
            """, (article_id,))

            return sql_to_pydantic(cur.fetchone())  











