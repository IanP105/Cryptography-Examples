def GCD(m,n):
    x = m
    y = n
    if m < n:
        swap(m,n)
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
    return x,y,m
    
# Driver code starts here.
print(f"{'i' : <5}{'q' : ^10}{'m' : ^10}{'n' : ^10}{'r' : >5}")
a =
b =
divider, dividend, gcd = GCD(a,b)
