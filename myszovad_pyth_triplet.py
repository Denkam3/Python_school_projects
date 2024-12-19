# Find Pythagorean triplet where a + b + c = 1000. Answer a * b * c
found = False
while found == False:
    for a in range (1, 501): # can't be more, save time
        for b in range (1, 501):
            c = (a * a + b * b) ** 0.5 # Pythagorean theorem
            if a + b + c == 1000:
                found = True
                r = a * b * c
                break
print(f"The pythagorean triplet's product is {int(r)}")

