#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-15-2018
import socket
s = socket.socket()

host = socket.gethostname()
port = 10086+1

s.connect((host,port))
s.send("hello".encode())
print(s.recv(1024))