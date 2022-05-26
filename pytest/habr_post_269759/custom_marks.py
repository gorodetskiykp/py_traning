import pytest
 
def test_1():
    print("test_1")
    
@pytest.mark.critital_tests
def test_2():
    print("test_2")
    
def test_3():
    print("test_3")