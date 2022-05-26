import pytest

@pytest.mark.parametrize(("x", "expected"), [
    (1,2),
    pytest.mark.critical((2,3)),
    (3,4)
])
def test_inc(x, expected):
    print(x, "+ 1 = ", expected)
    assert x + 1 == expected