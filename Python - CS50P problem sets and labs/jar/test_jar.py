from jar import Jar
import pytest

def test_dep():
    rac = Jar()
    print(rac._capacity)
    with pytest.raises(ValueError) as pytest_wrapped_e:
        rac.deposit(rac._capacity+1)
    assert pytest_wrapped_e.type == ValueError

def test_wid():
    rac = Jar()
    with pytest.raises(ValueError) as pytest_wrapped_e:
        rac.withdraw(1)
    assert pytest_wrapped_e.type == ValueError

def test_racun():
    rac = Jar()
    rac.deposit(5)
    rac.withdraw(2)
    assert str(rac) == '🍪🍪🍪'

def test_init():
    rac = Jar()
test_dep()