import consts
import os
import funk_model
import train
from misc import hasBinExtentnion
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from handledata import readMovies
from custom_types import Movie

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
def status()->object:
    """Ping endpoint

    Returns:
        {status: "running"}
    """
    return {"status": "running"}

@app.post("/movies/{offset}")
def getMovies(offset:int)->list[Movie]:
    """Load a batch of movies, beginning from given parameter.

    Args:
        offset (int): the index of the beginning movie

    Returns:
        list[Movie]: a batch of movies
    """
    # return movies[0]
    return JSONResponse(content = jsonable_encoder(movies[offset : offset+consts.RETURN_MOVIES]) )

@app.post("/movies/ids")
def getMoviesWithID(ids: list[int])->list[Movie]:
    """Find movies with given ids

    Args:
        ids (list[int]): wanted movie ids

    Returns:
        list[Movie]: movies which id are in ids argument
    """
    foundMovies=list(filter(lambda movie: movie.id in ids, movies))
    return JSONResponse(content=jsonable_encoder(foundMovies))

@app.post("/search/{query}")
def searchMovie(query:str)->list[Movie]:
    """Searching movies by title or ID

    Args:
        query (str | "id:{number}"): string that should be in the title of the movie or "id:{number}" that returns single movie with given id if exists

    Returns:
        list[Movie]: list of movies that include string in {query} or list with single movie with given id
    """
    query=query.lower()
    if query[0:3]=="id:": # looking for a movie with specified ID
        searchId=int(query[3:])

        foundMovie=list(filter(lambda mov: mov.id==searchId, movies)) # as list for integrity
        return JSONResponse(content = jsonable_encoder(foundMovie))
    else:
        foundMovies = list(filter(lambda mov: query in mov.title.lower(), movies))
        return JSONResponse(content = jsonable_encoder(foundMovies))

@app.post("/models/list")
def getListOfSavedModels()->list[str]:
    """Get list of trained models

    Returns:
        list[str]: list of file names with trained models
    """
    if not (consts.SAVE_DIR.exists()):
        return JSONResponse(content=jsonable_encoder( [] ))

    
    fileNames:list[str]=os.listdir(consts.SAVE_DIR)
    fileNames=list(filter(hasBinExtentnion, fileNames))
    return JSONResponse(content=jsonable_encoder(fileNames))

@app.post("/models/recommend/{fileName}")
def getRecommendations(fileName:str)->list[Movie]:  # todo jakoś że film, oceny i przewidywana ocena
    model=funk_model.Funk.load(consts.SAVE_DIR / fileName)
    user=consts.REAL_USER_ID  # it's aimed for one user
    predictions=model.predictForUser(user)
    predictions=list(filter(lambda x: x[1]>=consts.RECOMMENDATION_RATE_THRESHOLD,predictions))

    # todo test it if i can change the values simply
    predictedMovies=getMoviesWithID(list(map(lambda x: x[0], predictions)))
    print(type(predictedMovies))
    print(type(predictedMovies[0]))
    return predictedMovies

@app.put("/models/retrain")
def retrainModel():
    train.trainModel()


if __name__=="__main__":
    print(getRecommendations("funk-model-2026-9-10T11:48:6.bin"))