import socket
from time import sleep
import os

names = ['drive.google.com', 'mail.google.com', 'google.com']

def getDNSResolution(names):
    addrs = {}
    for name in names:
        addr = socket.gethostbyname(name)
        addrs[name] = addr
    return addrs

records = getDNSResolution(names)

while True:
    print('\n')
    sleep(1)
    for name in records:
        addr = socket.gethostbyname(name)
        if addr == records[name]:
            print(name + ' - ' + addr)
        else:
            print(' [ERROR] ' + name + ' IP mistmatch: ' + records[name] + '=>' + addr)
            records[name] = addr