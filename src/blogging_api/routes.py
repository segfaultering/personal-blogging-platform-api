from fastapi import FastAPI


app = FastAPI()

@app.get("/article")
def get_articles():
    pass

@app.get("/article/{id_}")
def get_article(id_: int):
    pass

@app.post("/article/")
def create_article(title: str, content: str, date: str):
    pass

@app.delete("/article/{id_}")
def delete_article(id_: int):
    pass

@app.put("/article/{id_}")
def edit_article(id_: int, title: str | None, content: str | None, 
                 date: str | None):
    pass




