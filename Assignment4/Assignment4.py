a = input("Enter the 1st number of the GCD equation.")
print("1st input number is: " + a)
a = int(a)
b = input("Enter the 2nd number of the GCD equation.")
print("2nd input number is: " + b)
b = int(b)

def gcd(a, b):
    while(b>0):
       a, b = b, a % b
    return a
print()
print("The GCD of the two input numbers is:")
print(gcd(a,b))
