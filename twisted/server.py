# -*- coding: utf-8 -*-

import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

data = conn.recv(1024)
print('client is at', addr, data)

conn.send(data)
# z = raw_input()
conn.close()

