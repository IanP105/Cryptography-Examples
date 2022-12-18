# Find the multiplicative inverse via extended euclidean algorithm

# Needs to have "extended" code implemented


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

def GCD(m, n):
    x = m
    y = n
    if m < n:
        swap(m, n)
    i = 0
    while n != 0:
        r = m % n
        q = m // n
        print(f"{f'{i}' : <5}{f'{q}' : ^10}{f'{m}' : ^10}{f'{n}' : ^10}{f'{r}' : >5}")
        i = i + 1
        m = n
        n = r
        if n == 0:
            m = 1
            q = ""
            r = "STOP"
            print(f"{f'{i}' : <5}{f'{q}' : ^10}{f'{m}' : ^10}{f'{n}' : ^10}{f'{r}' : >5}")
    return x, y, m


# Unimplemented example of extended euclidean
# def extendedEuclideanAlgorithm(a,b):
#     if a == 0:
#         return b, 0, 1
#     gcd, u, v = extendedEuclideanAlgorithm(b % a, a)
#     x = v - (b // a ) * u
#     y = u
#     return gcd, x, y
#
# print(extendedEuclideanAlgorithm(10,25))
#
# #Output:
# (5, -2, 1)

# Driver code starts here.
print(f"{'i' : <5}{'q' : ^10}{'m' : ^10}{'n' : ^10}{'r' : >5}")
a = 4
b = 16
divider, dividend, gcd = GCD(a, b)