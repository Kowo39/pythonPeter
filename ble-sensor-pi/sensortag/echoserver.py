import socket
import sys

#create a TCP/IP Socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
server_address = ('localhost', 10000)

print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listen incomming connection
sock.listen(1)

while True:
	#wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()

	try:
	   	print >>sys.stderr, 'connection from', client_address
		#Recieve data in small chunks and retrasmi it
		while True:
			data = connection.recv(16)
			print >>sys.stderr, 'received "%s"' %data
	   		if data:	 
				print >>sys.stderr, 'sendinng data back to the client'
				connection.sendall(data)
	   		else:
				print >>sys.stderr, 'no more data my friend from', client_address
				break

	
	finally:
		#Clean up the conection
		connection.close() 
