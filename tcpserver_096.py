#!/usr/bin/env python
#-*- coding: utf-8 -*-
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive.'
while 1:
    connectionSocket, addr = serverSocket.accept()
    print "Connection established by:",addr
    numbers = connectionSocket.recv(1024)
    print "Data received is",numbers
    temp=map(lambda x:int(x),numbers.split())
    temp.sort()
    print "Sorted Data is:",str(temp)
    sorted_numbers = str(temp)
    connectionSocket.send(sorted_numbers)
connectionSocket.close()
