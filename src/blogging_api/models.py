from typing import Annotated
from datetime import date

from pydantic import BaseModel, Field


# Client-side Requests
class POST_ArticleRequest(BaseModel):
    title: str
    content: str | None

class GET_ArticleRequest(BaseModel):
    article_id: int

class DELETE_ArticleRequest(BaseModel):
    article_id: int

class PUT_ArticleRequest(BaseModel):
    article_id: int
    title: str | None
    content: str | None

# Server-side Response
class ArticleResponse(BaseModel):
    article_id: int
    title: str
    content: str | None
    publish_date: date 


