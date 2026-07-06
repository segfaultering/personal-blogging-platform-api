import blogging_api.config as config


@config.APP.get("/article") -> list[dict]
def get_articles():
    with config.CONN.transaction():
        config.CONN.execute("""
            SELECT * FROM article;
        """)

        rows = config.CONN.fetchall()

    return [{"id": id_, 
             "title": title, 
             "content": content, 
             "publish_date": str(publish_date)} 
            for (id_, title, content, publish_date) in rows]


@config.APP.get("/article/{id_}")
def get_article(id_: int):
    with config.CONN.transaction():
        config.CONN.execute("SELECT * FROM article WHERE id


@config.APP.post("/article/")
def create_article(title: str, content: str, date: str):
    pass

@config.APP.delete("/article/{id_}")
def delete_article(id_: int):
    pass

@config.APP.put("/article/{id_}")
def edit_article(id_: int, title: str | None, content: str | None, 
                 date: str | None):
    pass




