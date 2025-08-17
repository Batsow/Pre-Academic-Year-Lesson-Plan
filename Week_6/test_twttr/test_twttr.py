from twttr import shorten

def test_shorten_both_cases():
    assert shorten("Twitter") == "Twttr" 
    
def test_all_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    
def test_all_lowercase():
    assert shorten("twitter") == "twttr"

def test_numbers():
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("let's set up my twitter.") == "lt's st p my twttr."
    