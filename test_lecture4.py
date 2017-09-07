import pytest

def add(a, b):
    c = a + b
    if c < 0:
        return 0
    else:
        return c

def test_intAdd():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(-1,-2) == 0

def test_doubleAdd():
    assert add(.001,1.11) == 1.111
    assert add(-0.2,0.1) == 0
    assert add(1.33,1.67) == 3
