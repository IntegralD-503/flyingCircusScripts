#!/usr/bin/python2.7

import socket

target_host = "localhost"
target_port = 9999;

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#coonect to client
client.connect((target_host,target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

#recieve some data
response = client.recv(4096)

print response
