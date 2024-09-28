# dividable by numbers in range
testing = 30 # defined range 1 to n
found = False

def dividers(testing): # can it be divided by numbers in range?
    for i in range (1, 30):
        if testing % i != 0:
            return False
    return True
    
while found == False:
    if dividers(testing):
        found = True
        break
    testing = testing + 30 # test next
print (testing)

    
