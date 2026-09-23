import pytest
from back.src.misc import *


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

def test_strToDate_year_zero():
    with pytest.raises(ValueError):
        strToDate("0-5-19")

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

# ===== misc.py strToListOfGenre FUNCTION =====

@pytest.mark.parametrize("csvPartString,expected",[
    ("[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",['Animation', 'Comedy', 'Family']),
    ("[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",['Adventure', 'Fantasy', 'Family']),
    ("[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}]",['Romance', 'Comedy']),
    ("[{'id': 35, 'name': 'Comedy'}, {'id': 18, 'name': 'Drama'}, {'id': 10749, 'name': 'Romance'}]",['Comedy', 'Drama', 'Romance']),
])
def test_strToListOfGenre_general_usage(csvPartString,expected):
    assert strToListOfGenre(csvPartString)==expected

@pytest.mark.parametrize("csvPartString,expected",[
    ("[{'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'name': 'Family'}]",['Animation', 'Comedy', 'Family']),
    ("[{'id': 12, 'name': 'Adventure'}, {'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",['Adventure', 'Fantasy', 'Family']),
    ("[{'id': 10749, 'name': 'Romance'}, {'name': 'Comedy'}]",['Romance', 'Comedy']),
    ("[{'id': 35, 'name': 'Comedy'}, {'name': 'Drama'}, {'id': 10749, 'name': 'Romance'}]",['Comedy', 'Drama', 'Romance']),
])
def test_strToListOfGenre_missing_id(csvPartString,expected):
        assert strToListOfGenre(csvPartString)==expected

@pytest.mark.parametrize("csvString", [
    "[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751}]",
    "[{'id': 12}, {'id': 14}, {'id': 10751, 'name': 'Family'}]",
    "[{'id': 10749}, {'id': 35, 'name': 'Comedy'}]",
    "[{'id': 35, 'name': 'Comedy'}, {'id': 18}, {'id': 10749, 'name': 'Romance'}]",
])
def test_strToListOfGenre_doesnt_have_name(csvString):
    with pytest.raises(KeyError):
        strToListOfGenre(csvString)

@pytest.mark.parametrize("csvPartString,expected",[
    ("[{'id': 16, 'name': 'Animation', 'random': 423}, {'id': 35,'lorem': 'Comedy', 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",['Animation', 'Comedy', 'Family']),
    ("[{'id': 12, 'name': 'Adventure', 'magyar': 632, 'mako': true}, {'id': 14, 'name': 'Fantasy', 'ipsum': 4.34}, {'id': 10751, 'name': 'Family'}]",['Adventure', 'Fantasy', 'Family']),
    ("[{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy', 'add1': 6}]",['Romance', 'Comedy']),
    ("[{'id': 35, 'name': 'Comedy', 'math':'trigonometry', 'physics':'dynamic'}, {'id': 18, 'addit1':null, 'name': 'Drama'}, {'id': 10749, 'name': 'Romance'}]",['Comedy', 'Drama', 'Romance']),
])
def test_strToListOfGenre_has_additional_keys(csvPartString,expected):
    assert strToListOfGenre(csvPartString)==expected
        
@pytest.mark.parametrize("csvString", [
    "[{'id': 16, 'name': 3.14}, {'id': 35, 'name': 100}, {'id': 10751, 'name': 'Family'}]",
    "[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': True}, {'id': 10751, 'name': []}]",
    "[{'id': 10749, 'name': 100}, {'id': 35, 'name': 'Comedy'}]",
    "[{'id': 35, 'name': 100}, {'id': 18, 'name': null}, {'id': 10749, 'name': 3.14}]",
])
def test_strToListOfGenre_name_is_wrong_type(csvString):
    with pytest.raises(ValueError):
        strToListOfGenre(csvString)