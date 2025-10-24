from seasons import validate_birthday


def test_Validate_birthday():
    assert validate_birthday("1990-10-10") == ("1990", "10", "10")
    assert validate_birthday("August 24, 1989")==None
    assert validate_birthday("1995-6-9")==None
