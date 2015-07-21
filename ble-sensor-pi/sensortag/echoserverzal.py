import socket
import sys
import time
import datetime

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
	print >>sys.stderr, '\n\n\n\t\t*** A Server waiting for a connection ***'
	connection, client_address = sock.accept()
	ts = time.time()
	try:
		
        	print >>sys.stderr, '\n - connection from', client_address
		print " -",datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')	   	
		
		#Recieve data in small chunks and retrasmi it
		while True:
			data = connection.recv(30)
			
			
	   		if data:	 
				pass
				print >>sys.stderr, ' - Data received from tag"%s"' %data
			#	print >>sys.stderr, 'sendinng data back to the client'
			#	connection.sendall(data)
	   		else:
				#print >>sys.stderr, '\nno more data my friend from', client_address
				break

	
	finally:
		pass #Clean up the conection
		#connection.close() 
