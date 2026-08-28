from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

import consts

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    try:
        return {"item_id": item_id, "q": consts.REQURED_DATA[item_id]}
    except:
        return {"item_id": item_id, "q": None}