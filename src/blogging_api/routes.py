import blogging_api.config as config


@config.APP.get("/article") -> list[dict]
def get_articles():
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            cur.execute("""
                SELECT * FROM article;
            """)

            rows = cur.fetchall()

    return [{"id": id_, 
             "title": title, 
             "content": content, 
             "publish_date": str(publish_date)} 
            for (id_, title, content, publish_date) in rows]


@config.APP.get("/article/{id_}")
def get_article(id_: int):
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            cur.execute(t"SELECT * FROM article WHERE id = {id_}")
        row = cur.fetchone()
    
    if not row:
        return {}

    id_, title, content, date = row
    return {
        "id": id_,
        "title": title,
        "content": content,
        "date": str(date)
    }
    

@config.APP.post("/article/")
def create_article(title: str, content: str, date: str):
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            cur.execute(t"""
                INSERT INTO article (title, content, date) 
                VALUES ({title}, {content}, {date});
            """)

    return {}

@config.APP.delete("/article/{id_}")
def delete_article(id_: int):
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            cur.execute(t"""
                DELETE FROM article WHERE id = {id_};
            """)

    return {}

@config.APP.put("/article/{id_}")
def edit_article(id_: int, title: str | None, content: str | None):
    with config.CONN.cursor() as cur:
        with config.CONN.transaction():
            if title and content:
                query = t"""
                    UPDATE article SET title = {title}, content = {content}
                    WHERE id = {id_};
                """

            elif title:
                query = t"UPDATE article SET title = {title} WHERE id = {id_};"

            elif content: 
                query = t"UPDATE article SET content = {content} WHERE id = {id_};"

            cur.execute(query)

    return {}








