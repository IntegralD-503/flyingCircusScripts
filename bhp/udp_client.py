#!/usr/bin/python2.7

import socket

target_host = "localhost"
target_port = 80;

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto("AAABBBCCC",(target_host,target_port))

#recieve some data
data, addr = client.recvfrom(4096)

print data
