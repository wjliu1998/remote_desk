# -*- coding: cp936 -*-

from Crypto.Cipher import AES
from Crypto import Random
import binascii

#encrypt
def encrypt(passwd):
    key = 'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(passwd)
    ciphertext = binascii.b2a_hex(msg)
    return iv,ciphertext

#save iv and ciphertext
def save(iv,ciphertext):
    with open('iv.txt','w') as f:
        f.write(iv)
    with open('ciphertext.txt','w') as f:
        f.write(ciphertext)

#certificate
def certificate(passwd2):
    with open('iv.txt') as f:
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
        print 'fail certification'
        
#test 
passwd='12345678'
print 'original password:',passwd

iv,ciphertext=encrypt(passwd)
print 'iv:',iv
print 'ciphertext:',ciphertext

save(iv,ciphertext)

passwd2='12345678'
print 'password input:',passwd2

certificate(passwd2)
