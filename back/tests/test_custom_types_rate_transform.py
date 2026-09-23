import pytest
from back.src.custom_types import Rate

@pytest.mark.parametrize("id,rate,expected",[
    (1,1.0,Rate(movieId=1, rate=1.0)),
    (234,7.4,Rate(movieId=234, rate=7.4)),
    (42,5.0,Rate(movieId=42, rate=5.0)),
    (67,8.5,Rate(movieId=67, rate=8.5)),
    (654,6.12,Rate(movieId=654, rate=6.12)),
    (32165,1.7,Rate(movieId=32165, rate=1.7)),
    (6921,1.726,Rate(movieId=6921, rate=1.726)),
    (3851,9.5,Rate(movieId=3851, rate=9.5)),
    (85612,4,Rate(movieId=85612, rate=4)),
    (3584,1.2,Rate(movieId=3584, rate=1.2)),
    (6734,10,Rate(movieId=6734, rate=10)),
    (1658,3.14,Rate(movieId=1658, rate=3.14)),
])
def test_common_usage(id:int,rate:float,expected:Rate):
    rateDictionary={"movieId": id, "rate": rate}
    assert Rate.transform(rateDictionary)==expected

@pytest.mark.parametrize("id,rate",[
    (-3,1.3),
    (3,-1.3),
])
def test_negative_id_or_rate(id:int,rate:float):
    with pytest.raises(ValueError):
        rateDictionary={"movieId": id, "rate": rate}
        Rate.transform(rateDictionary)

@pytest.mark.parametrize("id,rate",[
    (12,15.0),
    (1,10.001),
])
def test_rate_too_big(id:int,rate:float):
    with pytest.raises(ValueError):
        rateDictionary={"movieId": id, "rate": rate}
        Rate.transform(rateDictionary)