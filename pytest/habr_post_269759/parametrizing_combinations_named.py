import pytest
 
def idfn_x(val):
    return "x=({0})".format(str(val))
    
def idfn_y(val):
    return "y=({0})".format(str(val))
 
@pytest.mark.parametrize("x", [-1, 2], ids=idfn_x)
@pytest.mark.parametrize("y", [-10, 11], ids=idfn_y)
def test_cross_params(x, y):
    print("x: {0}, y: {1}".format(x, y))
    assert True
    
@pytest.mark.parametrize("x", [-1, 2], ids=["negative x", "positive y"])
@pytest.mark.parametrize("y", [-10, 11], ids=["negative y", "positive y"])
def test_cross_params_2(x, y):
    print("x: {0}, y: {1}".format(x, y))
    assert True