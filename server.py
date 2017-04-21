#! /usr/bin/python
import os
import socket
import encryptionAES
import user_operation
import ipstore
import time

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
                '''identity = client.recv(1024)
                print identity
                username = client.recv(1024)
                print username
                password = client.recv(1024)
                print password'''
                transfer = client.recv(1024).split(":")
                identity = transfer[0]
                username = transfer[1]
                password = transfer[2]
                print identity
                print username
                print password

                #log in             
                if(identity == '1'):
                    if(encryptionAES.certificate(username, password)[0] == True):
                        client.send("Correct")
			ip = ipstore.find_ip()
			time.sleep(1)
			client.send(ip)
			while(1):
				time.sleep(5)
				client.sendall("ARE YOU OK")
				check = client.recv(1024)
				if(check == "Still in use"):
					print check
				else:
					break
			ipstore.recycle_ip(ip)
                    else:
                        client.send("Wrong")

                #log up
                elif(identity == '2'):
                    (iv, ciphertext) = encryptionAES.encrypt(password)
                    answer = user_operation.create_new_user(username, iv, ciphertext)
                    if(answer == True):
                        client.send("Log up successfully")
                    elif(answer == False):
                        client.send("The username has already been logged up")
                    else:
                        client.send("Invalid username or password")
                        
                #delete account
                elif(identity == '3'):
                   response = user_operation.delete_user(username, password)
                   if(response == True):
                       client.send("Correct")
                   else:
                       client.send("Wrong")
    	        client.close()

if __name__== '__main__':
	server(port)
