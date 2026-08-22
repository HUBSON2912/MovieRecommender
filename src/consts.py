import pathlib as pth

DATA_DIR=pth.Path("./data")

MOVIES:pth.Path = pth.Path("./data/movies_metadata.csv")
RATINGS:pth.Path = pth.Path("./data/ratings_small.csv")  # "ratings.csv"
LINKS:pth.Path = pth.Path("./data/links_small.csv")  #"links.csv"
KEYWORDS:pth.Path = pth.Path("./data/keywords.csv")
CREDITS:pth.Path = pth.Path("./data/credits.csv")

REQURED_DATA:list[str]=[MOVIES.name, RATINGS.name, LINKS.name, KEYWORDS.name, CREDITS.name]