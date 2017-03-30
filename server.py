#! /usr/bin/python
import os
import socket
import encryptionAES
import user_operation
port = 12000

def server(port):
        #if the file does not exist, create it
        if(os.path.isfile("user")):
            pass
        else:
            f = open("user", "w+")
            f.close()

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('',port))
	server.listen(1)

	while True:
		print "Waiting to be connected..."

		client, address = server.accept()
                identity = client.recv(1024)
                print identity
                username = client.recv(1024)
                print username
                password = client.recv(1024)
                print password
                #log in             
                if(identity == '1'):
                    if(encryptionAES.certificate(username, password)[0] == True):
                        client.send("Correct")
                    else:
                        client.send("Wrong")
                #log up
                elif(identity == '2'):
                    (iv, ciphertext) = encryptionAES.encrypt(password)
                    if(user_operation.create_new_user(username, iv, ciphertext)):
                        client.send("Log up successfully")
                    else:
                        client.send("The username has already been logged up")
                #delete account
                elif(identity == '3'):
                   response = user_operation.delete_user(username, password)
                   if(response):
                       client.send("Correct")
                   else:
                       client.send("Wrong")
		client.close()

if __name__== '__main__':
	server(port)
