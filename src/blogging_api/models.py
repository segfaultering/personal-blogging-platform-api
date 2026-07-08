from typing import Annotated
from datetime import datetime

from pydantic import BaseModel, Field


class Article(BaseModel):
    "The base resource representation"
    title: Annotated[str, Field(max_length=30)]
    content: str | None 


class ArticleReq(Article):
    "The client request representation of the article"
    pass


class ArticleResp(Article):
    "The server response representation of the article"
    article_id: int
    publish_date: datetime 


