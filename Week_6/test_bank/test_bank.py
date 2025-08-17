from bank import value

def test_startswith_hello():
    assert value("hello") == 0

def test_startswith_h():
    assert value("h") == 20

def test_startswith_any_word():
    assert value("sure") == 100

def test_case_insensitivity():
    assert value("HEllo") == 0

def test_entire_phrase():
    assert value("hello there") == 0