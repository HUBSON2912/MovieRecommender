import csv
import consts
import custom_types


def readMovies() -> list[custom_types.Movie]:
    """Returns the list of movies sorted by popularity (descending)."""
    result:list[custom_types.Movie]=[]
    with open(consts.MOVIES) as inputFile:
        reader=list(csv.DictReader(inputFile))
        headers=reader[0]
        reader=reader[1:]
        result=list(filter(
                        lambda x: not (x is None), 
                        map(custom_types.Movie.transform, reader)
                    ))
    
    result.sort(key=lambda x: x.popularity, reverse=True)
    return result

# if __name__=="__main__":