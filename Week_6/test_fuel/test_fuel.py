from fuel import convert, gauge
import pytest 

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error_numerator_greater():
    with pytest.raises(ValueError):
        convert("2/1")
        
def test_value_error_negative():
    with pytest.raises(ValueError):
        convert("-1/4")
        
def test_valid_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    
def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    
    
