import pytest


@pytest.fixture()  # scope = 'function* | cls | module |session'
def resource_setup(request):
    print('resource_setup')

    def resource_teardown():
        print('resource_teardown')

    request.addfinalizer(resource_teardown)  # teardown


# @pytest.yield_fixture()
# def resource_setup():
#     print("resource_setup")
#     yield
#     print("resource_teardown")


# autouse=True - для всех функций
@pytest.fixture(scope="function", autouse=True)
def another_resource_setup_with_autouse(request):
    print("another_resource_setup_with_autouse")
    def resource_teardown():
        print("another_resource_teardown_with_autouse")
    request.addfinalizer(resource_teardown)


def test1_that_needs_resource(resource_setup):
    print('test1_that_needs_resource')


def test2_that_does_not():
    print('test2_that_does_not')


@pytest.mark.usefixtures("resource_setup")
def test3_that_does_again():
    print('test3_that_does_again')
