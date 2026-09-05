from __future__ import annotations
import json
import typing
import datetime
from pydantic import BaseModel, ValidationError

class Collection(typing.TypedDict):
    id:int
    name:str
    poster_path:str
    backdrop_path:str

class Genre(typing.TypedDict):
    id:int
    name:str

class Company(typing.TypedDict):
    name:str
    id:int

class Country(typing.TypedDict):
    iso_3166_1:str
    name:str

class Language(typing.TypedDict):
    iso_639_1:str
    name:str


# general purpose functions but aimed for Movies
def strToDate(str:str)->datetime.date|None:
    params=str.split("-")
    y,m,d=list(map(int,params))
    return datetime.date(y, m, d)

def strToListOfGenre(str:str)->list[str]:
    str=str.replace("'", "\"")
    genres:Genre=json.loads(str)
    return list(map(lambda x: x["name"], genres))

TRANSFORMATION_FUNCTIONS:dict[str, typing.Callable] = {
    "adult": lambda str: str=="True",
    "genres": strToListOfGenre,
    "id": int,
    "imdb_id": str,
    "overview": str,
    "popularity": float,
    "poster_path": str,
    "release_date": strToDate,
    "title": str,
    "vote_average": float,
    "vote_count": int
}

class Movie(BaseModel):
    adult:bool
    genres:list[str] # just names
    id:int
    imdb_id:str
    overview:str
    popularity:float
    poster_path:str  # image.tmdb.org api -> developer.themoviedb.org/docs/image-basics
    release_date:datetime.date
    title:str
    vote_average:float
    vote_count:int

    @staticmethod
    def transform(dict_csv: dict) -> Movie|None:
        # remove fields that are unnecessary but exist in csv
        keyValPairs:list[str, typing.Any] = dict_csv.items()
        keyValPairs=list(filter(lambda kv: kv[0] in Movie.__annotations__.keys(), keyValPairs))

        dict_correctTypes={}
        for name,value in keyValPairs:
            try:
                dict_correctTypes[name]=TRANSFORMATION_FUNCTIONS[name](value)
            except:
                # if data not valid then None
                return None
        
        try:
            return Movie.model_validate(dict_correctTypes)
        except ValidationError:
            # missing data or wrong data
            return None

# if __name__=="__main__":
    
#     unittest.main()