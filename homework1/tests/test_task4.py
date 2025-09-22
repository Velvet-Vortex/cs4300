import pytest
from src.task4 import calculate_discount

testdata= [
    (10, 10, 9),
    (100, 30.00, 70),
    (100.00, 6, 94),
    (100.00, 100.00, 0),
    (100.00, 0, 100)
]

# Test a mix of integers and floats with parameterized test cases
@pytest.mark.parametrize("price,discount,expected", testdata)
def test_mixed_floats_and_ints(price, discount, expected):
    result = calculate_discount(price, discount)
    assert result == expected

# Check for input type validation
def test_non_numeric_price():
    with pytest.raises(TypeError):
        calculate_discount("text", 100)

# Check for valid discount
def test_invalid_discount_positive():
    with pytest.raises(ValueError):
        calculate_discount(10, 150)

def test_invalid_discount_negative():
    with pytest.raises(ValueError):
        calculate_discount(10, -10)