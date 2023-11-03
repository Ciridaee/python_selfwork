from numb3rs import validate

def main():
    test_valid()


def test_valid():
    assert validate("1.1.2.1") == True
    assert validate("1.1.2.256") == False
    assert validate("1.1.2") == False
    assert validate("1.1.1.1.1") == False




if "__name__" == "__main__":
    main()