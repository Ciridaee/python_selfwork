from fuel import convert,gauge
import pytest

def main():
    test_control()
    test_zero()
    test_string()

def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert('1/0')

def test_string():
    with pytest.raises(ValueError):
        assert convert('a/b')

def test_control():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('1/1') == 100 and gauge(100) == 'F'
    assert convert('99/100') == 99 and gauge(99) == 'F'


if __name__ == "__main__":
    main()