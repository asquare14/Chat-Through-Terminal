#!/usr/bin/env python
#-*- coding: utf-8 -*-
from socket import*
serverName="localhost"
serverPort=12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = raw_input("Enter String:")
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print "Sorted string is:"
print modifiedMessage
clientSocket.close()
