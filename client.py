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
            identity = raw_input("1 for login, 2 for logup, 3 for delete:")
            server.sendall(identity)
	    username=raw_input("Username: ")
	    server.sendall(username)
	    password=raw_input("Password: ")
            server.sendall(password)
            response = server.recv(1024)
            if(identity == '1'):
                if(response == "Correct"):
                    os.system("rdesktop %s -u %s -p %s" % (host, username, password))
                elif(response == "Wrong"):
                    print "Wrong username or password"
            elif(identity == '2'):
                print response
            elif(identity == '3'):
                if(response == "Correct"):
                    print "The account is deleted"
                else:
                    print "The username doesn't exist or the password is wrong"
        except socket.errno, e:
	    print "Socket error: %s" %str(e)
	except Exception, e:
	    print "Other exception: %s" %str(e)
	finally:
	    print"Closing..."
	    server.close()

if __name__ == '__main__':
	client(port)
