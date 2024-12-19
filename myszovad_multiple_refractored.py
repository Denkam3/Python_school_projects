"""
Sum of numbers that are less than 1235 and can be divided by 3 or 5
"""

def multiple(limit):
    """
    Returns final sum of numbers divided by 3 and 5 in defined limit
    """
    result = 0
    testing_number = 1
    while testing_number < limit:
        if testing_number % 3 == 0 or testing_number % 5 == 0:
            result = result + testing_number # add result
        testing_number += 1 # test next number
    return result

print(f"The final sum is {multiple(1234)}")
