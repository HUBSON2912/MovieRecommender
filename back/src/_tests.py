import pytest
import datetime
from pathlib import Path
# from handledata import readMovies
from misc import hasBinExtension, strToDate
from custom_types import Movie

# ===== misc.py hasBinExtension FUNCTION =====

@pytest.mark.parametrize("filename,expected", [
    ("file_name.bin", True), 
    ("file_name.mp3", False), 
    ("file_name.mp3.bin", True), 
    ("file_name.bin.mp3", False), 
    (Path("file_name.bin"), True),
    (Path("filename.mp3"), False),
    (Path("filename.mp3.bin"), True),
    (Path("filename.bin.mp3"), False),
])
def test_hasBinExtension_common_usage(filename,expected):
    assert hasBinExtension(filename) == expected

@pytest.mark.parametrize("filename,expected", [
    (".bin", True), 
    (Path(".bin"), True),
])
def test_hasBinExtension_filename_with_only_extension(filename,expected):
    assert hasBinExtension(filename) == expected

@pytest.mark.parametrize("filename",[
    (1,), 
    (3.12,), 
    (True,), 
    (["file.bin"],), 
    (-1,)
])
def test_hasBinExtension_wrong_input_types(filename,):
    with pytest.raises(TypeError):
        hasBinExtension(filename)

# ===== misc.py strToDate FUNCTION =====

@pytest.mark.parametrize("dateString,expected", [
    ("1990-1-12", datetime.date(1990,1,12)), 
    ("2000-2-15", datetime.date(2000,2,15)), 
    ("1970-03-03", datetime.date(1970,3,3)), 
    ("2021-4-30", datetime.date(2021,4,30)), 
    ("2026-06-11", datetime.date(2026,6,11)), 
    ("1983-7-21", datetime.date(1983,7,21)), 
    ("1981-12-13", datetime.date(1981,12,13)), 
    ("2013-01-5", datetime.date(2013,1,5)), 
])
def test_strToDate_common_usage(dateString,expected):
    assert strToDate(dateString) == expected

@pytest.mark.parametrize("dateString,expected", [
    ("2130-1-12", datetime.date(2130,1,12)), 
    ("3412-2-15", datetime.date(3412,2,15)), 
    ("2210-4-30", datetime.date(2210,4,30)), 
    ("2045-6-11", datetime.date(2045,6,11))
])
def test_strToDate_future_date(dateString,expected):
    assert strToDate(dateString) == expected

@pytest.mark.parametrize("dateString,expected", [
    ("1960-1-12", datetime.date(1960,1,12)), 
    ("1900-2-15", datetime.date(1900,2,15)), 
    ("1624-3-3", datetime.date(1624,3,3)), 
    ("1354-4-30", datetime.date(1354,4,30)), 
    ("2-6-11", datetime.date(2,6,11))
])
def test_strToDate_before_unix_era(dateString,expected):
    assert strToDate(dateString) == expected

def test_strToDate_year_one():
    assert strToDate("1-5-19") == datetime.date(1,5,19)

@pytest.mark.parametrize("dateString,expected", [
    ("2024-2-29", datetime.date(2024,2,29)), 
    ("2020-2-29", datetime.date(2020,2,29)), 
    ("1980-2-29", datetime.date(1980,2,29)), 
    ("1996-2-29", datetime.date(1996,2,29)), 
])
def test_strToDate_leap_year(dateString, expected):
    assert strToDate(dateString) == expected

@pytest.mark.parametrize("dateString", [
    "2026-2-29",
    "2020-03-32",
    "1980-04-31",
    "1996-15-12",
])
def test_strToDate_date_that_doesnt_exist(dateString):
    with pytest.raises(ValueError):
        strToDate(dateString)

@pytest.mark.parametrize("dateString", [
    "1970.03.03", 
    "2021/4/30", 
    "2026 06 11", 
    "1983:7:21", 
    "1983;7;21", 
])
def test_strToDate_wrong_separator(dateString):
    with pytest.raises(ValueError):
        strToDate(dateString)

@pytest.mark.parametrize("dateString", [
    "-753-12-3",
    "-2500-1-1",
    "-2500-1-1BC",
    "-2500-1-1 BC",
    "-812-3-9",
    "812BC-3-9",
])
def test_strToDate_before_christ(dateString):
    # strToDate doesn't support BC years
    with pytest.raises(ValueError):
        strToDate(dateString)

# ===== handledata.py readMovies FUNCTION =====
# @pytest.fixture(scope="session")
# def movies_file(tmp_path_factory):
#     headers="adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count"
#     movie1="False,\"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}\",30000000,\"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]\",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,\"some really long description\",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,\"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-10-30,373554033,81.0,\"[{'iso_639_1': 'en', 'name': 'English'}]\",Released,,Toy Story,False,7.7,5415"
#     movie2="False,,65000000,\"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]\",,8844,tt0113497,en,Jumanji,\"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.\",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,\"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]\",\"[{'iso_3166_1': 'US', 'name': 'United States of America'}]\",1995-12-15,262797249,104.0,\"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]\",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413"
#     file:Path=tmp_path_factory.mktemp("test_data_dir")/"movies.csv"
#     file.write_text(f"{headers}\n{movie1}\n{movie2}")
#     return file

# def test_readMovies(movies_file):
#     mov=readMovies(movies_file)
#     assert False


# ===== MOVIE.TRANSFORM FUNCTION =====

