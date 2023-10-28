from plates import is_valid

def test_is_valid_len():
    assert is_valid('AB') == True
    assert is_valid('ABC123') == True
    assert is_valid('ABCA123') == False
    assert is_valid('ABAAA') == True
    assert is_valid('A') == False

def test_is_valid_mid():
    assert is_valid('AB123A') == False
    assert is_valid('AB123') == True

def test_is_valid_zero():
    assert is_valid('AB01') == False
    assert is_valid('AB10') == True

def test_is_valid_two_letter():
    assert is_valid('A') == False
    assert is_valid('A2') == False
    assert is_valid('1A') == False
    assert is_valid('11') == False

def test_is_valid_punc():
    assert is_valid('AB.') == False
    assert is_valid('AB!') == False
    assert is_valid('AB,') == False
    assert is_valid('AB ') == False

