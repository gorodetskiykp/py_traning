import pytest
 
@pytest.fixture()
def fixture1(request, fixture2):
    print("fixture1")
    
@pytest.fixture()
def fixture2(request, fixture3):
    print("fixture2")
    
@pytest.fixture()
def fixture3(request):
    print("fixture3")
    
def test_1(fixture1):
    print("test_1")
 
def test_2(fixture2):
    print("test_2")