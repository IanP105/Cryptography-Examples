def expMod(x, e, n):
    y = x
    for i in range(m - 2, 0):
        y = (y * y) % n
        if e == 1:
            y = (y * x) % n
    return y


m = 0






# ALTERNATE ATTEMPT 1
# def expTest1(a, e_power2, mod):
#     for i in range (0, e_power2):
#         a = (a * a) % mod
#     return a






# ALTERNATE ATTEMPT 2
# # Prime modulo value
# N = 1000000007
#
#
# def expTest2(bas, exp):
#     t = 1
#     while (exp > 0):
#
#         # For non-even exponents
#         if (exp % 2 != 0):
#             t = (t * bas) % N
#
#         bas = (bas * bas) % N
#         exp = int(exp / 2)
#     return t % N
#
#
# # Driver Code
# bas = 5
# exp = 100000
#
# modulo = expTest2(bas, exp)
# print(modulo)