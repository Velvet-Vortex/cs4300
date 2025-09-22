import pytest
from src.task2 import integer_addition, float_multiplication, string_concatenation, boolean_operation

class TestIntegerAddition:
    # Use parameterized testing to run through multiple cases of data types, expect an integer
    testdata= [
        (10, 110),
        (10435, 10535),
        (10.0, "Error: argument of type integer expected"),
        ("string", "Error: argument of type integer expected"),
        (True, "Error: argument of type integer expected")
    ]

    @pytest.mark.parametrize("num,expected", testdata)
    def test_int_addition(self, num, expected):
        result = integer_addition(num)
        assert result == expected

class TestFloatMultiplication:
    # Use parameterized testing to run through multiple cases of data types, expect an float
    testdata= [
        (10.0, 5.0),
        (12345.0, 6172.5),
        (10, "Error: argument of type float expected"),
        ("string", "Error: argument of type float expected"),
        (True, "Error: argument of type float expected")
    ]

    @pytest.mark.parametrize("num,expected", testdata)
    def test_float_multiplication(self, num, expected):
        result = float_multiplication(num)
        assert result == expected

class TestStringConcatenation:
    # Use parameterized testing to run through multiple cases of data types, expect an string
    testdata= [
        ("CS4300 exists", "CS4300 exists which is really cool"),
        ("A cat is an animal", "A cat is an animal which is really cool"),
        (10, "Error: argument of type string expected"),
        (24.0, "Error: argument of type string expected"),
        (True, "Error: argument of type string expected")
    ]

    @pytest.mark.parametrize("string,expected", testdata)
    def test_string_concatenation(self, string, expected):
        result = string_concatenation(string)
        assert result == expected

class TestBooleanOperation:
    # Use parameterized testing to run through multiple cases of data types, expect a boolean
    testdata= [
        (True, True),
        (False, False),
        (10, "Error: argument of type boolean expected"),
        (24.0, "Error: argument of type boolean expected"),
        ("string", "Error: argument of type boolean expected")
    ]

    @pytest.mark.parametrize("boolean,expected", testdata)
    def test_boolean_operation(self, boolean, expected):
        result = boolean_operation(boolean)
        assert result == expected
