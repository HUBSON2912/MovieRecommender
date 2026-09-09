import re
from pathlib import Path

def hasBinExtentnion(filename: str|Path)->bool:
    if isinstance(filename, Path):
        return filename.match("*.bin")
    else:
        REGEX_BIN_EXT=r".*\.bin$"
        return re.match(REGEX_BIN_EXT, filename)