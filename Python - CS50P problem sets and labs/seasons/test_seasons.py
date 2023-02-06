from seasons import Racun
import datetime
import inflect
import pytest

def test_format():
    racuni = Racun()
    racuni.rodj = "2021-7-2"
    racuni.kraj = datetime.date(2022,7,2)
    assert racuni.racunica() == 525600


def test_format1():
    racuni = Racun()
    racuni.rodj = "2020-7-2"
    racuni.kraj = datetime.date(2022,7,2)
    assert racuni.racunica() == 1051200

def test_krajnje():
    p = inflect.engine()
    racun = Racun()
    racun.rodj = "2020-7-2"
    racun.kraj = datetime.date(2022,7,2)
    racun.racunica()
    assert str(racun) == 'One million, fifty-one thousand, two hundred minutes'

def test_krajnje1():
    p = inflect.engine()
    racun = Racun()
    racun.rodj = "2021-7-2"
    racun.kraj = datetime.date(2022,7,2)
    racun.racunica()
    assert str(racun) == 'Five hundred twenty-five thousand, six hundred minutes'

def test_input():
    racuni = Racun()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        racuni.rodj="2021/7/2"
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'Invalid date'
