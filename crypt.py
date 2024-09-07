'''
CSCI 531 Final Project
Andrew Rodriguez
Aaron Lobo
'''

import sys

import os
from Crypto.Cipher import AES # type: ignore
from Crypto.Util.Padding import pad, unpad





def rsaEncrypt(message, e, n):
    c = pow(message, e, n)


    return c

def rsaDecrypt(c, d, n):

    m = pow(c, d, n)
    return m

def aesEncrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    cipherBytes = cipher.encrypt(pad(message.encode("utf-8"), 16))
    return cipherBytes

def aesDecrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    cipherBytes = unpad(cipher.decrypt(ciphertext), 16)
    return cipherBytes.decode("utf-8")



def encrypt(publicKeyFile, messageFile, cryptFile):
    messageFile = messageFile
    key = os.urandom(16)

    message = open(messageFile, "r").read()

    encrypted = aesEncrypt(message, key)
    #print("Encrypted: ", encrypted)
    
    publicKeyFile = open(publicKeyFile, "r")
    publicKey = publicKeyFile.read()

    n, e = publicKey.replace(" ", "").split(",")


    intKey = int.from_bytes(key, 'big')

    Kp = rsaEncrypt(intKey, int(e), int(n))



    output = open(cryptFile, "w")
    output.write(str(encrypted))
    output.write("\n")
    output.write(str(Kp))
    output.close()

def encryptMessage(publicKeyFile, messageFile,fileName):
    #cryptFile = "tempEncryptedMessage.cip"
    #messageFile = messageFile
    key = os.urandom(16)

    message = messageFile

    encrypted = aesEncrypt(message, key)
    #print("Encrypted: ", encrypted)
    
    publicKeyFile = open(publicKeyFile, "r")
    publicKey = publicKeyFile.read()

    n, e = publicKey.replace(" ", "").split(",")


    intKey = int.from_bytes(key, 'big')

    Kp = rsaEncrypt(intKey, int(e), int(n))



    output = open(fileName, "w")
    output.write(str(encrypted))
    output.write("\n")
    output.write(str(Kp))
    output.close()



def decryptMessage(privateKeyFile,fileName):
    print(privateKeyFile)
    print(fileName)
    privateKeyFile = open(privateKeyFile, "r")
    privateKey = privateKeyFile.read()

    n, d = privateKey.replace(" ", "").split(",")

    
    
    encrypted, Kp = open(fileName, "r").read().split("\n")

    Key = rsaDecrypt(int(Kp), int(d), int(n))

    bytesKey = Key.to_bytes(16, 'big')

    decrypted = aesDecrypt(eval(encrypted), bytesKey)
    #print("Decrypted: ", decrypted)
    return decrypted



def decrypt(privateKeyFile,cipherFile):

    privateKeyFile = open(privateKeyFile, "r")
    privateKey = privateKeyFile.read()

    n, d = privateKey.replace(" ", "").split(",")

    cryptFile = cipherFile
    
    encrypted, Kp = open(cryptFile, "r").read().split("\n")

    Key = rsaDecrypt(int(Kp), int(d), int(n))

    bytesKey = Key.to_bytes(16, 'big')

    decrypted = aesDecrypt(eval(encrypted), bytesKey)
    return decrypted





