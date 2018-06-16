#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-15-2018

import socket

s = socket.socket()

host = socket.gethostname()
port = 10086
s.bind((host, port))

s.listen(5)
while True: 
    c, addr = s.accept() # , caution
    print("got connection from", addr)
    c.send("thanks,y".encode())
    c.close()