from twttr import shorten

def test_shorten():
    assert shorten ("casa") == "cs"
    assert shorten ("Shorten") == "Shrtn"
    assert shorten ("cs50!") == "cs50!"
    assert shorten("SAEIOUS") == "SS"