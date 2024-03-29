# Generate the random numbers


import random

def generate_random_number ():
    counter = 0
    while counter < 5:
        baseRand = random.getrandbits(5)                                # Get random number of length 5 bits
        print("Integer form: "),
        print(baseRand)
        print()
        baseRand = format(baseRand, '05b')                              # Convert to binary, strip "0b", and retain all leading 0s
        print("Binary form: ")
        print(baseRand)
        print()
        fullRand = "0000000000000000000000000" + "1" + baseRand + "1"   # Add all padding to random number
        print("Full form: "),
        print(fullRand)
        print()
        counter += 1                                                      # Increment counter

generate_random_number()


# Unused implementation below

# def bin_string(int_val, bit_length):
#     i = 1 << bit_length - 1
#     binary_string = ''
#
#     while 1 > 0:
#         if (int_val & i) != 0:
#             binary_string += '1'
#         else:
#             binary_string += '0'
#         i = i // 2
#
#         return binary_string

# def gen_bin_list(n):
#     binary_list = []
#
#     for i in range(n):
#         random_int = random.randint(0, 2 ** 32)
#         binary_string = bin_string(random_int, 32)
#         binary_list.append(binary_string)
#
#         return binary_string

# def get_random_bit():
#     a = bin(random.randint(0, 2**32))
#     c = a [2:]
#     return c[-1]

# End unused implementation