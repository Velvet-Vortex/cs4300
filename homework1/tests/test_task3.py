from src.task3 import check_input_number, print_primes, check_for_prime, sum_to_hundred
from io import StringIO
import sys

class TestCheckInputNumber:
    # Test positive, negative and zero integer inputs
    def test_positive_int(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "10")
        check_input_number()
        out, err = capsys.readouterr()
        assert out == "The inputted number is positive\n"

    def test_negative_int(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "-10")
        check_input_number()
        out, err = capsys.readouterr()
        assert out == "The inputted number is negative\n"

    def test_zero_int(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "0")
        check_input_number()
        out, err = capsys.readouterr()
        assert out == "The inputted number is zero\n"

# Test positive, negative and zero float inputs
    def test_positive_float(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "10.101")
        check_input_number()
        out, err = capsys.readouterr()
        assert out == "The inputted number is positive\n"

    def test_negative_float(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "-10.101")
        check_input_number()
        out, err = capsys.readouterr()
        assert out == "The inputted number is negative\n"

    def test_zero_float(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "0.0")
        check_input_number()
        out, err = capsys.readouterr()
        assert out == "The inputted number is zero\n"

class TestPrintPrimes:
    # Test the prime number outputs
    def test_print_primes(self, capsys):
        expected_output = "The first ten prime numbers are: \n2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"
        print_primes()
        out, err = capsys.readouterr()
        assert out == expected_output
        
    # Verify the check for prime function with a prime number
    def test_true_check_for_prime(self):
        result = check_for_prime(2)
        assert result == True
    
    # Verify the check for prime function with a nonprime number
    def test_false_check_for_prime(self):
        result = check_for_prime(10)
        assert result == False

class TestSumToHundred:
    # Verify the summation is 5050
    def test_sum_to_hundred(self, capsys):
        expected_output = "The summation of all numbers from 1 to 100 is 5050\n"
        sum_to_hundred()
        out, err = capsys.readouterr()
        assert out == expected_output