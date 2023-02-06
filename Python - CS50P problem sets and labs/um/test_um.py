from um import count

def test_1():
    assert count('Um popusis mi umkurac') == 1
def test_2():
    assert count('um yummy um um') == 3
def test_3():
    assert count('samojako') == 0