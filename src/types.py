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
    belongs_to_collection: typing.Optional[Collection]
    budget:int
    genres:list[Genre]
    homepage: typing.Optional[str]
    id:int
    imdb_id:str
    original_language:str
    original_title:str
    overview:typing.Optional[str]
    popularity:float
    poster_path:str
    production_companies:list[Company]
    production_countries:list[Country]
    release_date:datetime.date
    revenue:int
    runtime:float
    spoken_languages:list[Language]
    status:str
    tagline:typing.Optional[str]
    title:str
    video:bool
    vote_average:float
    vote_count:int
    