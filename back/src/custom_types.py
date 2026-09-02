import typing
import datetime

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

class Movie(typing.TypedDict):
    adult:bool
    genres:list[Genre]
    id:int
    overview:typing.Optional[str]
    popularity:float
    poster_path:typing.Optional[str]  # image.tmdb.org api -> developer.themoviedb.org/docs/image-basics
    release_date:datetime.date
    title:str
    vote_average:float
    vote_count:int