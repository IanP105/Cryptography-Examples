import sys
import random

# Opens the .html file
def readFileInfo(pathToFile):
    infoOfFile = None
    with open(pathToFile, "r") as f:
        infoOfFile = f.read()
    return infoOfFile

# Writes to the .html file
def writeFileInfo(pathToFile, fileInfo):
    with open(pathToFile, "w") as f:
        f.write(fileInfo)
    return

# Creates the encryption key
def createKey(keySize):
    key = []
    for i in range(keySize):
        key.append(chr(random.randrange(26)+ord('A')))
    return("" . join(key))

# Puts the encryption key in a file
def createKeyFile(pathToFile, keySize):
    key = createKey(keySize)
    writeFileInfo(pathToFile, key)
    return key

# Sets up the encryption process
def encrypt(plainText, key):
    cipher_text = ""
    key_len = len(key)
    key_point = 0
    for i in range(len(plainText)):
        x = ord(plainText[i])
        shifts = ord(key[key_point % key_len]) - ord('A')
        offset_point = ord('A') if plainText[i]>='A' and plainText[i]<='Z' else ord('a')
        if (plainText[i]>='A' and plainText[i]<='Z') or (plainText[i]>='a' and plainText[i]<='z'):
            key_point += 1     
            x = ((ord(plainText[i])-offset_point) + shifts) % 26 + offset_point
        cipher_text += chr(x)
    return cipher_text

# Uses the key to encrypt the .html file
def encryptFile(pathToFile, keyPath):
    key = readFileInfo(keyPath).strip()
    plaintext = readFileInfo(pathToFile)
    ciphertext = encrypt(plaintext, key)
    outputPathToFile = pathToFile[:pathToFile.rfind(".")] + "_enc"+pathToFile[pathToFile.rfind("."):]
    writeFileInfo(outputPathToFile, ciphertext)
    return ciphertext, outputPathToFile

# Sets up the decryption process
def decrypt(cipherText, key):
    plain_text = ""
    key_len = len(key)
    key_point = 0
    for i in range(len(cipherText)):
        x = ord(cipherText[i])
        shifts = ord(key[key_point % key_len]) - ord('A')
        offset_point = ord('A') if cipherText[i]>='A' and cipherText[i]<='Z' else ord('a')
        if (cipherText[i]>='A' and cipherText[i]<='Z') or (cipherText[i]>='a' and cipherText[i]<='z'):
            key_point += 1     
            x = ((ord(cipherText[i])-offset_point) - shifts) % 26 + offset_point
        plain_text += chr(x)
    return plain_text

# Uses the key to decrypt the .html file
def decryptFile(pathToFile, keyPath):
    key = readFileInfo(keyPath).strip()
    cipher_text = readFileInfo(pathToFile)
    plain_text = decrypt(cipher_text, key)
    outputPathToFile = pathToFile[:pathToFile.rfind(".")] + "_dec"+pathToFile[pathToFile.rfind("."):]
    writeFileInfo(outputPathToFile, plain_text)
    return plain_text, outputPathToFile



# Begin command input sequence
print(len(sys.argv))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Wrong arguments.")
        sys.exit(1)
   
    command_action =  sys.argv[1]

    if command_action == "keygen":
        if len(sys.argv) != 4:
            sys.exit(1)
        else:
            createKeyFile(sys.argv[3], int(sys.argv[2]))
            sys.exit(0) 
    elif  command_action == "encrypt":
        if len(sys.argv) != 4:
            sys.exit(1)
        else:
            print(sys.argv[3], sys.argv[2])
            encryptFile(sys.argv[3], sys.argv[2])
            sys.exit(0) 
    elif  command_action == "decrypt":
        if len(sys.argv) != 4:
            sys.exit(1)
        else:
            print(sys.argv[3], sys.argv[2])
            decryptFile(sys.argv[3], sys.argv[2])
            sys.exit(0) 
    else:
        print ("Invalid command.")
        sys.exit(1)
