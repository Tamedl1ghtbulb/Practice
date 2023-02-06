from numb3rs import validate

def test_validate():
    assert(validate('255.1.1.3')) == True
    assert(validate('275.6.41.5')) == False
    assert(validate('1.2.3.1000')) == False
    assert(validate('kuce')) == False
    assert(validate('samo.jako.jace.malo'))== False
    assert(validate('1.1.1.1')) == True
    assert(validate('1.275.1.1')) == False
    assert(validate('2.2.275.3')) == False
    assert(validate('3.78.14.275'))== False