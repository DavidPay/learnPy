#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import learnModule
import copy
#sys.path.append(".\..")
print(sys.path) 
print(dir(learnModule),'\n')

#__all__ is used for import xx 
test_dir_full = [n for n in dir(copy)] 
test_dir = [n for n in dir(copy) if not n.startswith('_')]
print('full_copy: ', test_dir_full,'\n')
print('simple_copy: ',test_dir,'\n')
print('__all__ _copy: ', copy.__all__, '\n')
#print(help(copy.copy),'\n')
#print(copy.__doc__,'\n')