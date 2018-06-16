#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-16-2018

import sys , re
from handlers import *
from rulers import *
from util import *

class Parser:
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')

class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(TitleRule())
        self.addRule(ListItemRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', r"emphasis")
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)

'''
there left several problems:

1.powershell didn't support <(stdin) so i can use cmd: python makeup.py < thinking.txt > outtest.html
but can't use powershell

a: just enter cmd, the terminal will change to cmd. how to use powershell is another problem.

2.how to debug when not just using a single file but command lines

3.git in vscode
'''