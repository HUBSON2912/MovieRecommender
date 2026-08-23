# fix it has overflow on dot product in model with bigger data
# for some reason the values in matrix Q grows really fast

import csv
import os
import consts
import funk_model

def areDataComplete() -> bool:
    filesInData:list[str] = os.listdir(consts.DATA_DIR)
    for file in consts.REQURED_DATA:
        if not (file in filesInData):
            return False
    return True

def readRatings() -> dict[tuple[int,int], float]: 
    res:dict[tuple[int,int], float] = dict()
    with open(consts.RATINGS) as file:
        reader=list(csv.reader(file))
        headers=reader[0]
        reader=reader[1:]
        for userId,movieId,rating,_ in reader:
            userId,movieId,rating = int(userId),int(movieId),float(rating)
            res[(userId, movieId)] = rating

    return res

def getNumUsersItems(ratings: dict[tuple[int,int], float]) -> tuple[int,int]:
    unum, inum=0,0
    for u,i in ratings.keys():
        unum=max(unum, u)
        inum=max(inum, i)
    return unum, inum

if __name__=="__main__":
    if not areDataComplete():
        raise FileNotFoundError("Missing data file. Try to download the data .zip package.")

    real_ratings:dict[tuple[int,int], float] = readRatings()

    num_users:int = 0
    num_movies:int = 0
    num_users, num_movies=getNumUsersItems(real_ratings)

    
    model=funk_model.Funk(num_users+1, num_movies+1,consts.SECOND_DIMENTIONS, 10**-8, 0.01, 0.005)  # +1 because the user is the 0th and ids are counted from 1
    model.train(real_ratings, max_iterations=100)
    
    print("Predicions:\n")
    model.printPredictions()

    for u in range(model.nusers):
        for i in range(model.nitems):
            if (u,i) in real_ratings.keys():
                Rp=model.predict(u,i)
                R=real_ratings[(u,i)]
                print(f"{(u,i)}:\tR={R}\tR'={Rp}\tdR={Rp-R}")