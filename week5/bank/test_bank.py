from bank import value

def test_value():
    assert value("hello")==0
    assert value("hi")==20
    assert value("whats's up?")==100
    assert value("Hello")==0
    assert value("hello, Newman")==0
    assert value("123")==100


