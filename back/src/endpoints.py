import json
import consts
import os
import funk_model
import train
import custom_types
from misc import hasBinExtentnion
from fastapi import FastAPI, BackgroundTasks, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
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

currently_training:bool=False # only one model can be trained at once

movies, ids_map=readMovies()

@app.get("/")
def serverStatus()->object:
    """Ping endpoint

    Returns:
        {status: "running"}
    """
    return {"status": "running"}

@app.post("/movies/batch/{offset}")
def getMovies(offset:int)->JSONResponse:
    """Load a batch of movies, beginning from given parameter.

    Args:
        offset (int): the index of the beginning movie

    Returns:
        list[Movie]: a batch of movies
    """
    # return movies[0]
    return JSONResponse(content = jsonable_encoder(movies[offset : offset+consts.RETURN_MOVIES]) )

@app.post("/movies/ids")
def getMoviesWithID(ids: list[int])->JSONResponse:
    """Find movies with given ids

    Args:
        ids (list[int]): wanted movie ids

    Returns:
        list[Movie]: movies which id are in ids argument
    """
    foundMovies=list(filter(lambda movie: movie.id in ids, movies))
    return JSONResponse(content=jsonable_encoder(foundMovies))

@app.post("/search/{query}")
def searchMovie(query:str)->JSONResponse:
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
def getListOfSavedModels()->JSONResponse:
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
def getRecommendations(fileName:str)->JSONResponse:
    model=funk_model.Funk.load(consts.SAVE_DIR / fileName)
    user=consts.REAL_USER_ID  # it's aimed for one user
    predictions=model.predictForUser(user)
    predictions.sort(key=lambda x: x[1], reverse=True)

    bestMoviesIds:list[int]=[]
    for pred in predictions:
        if len(bestMoviesIds)>=consts.RETURN_MOVIES:
            break
        if pred[0] in ids_map.values():
            bestMoviesIds.append(pred[0])

    return getMoviesWithID(bestMoviesIds)

@app.post("/models/retrain", status_code=status.HTTP_202_ACCEPTED)
async def retrainModel(ratings:list[custom_types.Rate], background_tasks: BackgroundTasks)->JSONResponse:
    global currently_training

    if currently_training:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, "Server is currently training a model.")
    else:
        def __train(userRatings:list[custom_types.Rate], ids_map: dict[int,int]):
            global currently_training
            currently_training=True
            train.trainModel(userRatings, ids_map)
            currently_training=False
        
        userRatings:list[custom_types.Rate]=jsonable_encoder(ratings)
        background_tasks.add_task(__train, userRatings, ids_map)

        return JSONResponse(content=jsonable_encoder({"status": "training"}))
    
@app.post("/models/trainStatus")
def trainingStatus()->JSONResponse:
    if currently_training:
        return JSONResponse(content=jsonable_encoder({"status": "training"}))
    return JSONResponse(content=jsonable_encoder({"status": "free"}))

if __name__=="__main__":
    recom=getRecommendations("funk-model-2026-9-15T21:15:54.bin").body
    if type(recom) is bytes:
        print(json.loads(recom))