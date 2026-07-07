"""Utility functions."""
from pydantic import BaseModel

from typing import Any
from datetime import datetime

from blogging_api.models import Article

# Row tuple datatype
Row = tuple[int, str, str, datetime.date]

def sql_to_pydantic(row: Row) -> Article:
    id_, title, content, publish_date = row
    return Article(
        id_=id_,
        title=title,
        content=content,
        publish_date=publish_date
    )















