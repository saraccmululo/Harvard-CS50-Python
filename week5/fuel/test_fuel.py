from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("4/5") == 80
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_convert_invalid():
        # non-integer input
    with pytest.raises(ValueError):
        convert("dog/cat")
    # more than one slash
    with pytest.raises(ValueError):
        convert("1/2/3")
    # numerator > denominator
    with pytest.raises(ValueError):
        convert("5/4")
    # negative numerator
    with pytest.raises(ValueError):
        convert("-1/2")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(0)=="E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100)=="F"
