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

if __name__=="__main__":
    odp=readMovies()
    print(type(odp))
    print(type(odp[0]))
    assert isinstance(odp[0], custom_types.BaseModel)

# adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count