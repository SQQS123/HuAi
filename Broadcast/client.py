from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024

ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(('', PORT))
print 'wating for message...'
while True:
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    print('...received ->%s  %s' % (addr, data))
