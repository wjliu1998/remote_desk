# -*- coding: cp936 -*-

from Crypto.Cipher import AES
from Crypto import Random
import binascii
import os

#encrypt
def encrypt(passwd):
    key = 'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(passwd)
    ciphertext = binascii.b2a_hex(msg)
    return iv,ciphertext

#save iv and ciphertext
def save(username, iv, ciphertext):
    #with open('iv.txt','w') as f:
    #    f.write(iv)
    #with open('ciphertext.txt','w') as f:
    #    f.write(ciphertext)
    f = open("user", "r+")
    f.seek(0, 2)
    f.write(username + ":" + iv + ":" + ciphertext + os.linesep)
    return True

#certificate
def certificate(username, passwd):
    '''with open('iv.txt') as f:
        iv=f.read()
    with open('ciphertext.txt') as f:
        ciphertext=f.read()
    key = 'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg2 = iv + cipher.encrypt(passwd2)
    ciphertext2 = binascii.b2a_hex(msg2)
    if ciphertext==ciphertext2:
        print 'pass certification'
    else:
        print 'fail certification'''

    key = 'Sixteen byte key'
    f = open("user", "r+")
    allLines = f.readlines()

    for eachline in allLines:
        (user, iv, ciphertext) = eachline.split(":")
        cipher = AES.new(key, AES.MODE_CFB, iv)
        msg2 = iv + cipher.encrypt(passwd)
        ciphertext2 = binascii.b2a_hex(msg2)
        #print user, username, user==username
        #print ciphertext, ciphertext2+os.linesep, ciphertext==ciphertext2+os.linesep
        if(user == username and ciphertext == ciphertext2+os.linesep):
            return True
        else:
            return False