def test_all_data_are_valid():
    in_dict={
        'adult': 'False', 
        'belongs_to_collection': "{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}", 
        'budget': '30000000', 
        'genres': "[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name 'Comedy'}, {'id': 10751, 'name': 'Family'}]", 
        'homepage': 'http://toystory.disney.com/toy-story', 
        'id': '862', 
        'imdb_id': 'tt0114709', 
        'original_language': 'en', 
        'original_title': 'Toy Story', 
        'overview': "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.", 
        'popularity': '21.946943', 
        'poster_path': '/rhIRbceoE9lR4veEXuwCC2wARtG.jpg', 
        'production_companies': "[{'name': 'Pixar Animation Studios', 'id': 3}]", 
        'production_countries': "[{'iso_3166_1': 'US', 'name': 'United States of America'}]", 
        'release_date': '1995-10-30', 
        'revenue': '373554033', 
        'runtime': '81.0', 
        'spoken_languages': "[{'iso_639_1': 'en', 'name': 'English'}]", 
        'status': 'Released', 
        'tagline': '', 
        'title': 'Toy Story', 'video': 'False', 
        'vote_average': '7.7', 
        'vote_count': '5415'
    }
    correct=Movie(adult=False,
        genres=['Animation', 'Comedy', 'Family'],
        id=862,
        imdb_id="tt0114709",
        overview="Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
        popularity=21.946943,
        poster_path="/rhIRbceoE9lR4veEXuwCC2wARtG.jpg",
        release_date=datetime.date(1995,10,30),
        title="Toy Story",
        vote_average=7.7,
        vote_count=5415
    )
    assert Movie.transform(in_dict) == correct

def test_useless_data_are_missing():
    in_dict = {
        'adult': 'False', 
        'belongs_to_collection': "{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}", 
        # 'budget': '30000000', 
        'genres': "[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]", 
        'homepage': 'http://toystory.disney.com/toy-story', 
        'id': '862', 
        'imdb_id': 'tt0114709', 
        'original_language': 'en', 
        'original_title': 'Toy Story', 
        'overview': "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.", 
        'popularity': '21.946943', 
        'poster_path': '/rhIRbceoE9lR4veEXuwCC2wARtG.jpg', 
        'production_companies': "[{'name': 'Pixar Animation Studios', 'id': 3}]", 
        'production_countries': "[{'iso_3166_1': 'US', 'name': 'United States of America'}]", 
        'release_date': '1995-10-30', 
        'revenue': '373554033', 
        'runtime': '81.0', 
        'spoken_languages': "[{'iso_639_1': 'en', 'name': 'English'}]", 
        'status': 'Released', 
        'tagline': '', 
        'title': 'Toy Story', 
        'video': 'False', 
        'vote_average': '7.7', 
        'vote_count': '5415'
    }
    correct = Movie(adult=False,
        genres=['Animation', 'Comedy', 'Family'],
        id=862,
        imdb_id="tt0114709",
        overview="Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
        popularity=21.946943,
        poster_path="/rhIRbceoE9lR4veEXuwCC2wARtG.jpg",
        release_date=datetime.date(1995,10,30),
        title="Toy Story",
        vote_average=7.7,
        vote_count=5415
    )
    assert Movie.transform(in_dict) == correct

def test_important_data_are_missing():
    in_dict = {
        'adult': 'False', 
        'belongs_to_collection': "{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}", 
        'budget': '30000000', 
        # 'genres': "[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]", 
        'homepage': 'http://toystory.disney.com/toy-story', 
        'id': '862', 
        'imdb_id': 'tt0114709', 
        'original_language': 'en', 
        'original_title': 'Toy Story', 
        'overview': "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.", 
        'popularity': '21.946943', 
        'poster_path': '/rhIRbceoE9lR4veEXuwCC2wARtG.jpg', 
        'production_companies': "[{'name': 'Pixar Animation Studios', 'id': 3}]", 
        'production_countries': "[{'iso_3166_1': 'US', 'name': 'United States of America'}]", 
        'release_date': '1995-10-30', 
        'revenue': '373554033', 
        'runtime': '81.0', 
        'spoken_languages': "[{'iso_639_1': 'en', 'name': 'English'}]", 
        'status': 'Released', 
        'tagline': '', 
        'title': 'Toy Story', 
        'video': 'False', 
        'vote_average': '7.7', 
        'vote_count': '5415'
    }
    assert Movie.transform(in_dict) is None

def test_data_wrong_type():
    in_dict = {
        'adult': 'False', 
        'belongs_to_collection': "{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}", 
        'budget': '30000000', 
        'genres': "[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]", 
        'homepage': 'http://toystory.disney.com/toy-story', 
        'id': "LOREM IPSUM", # wrong type
        'imdb_id': 'tt0114709', 
        'original_language': 'en', 
        'original_title': 'Toy Story', 
        'overview': "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.", 
        'popularity': '21.946943', 
        'poster_path': '/rhIRbceoE9lR4veEXuwCC2wARtG.jpg', 
        'production_companies': "[{'name': 'Pixar Animation Studios', 'id': 3}]", 
        'production_countries': "[{'iso_3166_1': 'US', 'name': 'United States of America'}]", 
        'release_date': '1995-10-30', 
        'revenue': '373554033', 
        'runtime': '81.0', 
        'spoken_languages': "[{'iso_639_1': 'en', 'name': 'English'}]", 
        'status': 'Released', 
        'tagline': '', 
        'title': 'Toy Story', 
        'video': 'False', 
        'vote_average': '7.7', 
        'vote_count': '5415'
    }
    assert Movie.transform(in_dict) is None

if __name__=="__main__":
    correct = Movie(adult=False,
            genres=['Animation', 'Comedy', 'Family'],
            id=862,
            imdb_id="tt0114709",
            overview="Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
            popularity=21.946943,
            poster_path="/rhIRbceoE9lR4veEXuwCC2wARtG.jpg",
            release_date=datetime.date(1995,10,30),
            title="Toy Story",
            vote_average=7.7,
            vote_count=5415
        )
    print(correct)