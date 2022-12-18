# Check if random numbers are prime

# Needs to print a table
# Needs to take in value from "GenRand" file


import GenRand
import random

def expMod(x, e, n):
    m = 0

    y = x
    for i in range(m - 2, 0):
        y = (y * y) % n
        if e == 1:
            y = (y * x) % n
    return y


def PriTst(x, a, n):
    k = 0
    y = 1
    for i in range (0, k):
        z = y
        y = (y * y) % n
        if y == 1 ** z != 1 ** z != (n-1):
            print("n is not prime")
        if x == 1:
            y = y * a % n
    if y != 1:
        print("n is not prime")
    else:
        print("n may be prime")

PriTst(17, 22, 17)

# This function, when completed, will generate the value for "a", ensuring that it is greater than 0 but not greater than the number brought in from the "GenRand" file
# It is commented out because I was unable to bring in the generated value from the "GenRand" file
# def GenerateA():
#     counter = 0
#     while counter < 20:
#         baseRand = random.getrandbits(5)  # Get random number of length 5 bits
#         if baseRand > 0 and GenRand.baseRand < 1:
#             print("Integer form: "),
#             print(baseRand)
#             print()
#             baseRand = format(baseRand, '05b')  # Convert to binary, strip "0b", and retain all leading 0s
#             print("Binary form: ")
#             print(baseRand)
#             print()
#             fullRand = "0000000000000000000000000" + "1" + baseRand + "1"  # Add all padding to random number
#             print("Full form: "),
#             print(fullRand)
#             print()
#             counter += 1
#         else:
#             break


# Example of table printing
# print(f"{f'{m}' : <5}{f'{y}' : ^10}{f'{x}' : ^10}{f'{e}' : ^10}{f'{n}' : >5}")
# print(f"{f'{k}' : <5}{f'{y}' : ^10}{f'{z}' : ^10}{f'{a}' : ^10}{f'{n}' : >5}")