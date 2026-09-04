import pathlib as pth

# directories
DATA_DIR=pth.Path("./back/data")
SAVE_DIR=pth.Path("./back/saved")

# data files
MOVIES:pth.Path = pth.Path(DATA_DIR / "movies_metadata.csv")
RATINGS:pth.Path = pth.Path(DATA_DIR / "ratings_small.csv")  # "ratings.csv"
LINKS:pth.Path = pth.Path(DATA_DIR / "links_small.csv")  #"links.csv"
KEYWORDS:pth.Path = pth.Path(DATA_DIR / "keywords.csv")
CREDITS:pth.Path = pth.Path(DATA_DIR / "credits.csv")

REQURED_DATA:list[str]=[MOVIES.name, RATINGS.name, LINKS.name, KEYWORDS.name, CREDITS.name]

# ai model consts
SECOND_DIMENTIONS=150

# endpoints consts
RETURN_MOVIES = 15  # how many movies you return at once