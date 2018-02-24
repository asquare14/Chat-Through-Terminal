#!/usr/bin/env python
#-*- coding: utf-8 -*-
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive."
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    b = sorted(message)
    modifiedMessage = ''.join(b)
    serverSocket.sendto(modifiedMessage,clientAddress)
