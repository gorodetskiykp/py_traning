import pytest
 
@pytest.fixture(scope="function")
def resource_setup(request):
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)
    
def test_1(resource_setup):
    assert True
 
class TestClass():
    def test_2(self, resource_setup):
        assert True
