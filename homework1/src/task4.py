"""
Task 4: Functions and Duck Typing
Duck typing is the functionality of a language where "if it looks like a duck and quacks like a duck,
you might as well treat it like a duck." This is quite common in interpreted languages. Create a
new file namedtask4.py that calculates the final price of a product after applying a given discount
percentage inside of a function named calculate_discount. The function should accept any numeric
type for price and discount. Write pytest test cases to test the calculate_discount function with
various types (integers, floats) for price and discount.
"""

def calculate_discount(price, discount):
    """
    Calculates the total given a price and discount
    
    Args:
        price: the total before the discount is applied
        discount: the discount to apply to the price in percent

    Returns:
        the total after the discount is applied to the price
    
    Raises:
        ValueError: if the discount is not between 0 and 100
        TypeError: if the inputs for price and discount are non-numeric
    """
    # Convert the percentage to a decimal value
    try:
        if (discount > 100 or discount < 0):
            raise ValueError("Discount must be between 0 and 100")
        # Calculate the total after taking off the discount
        total = price - (price*(discount/100))
        return total
    except TypeError:
        raise TypeError("Price and discount must be an integer or float")