# Personal Blogging API
A personal blogging API for learning backend better. The primary goal of this application is to learn some of the fundamentals of backend development, specifically in building a simple CRUD app with FastAPI and PostgreSQL (via the `psycopg` package).

## GOALS:
1. Learn API development basics with FastAPI.
2. Learn to work with PostgreSQL.

I can safely say that both of these goals were met along with getting some experience with Curl, Pydantic, and Docker, along with many other things.

## HOW TO RUN:
If you, for some reason, want to try and run this project, then you need to have a local instance of PostgreSQL running, with a database named "blogging" with a singular table "article" with the following schema:

- id: SERIAL PRIMARY KEY
- title: TEXT UNIQUE NOT NULL
- content: TEXT 
- date: DATE NOT NULL

Then you run the project by installing the dependencies, I used `uv`, so you might need to install `uv`, then go to the project root, and run `uv sync`. When all of the dependencies are finished downloading, you may need to also download a Python 3.12 interpreter. Then, standing at the project root, run the command:

```
uv run fastapi dev -e src.api.routes:app
```

This will get the API up and running. 
