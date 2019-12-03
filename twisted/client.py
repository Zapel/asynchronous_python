# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 8007))
sock.send('hello, world!'.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print('received', data, len(data), 'bytes')