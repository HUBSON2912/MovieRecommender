import datetime
import json
import re
from pathlib import Path

def hasBinExtension(filename: str|Path)->bool:
    if isinstance(filename, Path):
        return filename.match("*.bin")
    else:
        REGEX_BIN_EXT=r".*\.bin$"
        return bool(re.match(REGEX_BIN_EXT, filename))

def strToDate(str:str) -> datetime.date:
    params=str.split("-")
    y,m,d=list(map(int,params))
    return datetime.date(y, m, d)

def strToListOfGenre(csvString:str)->list[str]:
    csvString=csvString.replace("'", "\"")
    genres=json.loads(csvString)
    return list(map(lambda x: x["name"], genres))