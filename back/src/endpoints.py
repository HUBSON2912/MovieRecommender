from fastapi import FastAPI
import consts
from handledata import readMovies

app = FastAPI()
movies=readMovies()

@app.get("/")
def status():
    return {"status": "running"}

@app.get("/get/movies/{offset}")
def getMovies(offset:int):
    # return movies
    return movies[offset:offset+consts.RETURN_MOVIES]

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    try:
        return {"item_id": item_id, "q": consts.REQURED_DATA[item_id]}
    except:
        return {"item_id": item_id, "q": None}