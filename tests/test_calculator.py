from simple_calculator.calculator import Calculator

calculator = Calculator()

def test_add_two_numbers():
    # print("Pass")
    assert calculator.add(1,2) == 3

def test_add_multiple_numbers():
    # print("Pass")
    assert calculator.add(1,2,3,4) == 10

def test_multiply_numbers():
    # print("Pass")
    assert calculator.multiply(1,2) == 2

def test_multiply_multiple_numbers():
    # print("Pass")
    assert calculator.multiply(1,2,3,4) == 24
