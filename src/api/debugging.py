import psycopg

from src.api.crud import return_articles

conn = psycopg.connect("dbname=blogging user=mohsin")

articles = return_articles(conn)

