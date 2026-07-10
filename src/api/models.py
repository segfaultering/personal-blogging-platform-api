from datetime import date
from typing import Annotated

from pydantic import BaseModel, Field


class ArticleBase(BaseModel):
    title: Annotated[str, Field(
        min_length=8,
        max_length=64
    )]

    content: Annotated[str | None, Field(
        default=None,
        min_length=0,
        max_length=10_000
    )]


class ArticleCreate(ArticleBase):
    ...


class ArticleUpdate(BaseModel): 
    title: Annotated[str | None, Field(
        default=None,
        min_length=8,
        max_length=64
    )]

    content: Annotated[str | None, Field(
        default=None,
        min_length=0,
        max_length=10_000
    )]

# Server-side Response
class ArticleResponse(ArticleBase):
    article_id: Annotated[int, Field(
        frozen=True,
        gt=0,
    )]

    publish_date: date


