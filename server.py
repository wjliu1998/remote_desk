#! /usr/bin/python
import os
import socket
import encryptionAES

#host = 'localhost'
port = 12000

def server(port):
        if(os.path.isfile("user")):
            pass
        else:
            f = open("user", "w+")
            f.close()
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#server_address = (host, port)
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
                if(identity == '1'):
                    if(encryptionAES.certificate(username, password) == True):
                        client.send("Correct")
                    else:
                        client.send("Wrong")
                else:
                    (iv, ciphertext) = encryptionAES.encrypt(password)
                    if(encryptionAES.save(username, iv, ciphertext)):
                        print "Logup successfully!"
		#username = client.recv(1024)
		#print username
		#password = client.recv(1024)
		#print password
		client.close()

if __name__== '__main__':
	server(port)
