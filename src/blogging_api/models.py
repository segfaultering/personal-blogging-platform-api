from typing import Annotated
from pydantic import BaseModel, Field


class Article(BaseModel):
    id_: Annotated[int, Field(alias="id")] 
    title: Annotated[str, Field(max_length=30)]
    content: str 





