import pytest
 
def strange_string_func(str):
    if len(str) > 5:
        return str + "?"
    elif len(str) < 5:
        return str + "!"
    else:
        return str + "."
 
@pytest.fixture(scope="function", params=[
("abcdefg", "abcdefg?"),
("abc", "abc!"),
("abcde", "abcde.")
])
def param_test(request):
    return request.param
    
def test_strange_string_func(param_test):
    (input, expected_output) = param_test
    result = strange_string_func(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output