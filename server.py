#! /usr/bin/python

import socket

host = 'localhost'
port = 54321

def server(port):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_address = (host, port)
	server.bind(server_address)
	server.listen(5)
	while True:
		print "Waiting to be connected..."
		client, address = server.accept()
		ID = client.recv(1024)
		print ID
		Password = client.recv(1024)
		print Password
		client.close()

if __name__== '__main__':
	server(port)
