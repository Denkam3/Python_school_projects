# Delitelia

# Euclid's algorithm
def Euklid(a, b):
    while b != 0:
        result = a % b
        a = b
        b = result
    return a

# Formula I found
def Formula(a, b):
    result = a * b // Euklid(a, b)
    return result

final = 1 # must def first value
for i in range (1, 31): #iteration with all numbers in range
    final = Formula(final, i)
print(f"The smallest possitive integer divisible by numbers 1-30 is {final}")


