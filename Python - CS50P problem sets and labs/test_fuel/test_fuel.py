import fuel
import pytest

def test_nesto():
    assert fuel.gauge((80))== '80%'
    assert fuel.gauge((20)) == '20%'
    assert fuel.gauge((99)) == 'F'
    assert fuel.gauge((1)) == 'E'

def test_jako():
    assert fuel.convert('4/5') == 80
    assert fuel.convert('1/10') == 10
    assert fuel.convert('7/10') == 70

def test_greske():
    with pytest.raises(ValueError):
        fuel.convert('4.3/5')
    with pytest.raises(ZeroDivisionError):
        fuel.convert('1/0')