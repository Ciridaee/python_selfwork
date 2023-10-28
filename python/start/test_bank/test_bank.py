from bank import value

def test_value():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('Hello there') == 0
    assert value('hi') == 20
    assert value('Hi') == 20
    assert value('how are you') == 20
    assert value('whats up') == 100
    assert value('whats new') == 100