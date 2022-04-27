import socket
from time import sleep
import os
import json
import yaml

names = ['drive.google.com', 'mail.google.com', 'google.com']

def getDNSResolution(names):
    addrs = {}
    for name in names:
        addr = socket.gethostbyname(name)
        addrs[name] = addr
    return addrs

def saveDNSResolution(records):
    with open('dnsResolution.json', 'w') as jsonFile:
        jsonFile.write(str(json.dumps(records)))
    with open('dnsResolution.yaml', 'w') as yamlFile:
        yamlFile.write(yaml.dump(records))
    return

records = getDNSResolution(names)
saveDNSResolution(records)

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
            saveDNSResolution(records)