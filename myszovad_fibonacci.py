# Fibonacci

first_number = 0
second_number = 1
Fibonacci = 1
result = 0

while Fibonacci < 5000000:
    if Fibonacci % 2 == 0:
        result = result + Fibonacci # add to result
    first_number = second_number
    second_number = Fibonacci
    Fibonacci = first_number + second_number # next number
    if Fibonacci >= 5000000:
        print(f"Súčet čísel je: {result}")
    
    
