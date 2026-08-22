import csv
import os
from consts import DATA_DIR, REQURED_DATA, MOVIES

def areDataComplete() -> bool:
    filesInData:list[str] = os.listdir(DATA_DIR)
    for file in REQURED_DATA:
        if not (file in filesInData):
            return False
    return True


if __name__=="__main__":
    if not areDataComplete():
        raise FileNotFoundError("Missing data file. Try to download the data .zip package.")

    with open(MOVIES) as file:
        reader=list(csv.reader(file))
        reader=reader[1:] # skip headers
        
        for row in reader:
            if i>=15:
                break
            print(row)
            i+=1