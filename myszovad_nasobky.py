# first exercise

result = 0 # starting value
testing_number = 1
while testing_number < 1235:
    if testing_number % 3 == 0 or testing_number % 5 == 0:
        result = result + testing_number # add result
    testing_number += 1 # test next number
    if testing_number == 1234:
        print(f"Soucet cisel je: {result}") # end
