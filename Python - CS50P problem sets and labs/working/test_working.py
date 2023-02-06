from working import convert
import pytest

def test_convert():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('7:00 AM to 8:00 PM') == '07:00 to 20:00'
    assert convert('11 PM to 7 AM') == '23:00 to 07:00'
def test_er():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
