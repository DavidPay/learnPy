#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-18-2018
import os

testpath = 'testpath'

path12 = os.path.join(*[testpath])
if not os.path.isdir(path12):
    os.makedirs(path12)