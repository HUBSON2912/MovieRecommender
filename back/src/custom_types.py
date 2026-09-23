from __future__ import annotations
import typing
import datetime
from pydantic import BaseModel, ValidationError

from .misc import strToDate, strToListOfGenre

class Genre(typing.TypedDict):
    id:int
    name:str


TRANSFORMATION_FUNCTIONS:dict[str, typing.Callable[[str],typing.Any]] = {
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
    def transform(dict_csv: dict[str,str]) -> Movie|None:
        
        # remove fields that are unnecessary but exist in csv
        keyValPairs= dict_csv.items()
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


class Rate(BaseModel):
    movieId:int
    rate:float

    @staticmethod
    def transform(readDict:dict[str,int])->Rate:
        return Rate(movieId=readDict["movieId"], rate=readDict["rate"])