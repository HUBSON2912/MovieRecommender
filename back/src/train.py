import pathlib
import consts
import funk_model
import custom_types
import handledata

def getNumUsersItems(ratings: dict[tuple[int,int], float]) -> tuple[int,int]:
    unum, inum=0,0
    for u,i in ratings.keys():
        unum=max(unum, u)
        inum=max(inum, i)
    return unum, inum

def trainModel(userRatings:list[custom_types.Rate]=[], map_of_ids:dict[int, int]|None=None, show_logs:bool=False)->str:
    if not handledata.areDataComplete():
        raise FileNotFoundError("Missing data file. Try to download the data .zip package.")

    real_ratings:dict[tuple[int,int], float] = handledata.readRatings(map_of_ids)

    if len(userRatings)!=0:
        for rate in userRatings:
            real_ratings[(consts.REAL_USER_ID, rate.movieId)]=rate.rate

    num_users:int = 0
    num_movies:int = 0
    num_users, num_movies=getNumUsersItems(real_ratings)
    
    model=funk_model.Funk(num_users+1, num_movies+1,consts.SECOND_DIMENTIONS, 0.01, 0.001, 0.001)  # +1 because the user is the 0th and ids are counted from 1
    model.train(real_ratings, max_iterations=consts.ITERATIONS, show_logs=show_logs)
    
    return model.save().name
    
    # model.printPredictions()

if __name__=="__main__":
    movies,ids=handledata.readMovies()
    name=trainModel(map_of_ids=ids)
    model=funk_model.Funk.load(pathlib.Path(consts.SAVE_DIR/name))
    # model.printPredictions()
