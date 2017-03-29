#! /usr/bin/python
import os
import socket

host = '192.168.1.111'
port = 12000

def client(port):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (host, port)
	print "Connecting to %s port %s" %server_address
	server.connect(server_address)
	
	try:
            identity = raw_input("1 for login, 2 for logup")
            server.sendall(identity)
	    ID=raw_input("Enter your ID: ")
	    server.sendall(ID)
	    password=raw_input("Password: ")
            server.sendall(password)
            if("Correct" == server.recv(1024)):
                os.system("rdesktop %s -u %s -p %s" % (host, ID, password))
	except socket.errno, e:
	    print "Socket error: %s" %str(e)
	except Exception, e:
	    print "Other exception: %s" %str(e)
	finally:
	    print"Closing..."
	    server.close()

if __name__ == '__main__':
	client(port)
