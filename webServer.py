#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
#Prepare a sever socket
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
	
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	print 'Required connection', addr
	try:

		message = connectionSocket.recv(1024)
		print message,'\n'
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()

		#Send one HTTP header line into socket
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
		connectionSocket.send('Content-Type:text/html\n')
		

		#Send the content of the requested file to the client

		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
		#Close client socket
		connectionSocket.close()
		serverSocket.close()