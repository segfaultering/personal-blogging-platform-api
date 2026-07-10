import psycopg

from src.api.crud import edit_article
from src.api.models import ArticleUpdate

conn = psycopg.connect("dbname=blogging user=mohsin")

article_in = ArticleUpdate(title="NEW TITLE")
article = edit_article(conn, article_in, 4) 

