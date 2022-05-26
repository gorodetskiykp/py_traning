import pytest

pytestmark = pytest.mark.level1
 
def test_1():
    print("test_1")
    
@pytest.mark.level2
class TestClass:
    def test_2(self):
        print("test_2")
    @pytest.mark.level3
    def test_3(self):
        print("test_3")