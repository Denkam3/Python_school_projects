# palindrome
a = 1000
b = 1000

def palindrome(a, b): # is it a palindrome
    test = str(a * b)
    first = test
    second = ""
    for i in range (len(test) - 1, -1, -1): # reverse the string
        second = second + test[i]
    if first == second:
        return True
    else:
        return False

while palindrome(a,b) == False:
    for a in range (9999, 999, -1): # go from the highest numbers
        for b in range (9999, 999, -1):
             if palindrome(a, b):
                break
        if palindrome(a, b):
            break
print(a * b)
