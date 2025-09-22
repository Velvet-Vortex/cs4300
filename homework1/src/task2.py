"""
Task 2: Variables and Data Types
Create a new file named task2.py demonstrating the use of various data types, including integers, 
floating-point numbers, strings, and boolean. Implement a Python using pytest to test case for each
data type, ensuring that the script's behavior matches the expected outcomes.
"""

def integer_addition(num):
    if (type(num) == int):
        return num + 100
    else: 
        return "Error: argument of type integer expected"

def float_multiplication(num):
    if (type(num) == float):
        return num * 0.50
    else: 
        return "Error: argument of type float expected"

def string_concatenation(text):
    if (type(text) == str):
        return text + " which is really cool"
    else:
        return "Error: argument of type string expected"

def boolean_operation(value):
    if (type(value) == bool):
        return value and True
    else:
        return "Error: argument of type boolean expected"

if __name__ == '__main__':
    print(integer_addition(10))
    print(float_multiplication(50.0))
    print(string_concatenation("A cat is an animal"))
    print(boolean_operation(True))