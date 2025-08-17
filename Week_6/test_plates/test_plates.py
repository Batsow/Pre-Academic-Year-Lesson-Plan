from plates import is_valid

def test_invalid_length():
    invalid_plates = ["A", "ABCDEFG", ""]
    for plate in invalid_plates:
        assert is_valid(plate) == False
    
def test_valid_length():
    valid_plates = ["CS", "CS50", "CS101", "ABC321"]
    for plate in valid_plates:
        assert is_valid(plate) == True
    
def test_start_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("05CS") == False
    assert is_valid("C550") == False
    
def test_alphanumeric():
    assert is_valid("CS*'90") == False
    assert is_valid("AB 12") == False
    assert is_valid("CS50") == True

def test_number_rules():
    assert is_valid("CS05") == False
    assert is_valid("CS5T") == False
    assert is_valid("CS50") == True
    
    
    