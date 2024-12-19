"""
Sum of Fibonacci sequence even numbers that are less than 5000000
"""

def fibonacci(limit):
    """
    Returns sum of even numbers of fibonacci sequence in the defined limit
    """
    first_number, second_number = 1, 2
    result = 0
    while first_number < limit:
        if first_number % 2 == 0:
            result = result + first_number
        first_number, second_number = second_number, first_number + second_number
    return result

print(fibonacci(5000000))
