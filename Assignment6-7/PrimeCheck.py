# Check if random numbers are prime

# Needs to print a table
# Needs to take in value from "GenRand" file


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

# Example of table printing
# print(f"{f'{m}' : <5}{f'{y}' : ^10}{f'{x}' : ^10}{f'{e}' : ^10}{f'{n}' : >5}")
# print(f"{f'{k}' : <5}{f'{y}' : ^10}{f'{z}' : ^10}{f'{a}' : ^10}{f'{n}' : >5}")