import twttr

def testiranjetw():
    assert twttr.shorten('Twitter') == 'Twttr'
    assert twttr.shorten('What\'s your name?') == 'Wht\'s yr nm?'
    assert twttr.shorten('CS50') == 'CS50'
    assert twttr.shorten('samolagano') == 'smlgn'
    assert twttr.shorten('SAMOPOLAKO') == 'SMPLK'
