import pytest

@pytest.fixture(scope="session", autouse=True)
def auto_session_resource(request):
    """ Auto session resource fixture
    """
    print("auto_session_resource_setup")
    def auto_session_resource_teardown():
        print("auto_session_resource_teardown")
    request.addfinalizer(auto_session_resource_teardown)
    
@pytest.fixture(scope="session")
def manually_session_resource(request):
    """ Manual set session resource fixture
    """
    print("manually_session_resource_setup")
    def manually_session_resource_teardown():
        print("manually_session_resource_teardown")
    request.addfinalizer(manually_session_resource_teardown)
    
@pytest.fixture(scope="function")
def function_resource(request):
    """ Function resource fixture
    """
    print("function_resource_setup")
    def function_resource_teardown():
        print("function_resource_teardown")
    request.addfinalizer(function_resource_teardown)