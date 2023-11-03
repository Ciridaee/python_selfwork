from um import count
import sys


def main():
    testcase()
    sys.exit(1)


def testcase():
    assert count("hello um, how are um you um:")==3
    assert count("asfaf um, um um um:")==4
    assert count("Um")==1
    assert count("um?")==1
    assert count("sumo")==0