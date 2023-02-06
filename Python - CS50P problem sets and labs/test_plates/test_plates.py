from plates import is_valid

def test_plates():
    assert is_valid('CS50') == True
    assert is_valid('A12412') == False
    assert is_valid('AB1587758') == False
    assert is_valid('AB45S1') == False
    assert is_valid('AB./12') == False
    assert is_valid('BA0TT478') == False