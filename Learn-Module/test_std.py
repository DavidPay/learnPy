#!/usr/bin/env python
# -*- coding: utf-8 -*-

#sys
import sys
args = sys.argv[1:]
args.reverse()
print('|'.join(args))
print(sys.platform)
#print(sys.modules)
print('------------sys-------------------\n')


#os
print('-------------os------------------\n')

#fileinput
'''
import fileinput

for line in fileinput.input(inplace = True):
    line = line.rstrip()
    num = fileinput.lineno()
    print(('%-40s # %2i' % (line, num)))
'''
print('--------------fileinput-----------------\n')

#set 
set_a = set(range(10))
print(set_a) #dic
print('----------------set---------------\n')

#time
import time
print(time.asctime())
print('----------------time---------------\n')

#random

#shelve

#re