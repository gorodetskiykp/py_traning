import pytest
 
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 11])
def test_cross_params(x, y):
    print("x: {0}, y: {1}".format(x, y))
    assert True