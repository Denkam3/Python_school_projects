# prime divider
number = 70616204741131
found = False
testing = number

def prime(testing): # function to test if the number is a prime number
    print (testing) # is it working?
    for i in range (2, testing):
        if testing % i == 0:
            return False
    return True    
        
while found == False and testing > 1:
    if testing == number: # test if the first number is prime
        if prime(testing):
                found = True
                break
    for i in range (2, number): #find other numbers
        if number % i == 0:
            testing = number // i
            if prime(testing):
                found = True
                break
print(f"The biggest prime number that can divide number {number} is {testing}")

    
