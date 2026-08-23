import datetime
import pickle
import csv
import os
import consts
import custom_types
import numpy as np
import funk_model
from typing import TypedDict, cast

def areDataComplete() -> bool:
    filesInData:list[str] = os.listdir(consts.DATA_DIR)
    for file in consts.REQURED_DATA:
        if not (file in filesInData):
            return False
    return True

def getRatings() -> dict[tuple[int,int], float]:
    real_ratings:dict[tuple[int,int], float] = dict()
    with open(consts.RATINGS) as file:
        reader=list(csv.reader(file))
        headers=reader[0]
        reader=reader[1:]
        for userId,movieId,rating,_ in reader:
            userId,movieId,rating = int(userId),int(movieId),float(rating)
            real_ratings[(userId, movieId)] = rating
    
    return real_ratings

if __name__=="__main__":
    if not areDataComplete():
        raise FileNotFoundError("Missing data file. Try to download the data .zip package.")


    # TODO: every field in csv is string so it cant be converted
    # movie_list:list[custom_types.Movie] = []
    # with open(consts.MOVIES) as file:
    #     reader=list(csv.reader(file))
    #     headers=reader[0] # skip headers
    #     reader=reader[1:]

    #     for row in reader:
    #         movie_object=cast(custom_types.Movie, {})
    #         for i in range(len(row)): # len(row)=len(headers)
    #             movie_object[headers[i]]=row[i]
    #         print(movie_object)
    #         # print(type(cast(custom_types.Movie, movie_object)))
    #         custom_types.Movie.dictToMovie(movie_object)
    #         # print(custom_types.Movie.dictToMovie(movie_object))

    num_users:int = 0
    num_movies:int = 0

    real_ratings:dict[tuple[int,int], float] = getRatings()

    # read movies and get the number of them
    with open(consts.MOVIES) as file:
        reader=list(csv.reader(file))
        headers=reader[0]
        reader=reader[1:]
        num_movies=max(num_movies,len(reader))

    SECOND_DIMENTIONS=5
    model=funk_model.Funk(num_users+1, num_movies+1,SECOND_DIMENTIONS, 1e-8, 0.1)  # +1 because the user is the 0th and ids are counted from 1
    model.train(real_ratings)
    print("koniec\n\n")
    # print(np.cross(model.P, model.Q),axisa=0, axisb=0)
    for u in range(model.nusers):
        print(f"{u}: ",end="")
        for i in range(model.nitems):
            print(np.dot(model.P[u], model.Q.transpose()[i]), end=";")
        print()
    print("\n\n\n")

    for u in range(model.nusers):
        for i in range(model.nitems):
            if (u,i) in real_ratings.keys():
                Rp=np.dot(model.P[u], model.Q.transpose()[i])
                R=real_ratings[(u,i)]
                print(f"{(u,i)}:\tR={R}\tR'={Rp}\tdR={Rp-R}")
    # with open(f"./model{datetime.datetime.now()}", "w") as file:
    #     pickle.(model,file)