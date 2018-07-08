#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-17-2018

#learn from tutorials on web
import matplotlib.pyplot as plt
import sys
import numpy as np

#basic
def figure1():
    plt.plot([1,2,3,4])
    plt.ylabel('some number')
    plt.show()
#y is list, x is default [0,1,2,3]


def figure2():
    plt.plot([1,2,3,4],[1,4,9,16],'ro') 
    plt.axis([0, 6, 0, 20])
    plt.show()


def figure3():
    t = np.arange(0.,5.,0.2)
    plt.plot(t,t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()



if '__main__' == __name__: 
    import simple_pyplot
    fignum = input("which figure do you want to see?")  
    method = getattr(simple_pyplot, "figure"+fignum)
    method()

    '''
    >>> for func in func_list:
    locals()[func]()
foo
bar
 
>>> for func in func_list:
    globals()[func]()
foo
bar
    '''