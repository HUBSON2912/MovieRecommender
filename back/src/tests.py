import unittest
import datetime
from custom_types import Movie

class MovieTransformTester(unittest.TestCase):
    def test_all_data_are_valid(self):
        in_dict={
            'adult': 'False', 
            'belongs_to_collection': "{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}", 
            'budget': '30000000', 
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
        self.assertEqual(Movie.transform(in_dict), correct)

    def test_useless_data_are_missing(self):
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
        self.assertEqual(Movie.transform(in_dict), correct)

    def test_important_data_are_missing(self):
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
        correct = None
        self.assertIs(Movie.transform(in_dict), correct)

    def test_data_wrong_type(self):
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
        correct = None
        self.assertIs(Movie.transform(in_dict), correct)  


if __name__=="__main__":
    unittest.main()