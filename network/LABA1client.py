#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
h = 'hello, world!'
h = bytes(h, encoding = "utf8")
print('отправил:',h)
sock.send(h)
data = sock.recv(1024)
sock.close()

print('принял:',data)