# Use a helper function that takes in an integer and how many bytes long you want it to be, then gives a string binary representation for the part that X - look this up online

import random

def bin_string(int_val, bit_length):
    i = 1 << bit_length - 1
    binary_string = ''

    while 1 > 0:
        if (int_val & i) != 0:
            binary_string += '1'
        else:
            binary_string += '0'
        i = i // 2

    return binary_string

def gen_bin_list(n):
    binary_list = []

    for i in range(n):
        random_int = random.randint(0, 2 ** 32)
        binary_string = bin_string(random_int, 32)
        binary_list.append(binary_string)

    return binary_string




def get_random_bit():
    a = bin(random.randint(0, 2**32))
    c = a [2:]
    return c[-1]

def generate_random_number (show_trace = False):
    # X