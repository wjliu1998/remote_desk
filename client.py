#! /usr/bin/python

import socket

host = 'localhost'
port = 54321

def client(port):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (host, port)
	print "Connecting to %s port %s" %server_address
	server.connect(server_address)
	
	try:
		ID=raw_input("Enter your ID: ")
		server.sendall(ID)
		Password=raw_input("Password: ")
	except socket.errno, e:
		print "Socket error: %s" %str(e)
	except Exception, e:
		print "Other exception: %s" %str(e)
	finally:
		print"Closing..."
		server.close()

if __name__ == '__main__':
	client(port)
