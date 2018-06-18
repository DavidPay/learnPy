#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-18-2018
import os

testpath = 'testpath'

path12 = os.path.join(*[testpath])
if not os.path.isdir(path12):
    os.makedirs(path12)

#when i run python website.py, it's different in cmd mode and debug mode because the start path is different.
#so, i change the cwd in lauch.json like "cwd": "${fileDirname}"