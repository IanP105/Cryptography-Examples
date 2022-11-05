a = input("Enter the 1st number of the GCD equation.")
print("1st input number is: " + a)
a = int(a)
b = input("Enter the 2nd number of the GCD equation.")
print("2nd input number is: " + b)
b = int(b)

if b == 0:
    print("Denominator cannot be 0.")
    system.exit()

def gcd(a, b):
    while(b>0):
       a, b = b, a % b
    return a
print()
print("The GCD of the two input numbers is:")
print(gcd(a,b))

# I am not sure how to do this in a way that will show each step of the GCD equation, which is why a table is not printed.
