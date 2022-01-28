from unittest import result
# test Github Action nr 3

def szescian(liczba):
    liczba = liczba ** 3
    return liczba

def test1_szescian():
    a = 7
    result = szescian(a)
    assert result == 343

def test2_szescian():
    a = -3
    result = szescian(a)
    assert result == -27

# Zadanie 2
def wieksza(a,b):
    if a >= b:
        return a
    else:
        return b

def test1_wieksza():
    a = 10
    b = 20
    result = wieksza(a,b)
    assert result == b

def test2_wieksza():
    a = 30
    b = 20
    result = wieksza(a,b)
    assert result == a

def test3_wieksza():
    a = 20
    b = 20
    result = wieksza(a,b)
    assert result == 20
