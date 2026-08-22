import typing
import os
import pathlib

REQURED_DATA:list[str]=['movies_metadata.csv', 'ratings.csv', 'ratings_small.csv', 'links_small.csv', 'keywords.csv', 'links.csv', 'credits.csv']
DATA_DIR=pathlib.Path("./data")

def areDataComplete() -> bool:
    filesInData:list[str] = os.listdir(DATA_DIR)
    for file in REQURED_DATA:
        if not (file in filesInData):
            return False
    return True


if not areDataComplete():
    raise FileNotFoundError("Missing data file. Try to download the data .zip package.")

