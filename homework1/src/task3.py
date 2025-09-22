"""
Task 3: Control Sturctures
Create a new file named task3.py. Create an if statement to check if a given number is positive,
negative, or zero. Implement a for loop to print the first 10 prime numbers (you may need to
research how to calculate prime numbers). Create a while loop to find the sum of all numbers from
1 to 100. Write pytest test cases to verify the correctness of your code for each control structure.
"""

def check_input_number():
    """Checks the whether an inputted number is positive, negative, or zero"""
    user_input = input("Enter a number: ")
    number = 0

    # Check whether to cast user input to a float or a string
    if "." in user_input:
        number = float(user_input)
    else:
        number = int(user_input)
    
    if (number > 0):
        print("The inputted number is positive")
    elif (number< 0):
        print("The inputted number is negative")
    else:
        print("The inputted number is zero")

def print_primes():
    """Calculates and prints the first ten prime numbers using only for loops"""
    prime_nums = []

    # Add prime numbers to an array
    for num in range(2, 100):
        if (check_for_prime(num) == True):
            prime_nums.append(num)
    
    # Use a for loop to print the first ten prime numbers from the list
    print("The first ten prime numbers are: ")
    for x in range(0, 10):
        print(prime_nums[x])

def check_for_prime(num):
    """
    Checks if the given number is a prime
    Code for checking a prime number was taken from https://www.geeksforgeeks.org/dsa/check-for-prime-number/
    """
    # Check for divisibility by any number from two up to itself
    for i in range(2, num):
        if num % i == 0:
            return False
    # If the number is not evenly divisible, it's prime
    return True

def sum_to_hundred():
    current_num = 1
    total = 0
    while(current_num <= 100):
        total += current_num
        current_num += 1
    print("The summation of all numbers from 1 to 100 is " + str(total))

if __name__ == '__main__':
    print("CHECKING NEGATIVE, POSITIVE, OR ZERO")
    check_input_number()
    print("\nCALCULATING FIRST TEN PRIMES")
    print_primes()
    print("\nSUMMING THE NUMBERS FROM 1 - 100")
    sum_to_hundred()