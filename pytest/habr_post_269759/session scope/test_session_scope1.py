import pytest
 
def test_1_that_does_not_need_session_resource():
    print("test_1_that_does_not_need_session_resource")

def test_2_that_does(manually_session_resource):
    print("test_2_that_does")