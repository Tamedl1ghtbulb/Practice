import bank

def test_bank():
    assert str(bank.value('hello')) == '0'
    assert str(bank.value('HELLO')) == '0'
    assert str(bank.value('Hawqoqwdqw54')) == '20'
    assert str(bank.value('HASOAWQ')) == '20'
    assert str(bank.value('tass212')) == '100'
    assert str(bank.value('AASQO')) == '100'