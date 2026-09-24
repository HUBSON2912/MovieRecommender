import datetime

import pytest

from back.src.custom_types import Movie
from back.src.handledata import readMovies
from back.src.misc import strToDate

@pytest.fixture
def common_movies_file(tmp_path):
    headers="adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count"
    movie1="False,\"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}\",30000000,\"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]\",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,\"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.\",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,\"[{'name': 'Pixar Animation Studios', 'id': 3}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-10-30,373554033,81.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,,Toy Story,False,7.7,5415"
    movie2="False,,65000000,\"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]\",,8844,tt0113497,en,Jumanji,\"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.\",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,\"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-15,262797249,104.0,\"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]\",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413"
    movie3="False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"A family wedding reignites the ancient feud between next-door neighbors and fishing buddies John and Max. Meanwhile, a sultry Italian divorcée opens a restaurant at the local bait shop, alarming the locals who worry she'll scare the fish away. But she's less interested in seafood than she is in cooking up a hot time with Max.\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92"
    movie4="False,,16000000,\"[{'id': 35, 'name': 'Comedy'}, {'id': 18, 'name': 'Drama'}, {'id': 10749, 'name': 'Romance'}]\",,31357,tt0114885,en,Waiting to Exhale,\"Cheated on, mistreated and stepped on, the women are holding their breath, waiting for the elusive \"\"good man\"\" to break a string of less-than-stellar lovers. Friends and confidants Vannah, Bernie, Glo and Robin talk it all out, determined to find a better way to breathe.\",3.859495,/16XOMpEaLWkrcPqSQqhTmeJuqQl.jpg,\"[{'name': 'Twentieth Century Fox Film Corporation', 'id': 306}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,81452156,127.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Friends are the people who let you be yourself... and never let you forget it.,Waiting to Exhale,False,6.1,34"

    movies_file=tmp_path/"movies.csv"
    
    with open(movies_file, 'w+') as wfile:
        wfile.write(f"{headers}\n{movie1}\n{movie2}\n{movie3}\n{movie4}")
    return movies_file

@pytest.fixture
def invalid_data_movies_file(tmp_path):
    headers="adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count"
    movies=[
        "100,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"1. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92"
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 13}, {'id': 35, 'name': 3.14}]\",,15602,tt0113228,en,Grumpier Old Men,\"2. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92"
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,SHOULDBEINT,tt0113228,en,Grumpier Old Men,\"3. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92"
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,100,en,Grumpier Old Men,\"4. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"6. Lorem ipsum some description\",SHOULDBEFLOAT,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"7. Lorem ipsum some description\",11.7129,100,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",  # dodać regex żeby wykrywał to jako ścieżkę
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"8. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995.12.22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"9. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995/12/22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"11. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,SHOULDBEFLOAT,SHOULDBEINT",
        
        "\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"12. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,,15602,tt0113228,en,Grumpier Old Men,\"13. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,tt0113228,en,Grumpier Old Men,\"14. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,en,Grumpier Old Men,\"15. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"17. Lorem ipsum some description\",/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"18. Lorem ipsum some description\",11.7129,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"19. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"20. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,False,6.5,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"21. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,92",
        "False,\"{'id': 119050, 'name': 'Grumpy Old Men Collection', 'poster_path': '/nLvUdqgPgm3F85NMCii9gVFUcet.jpg', 'backdrop_path': '/hypTnLot2z8wpFS7qwsQHW1uV8u.jpg'}\",0,\"[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]\",,15602,tt0113228,en,Grumpier Old Men,\"22. Lorem ipsum some description\",11.7129,/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg,\"[{'name': 'Warner Bros.', 'id': 6194}, {'name': 'Lancaster Gate', 'id': 19464}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-22,0,101.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,Still Yelling. Still Fighting. Still Ready for Love.,Grumpier Old Men,False,6.5",
    ]

    movies_file=tmp_path/"movies.csv"
    
    with open(movies_file, 'w+') as wfile:
        wfile.write(f"{headers}\n")
        for csvstr in movies:
            wfile.write(f"{csvstr}\n")
    return movies_file

def test_movies_read_correctly(common_movies_file):
    movies, _ = readMovies(common_movies_file)

    assert movies[0] == Movie(
        adult=False,
        genres=['Animation', 'Comedy', 'Family'],
        id=1,
        imdb_id="tt0114709",
        overview="Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
        popularity=21.946943,
        poster_path="/rhIRbceoE9lR4veEXuwCC2wARtG.jpg",
        release_date=datetime.date(1995,10,30),
        title="Toy Story",
        vote_average=7.7,
        vote_count=5415
    )
    assert movies[1]==Movie(
        adult=False,
        genres=['Adventure', 'Fantasy', 'Family'],
        id=2,
        imdb_id="tt0113497",
        overview="When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",
        popularity=17.015539,
        poster_path="/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg",
        release_date=datetime.date(1995,12,15),
        title="Jumanji",
        vote_average=6.9,
        vote_count=2413
    )
    assert movies[2]==Movie(
        adult=False,
        genres=['Romance', 'Comedy'],
        id=3,
        imdb_id="tt0113228",
        overview="A family wedding reignites the ancient feud between next-door neighbors and fishing buddies John and Max. Meanwhile, a sultry Italian divorcée opens a restaurant at the local bait shop, alarming the locals who worry she'll scare the fish away. But she's less interested in seafood than she is in cooking up a hot time with Max.",
        popularity=11.7129,
        poster_path="/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg",
        release_date=datetime.date(1995,12,22),
        title="Grumpier Old Men",
        vote_average=6.5,
        vote_count=92
    )
    assert movies[3]==Movie(
        adult=False,
        genres=['Comedy', 'Drama', 'Romance'],
        id=4,
        imdb_id="tt0114885",
        overview="Cheated on, mistreated and stepped on, the women are holding their breath, waiting for the elusive \"good man\" to break a string of less-than-stellar lovers. Friends and confidants Vannah, Bernie, Glo and Robin talk it all out, determined to find a better way to breathe.",
        popularity=3.859495,
        poster_path="/16XOMpEaLWkrcPqSQqhTmeJuqQl.jpg",
        release_date=datetime.date(1995,12,22),
        title="Waiting to Exhale",
        vote_average=6.1,
        vote_count=34
    )

def test_ids_are_mapped_correctly(common_movies_file):
    _, id_map = readMovies(common_movies_file)
    correctIdMap={862:1, 8844:2, 15602:3, 31357:4}
    assert id_map==correctIdMap

def test_return_None_when_data_are_invalid(invalid_data_movies_file):
    movies, _ =readMovies(invalid_data_movies_file)
    assert movies==[]