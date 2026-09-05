from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import consts
from handledata import readMovies

app = FastAPI()

# handle CORS policy
# (I run both back and frontend at localhost)
origins=[
    "http://localhost",
    "http://localhost:5173",
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

movies=readMovies()

@app.get("/")
def status():
    return {"status": "running"}

@app.post("/get/movies/{offset}")
def getMovies(offset:int):
    # return movies[0]
    return JSONResponse(content = jsonable_encoder(movies[offset : offset+consts.RETURN_MOVIES]) )

@app.post("/search/{query}")
def searchMovie(query:str):
    query=query.lower()
    if query[0:3]=="id:": # looking for a movie with specified ID
        searchId=int(query[3:])

        foundMovie=list(filter(lambda mov: mov.id==searchId, movies)) # as list for integrity
        return JSONResponse(content = jsonable_encoder(foundMovie))
    else:
        foundMovies = list(filter(lambda mov: query in mov.title.lower(), movies))
        return JSONResponse(content = jsonable_encoder(foundMovies))
