import os
import base64


def setEnvVar():
    os.environ ['VAULT_ADDR'] = "VAULT SERVER GOES HERE"
    os.environ ['VAULT_TOKEN'] = "VAULT AUTH TOKEN GOES HERE"


def enableTransitEngine():
    os.system('vault secrets enable transit')


def createKey():
    key_name = 'my_key'
    os.system("vault write transit/keys/{} type=aes256-gcm96".format(key_name))


def decodeMessage(cipher, key):
    os.system("vault write transit/decrypt/{} ciphertext={}".format(key, cipher))

def encryptMessage(plain, key):
    plain_text = base64.b64encode(bytes(plain, 'utf-8'))
    os.system("vault write transit/encrypt/{} plaintext={}".format(key, plain_text.decode('utf-8')))

setEnvVar()
enableTransitEngine()
createKey()
encryptMessage('hello from python', 'my_key')
decodeMessage('vault:v1:KEYGOESHERE', 'my_key')

original_text = base64.b64decode('KEYGOESHERE')
print(original_text.decode())
