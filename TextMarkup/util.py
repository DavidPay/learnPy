#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-15-2018

def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

            