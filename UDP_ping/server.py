from socket import *
import random

HOST = 'localhost'
PORT = 8000
ADDR = (HOST, PORT)

RECEIVE_LIMIT = 1024

serverSocket = socket(AF_INET, SOCK_DGRAM)
try:
    serverSocket.bind(ADDR)
    print 'Server Ready.'
except Exception, err:
    print err

while True:
    message, addr = serverSocket.recvfrom(RECEIVE_LIMIT)
    print message
    if message == 'Q':
        break
    rand = random.randint(0, 10)
    print 'reply or ingnor:', rand
    if rand < 4:
        continue
    reply = 'Pong ' + addr[0]
    serverSocket.sendto(reply, addr)

serverSocket.close()
