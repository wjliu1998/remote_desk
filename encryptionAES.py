# -*- coding: cp936 -*-

from Crypto.Cipher import AES
from Crypto import Random
import binascii
import os

#encrypt password
def encrypt(passwd):
    key = 'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(passwd)
    ciphertext = binascii.b2a_hex(msg)
    return iv,ciphertext

#save username, iv and ciphertext to the file
def save(username, iv, ciphertext):
    #with open('iv.txt','w') as f:
    #    f.write(iv)
    #with open('ciphertext.txt','w') as f:
    #    f.write(ciphertext)
    f = open("user", "r+")
    f.seek(0, 2)
    f.write(username + ":" + iv + ":" + ciphertext + os.linesep)
    return True

#certificate the correctness of username and passwd
def certificate(username, passwd):

    key = 'Sixteen byte key'
    f = open("user", "r+")
    allLines = f.readlines()

    for eachline in allLines:
        (user, iv, ciphertext) = eachline.split(":")
        cipher = AES.new(key, AES.MODE_CFB, iv)
        msg2 = iv + cipher.encrypt(passwd)
        ciphertext2 = binascii.b2a_hex(msg2)
        if(user == username and ciphertext == ciphertext2+os.linesep):
            return True
        else:
            return False
