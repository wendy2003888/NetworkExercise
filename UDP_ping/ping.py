from socket import *
import time, random, select


serverName = 'localhost'
PORT = 8000
ADDR = (serverName, PORT)

RECEIVE_LIMIT = 1024

# setdefaulttimeout(0.01)

clientSocket = socket(AF_INET, SOCK_DGRAM)
try:
    clientSocket.bind(ADDR)
    print 'Bind Server.'
except Exception, err:
    print err

num = random.randint(1, 10)
message = 'Ping ' + str(num) + ' times.'
print message
for i in range(num):
    message = 'Ping '+str(i) +' ' + serverName
    resttime = 1
    while resttime > 0:
        start_time = time.time()
        clientSocket.sendto(message, ADDR)
        rlist, wlist, xlist = select.select([clientSocket], [], [], resttime)
        end_time = time.time()
        if rlist == []:
            print 'Ping', str(i), ADDR[0],'Timeout'
            break
        else:
            _time = (end_time - start_time) * 1000
            for item in rlist:
                reply, addr = item.recvfrom(RECEIVE_LIMIT)
                print 'Ping', str(i), 'receiced:', reply, 'RTT:', _time
            break

##close server
message = 'Q'
try:
    clientSocket.sendto(message, ADDR)
except Exception, e:
    print e
    

clientSocket.close()

