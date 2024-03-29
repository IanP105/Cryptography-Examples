import random
import time

def encrypt(input_string):
    random.seed(int(time.time()))
    key = random.randbytes(len(input_string))
    byte_array = bytearray(input_string.encode())
    encrypted_byte_array = bytearray()
    for i in range(len(byte_array)):
        encrypted_byte_array.append(byte_array[i] ^ key[i])
    return encrypted_byte_array

def decrypt(encrypted_byte_array, key):
    decrypted_byte_array = bytearray()
    for i in range(len(encrypted_byte_array)):
        decrypted_byte_array.append(encrypted_byte_array[i] ^ key[i])
    return decrypted_byte_array.decode()


# Run encryption
random.seed(1664435990)
input_string = "Hello World!"
encrypted_data = encrypt(input_string)
print("Encrypted data:", encrypted_data)

# Run decryption
decrypted_string = decrypt(encrypted_data, b'\xba\x9a\x05\x50\x35\x76\x72\xd6\x78\x4b\xff\x91')
print("Decrypted string:", decrypted_string)