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

    # read ratings
    real_ratings:dict[tuple[int,int], float] = dict()
    with open(consts.RATINGS) as file:
        reader=list(csv.reader(file))
        headers=reader[0]
        reader=reader[1:]
        for userId,movieId,rating,_ in reader:
            userId,movieId,rating = int(userId),int(movieId),float(rating)
            real_ratings[(userId, movieId)] = rating

            num_users=max(num_users, userId)

    # read movies and get the number of them
    with open(consts.MOVIES) as file:
        reader=list(csv.reader(file))
        headers=reader[0]
        reader=reader[1:]
        num_movies=len(reader)

    # print(real_ratings)

    model=funk_model.Funk(num_users, num_movies, 100)
    print(model.P)
    print(model.P.shape)
    print(model.Q)
    print(model.Q.shape)