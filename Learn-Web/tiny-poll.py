#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-15-2018
import socket , select

s = socket.socket()
host = socket.gethostname()
port = 10086
s.bind((host,port))

fdmap = {s.fileno():s}

s.listen(5) 

#not used for win32