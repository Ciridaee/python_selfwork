from twttr import shorten
import sys

def main():
    test_letter()
    test_numbers()
    test_punctuation()


def test_letter():
    assert shorten('twitter')=='twttr'
    assert shorten('TWITTER')=='TWTTR'

def test_numbers():
    assert shorten('10')=='10'

def test_punctuation():
    assert shorten('!?.,')=='!?.,'


    


if __name__ == "__main__":
    main()