from socket import *

Server = 'localhost'
serverPort = 12345
ADDR = (Server, serverPort)


clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(ADDR)
_request = raw_input('Please input request:')
clientSocket.send(_request)
message = clientSocket.recv(1024)
print message

# clientSocket.close()


