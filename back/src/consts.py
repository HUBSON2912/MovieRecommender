import pathlib as pth

DATA_DIR=pth.Path("./back/data")
SAVE_DIR=pth.Path("./back/saved")

MOVIES:pth.Path = pth.Path("./back/data/movies_metadata.csv")
RATINGS:pth.Path = pth.Path("./back/data/ratings_small.csv")  # "ratings.csv"
LINKS:pth.Path = pth.Path("./back/data/links_small.csv")  #"links.csv"
KEYWORDS:pth.Path = pth.Path("./back/data/keywords.csv")
CREDITS:pth.Path = pth.Path("./back/data/credits.csv")

REQURED_DATA:list[str]=[MOVIES.name, RATINGS.name, LINKS.name, KEYWORDS.name, CREDITS.name]

SECOND_DIMENTIONS=150