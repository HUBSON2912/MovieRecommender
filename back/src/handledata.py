import csv
import consts
import custom_types
import os


def readMovies() -> tuple[list[custom_types.Movie], dict[int,int]]:
    """Returns the list of movies sorted by popularity (descending) and dictionary of ids. There are missing movies id so it shifts all the movie ids down."""
    result:list[custom_types.Movie]=[]
    ids_map:dict[int, int]={}
    with open(consts.MOVIES) as inputFile:
        reader=csv.reader(inputFile)
        headers=next(reader)
        for row in reader:
            rowAsDict=dict(zip(headers, row))
            movie=custom_types.Movie.transform(rowAsDict)
            if not movie is None:
                result.append(movie)
        
    for i in range(len(result)):
        movie=result[i]
        ids_map[movie.id]=i+1
        result[i].id=i+1
    
    result.sort(key=lambda x: x.popularity, reverse=True)
    return (result, ids_map)

def readRatings(map_of_ids:dict[int,int]|None=None) -> dict[tuple[int,int], float]: 
    res:dict[tuple[int,int], float] = dict()
    with open(consts.RATINGS) as file:
        reader=list(csv.reader(file))
        reader=reader[1:] # skip headers
        for userId,movieId,rating,_ in reader:
            userId,movieId,rating = int(userId),int(movieId),float(rating)

            try:
                if not (map_of_ids is None):
                    movieId=map_of_ids[movieId]
            except KeyError:
                # for some reason, the data i have are not consitent
                # the first rating is user:1, movie:31 and there is no movie with id 31
                continue
            
            res[(userId, movieId)] = rating

    return res

def areDataComplete() -> bool:
    filesInData:list[str] = os.listdir(consts.DATA_DIR)
    for file in consts.REQURED_DATA:
        if not (file in filesInData):
            return False
    return True

if __name__=="__main__":
    movies, ids=readMovies()
    print(movies[0])
