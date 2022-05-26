import pytest
 
@pytest.fixture()
def fixture1(request):
    print("fixture1")
    
@pytest.fixture()
def fixture2(request):
    print("fixture2")
    
@pytest.fixture()
def fixture3(request):
    print("fixture3")
    
def test_1(fixture1, fixture2):
    print("test_1")
 
def test_2(fixture1, fixture2, fixture3):
    print("test_2")