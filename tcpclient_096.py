#!/usr/bin/env python
#-*- coding: utf-8 -*-
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
numbers = raw_input('Enter Numbers:')
clientSocket.send(numbers)
modifiednumbers = clientSocket.recv(1024)
print 'From Server:', modifiednumbers
clientSocket.close()
