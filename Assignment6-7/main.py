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
    for i == k:
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
