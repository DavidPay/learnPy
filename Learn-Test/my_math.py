#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-15-2018

def my_square(x):
    '''
    >>> my_square(2)
    4
    >>> my_square(3)
    9
    '''
    return x**x

if __name__ =='__main__':
    import doctest, my_math
    doctest.testmod(my_math)