from socket import *
import os

Host = 'localhost'
Port = 12345
ADDR = (Host, Port)

BASEDIR = os.getcwd()
BASEDIR = os.path.join(BASEDIR, 'files')

CONNECTION_LIMIT = 3
RECEIVE_LIMIT = 1024
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(ADDR)

serverSocket.listen(CONNECTION_LIMIT)

while True:
    print 'Listening...'
    _command = raw_input('If exit please input Q.\n')
    if _command == 'Q':
        break
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(RECEIVE_LIMIT)
        filenames = message.split()
        # print filename
        for filename in filenames: 
            _path = os.path.join(BASEDIR, filename)
            # print _path
            f = open(_path)
            outputdata = [line for line in f.readlines()]
            print outputdata
            Header = 'HTTP/1.1 200 OK\n'
            Header += 'Content-Type: text/html; charset=UTF-8\n\n'
            connectionSocket.send(Header)
            for i in range(len(outputdata)):
                connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except Exception, error:
        print error
        connectionSocket.close()
        

serverSocket.close()


