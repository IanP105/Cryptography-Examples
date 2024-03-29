# Cryptography-Examples

## 1-Vigenere-Cipher

This program will first generate a key that consists of random characters and is the length of the user's input.
Next, the user inputs the location of the .html file to encrypt and the file containing the key with which to do so.
Lastly, the user will repeat the above process for decryption.

## 2-PRNG-Stream-Cipher

This program uses a random seed and a pseudo random number generator to encrypt/decrypt a long string.
It uses the system time for the random seed and "random.randbytes" to generate a sequence of random bytes for use as a key.
The function "bytearray" is used to convert a string to an array of bytes.
The XOR operator is used over the input string and key to encrypt the string.

## 3-Euclid-Algorithm

This program will efficiently find the GCD of two numbers, "m" and "n", and display the calculations used to reach the result.
The program outputs a table that shows the values for every variable at each iteration.
At each round of iteration, "i", "m" is divided by "n", the quotient is labeled "q", and the remainder is labeled "r".
This repeats until "n" = 0. Lastly, "m" is the output, which is the GCD of all inputs.

## 4-KMS-Vault

This is a simple program that interfaces with [Hashicorp Vault](https://www.hashicorp.com/products/vault) running on the local machine.
It retrieves a message from the vault and encrypts or decrypts it using [aes256-gcm96](https://en.wikipedia.org/wiki/Galois/Counter_Mode).

## 5-Fast-Exponentiation

This program is a partial implementation of the "Fast Exponentiation Algorithm".
