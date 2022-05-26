import pytest

def f():
    print(1/0)

def test_exception():
    with pytest.raises(ZeroDivisionError):
        f()