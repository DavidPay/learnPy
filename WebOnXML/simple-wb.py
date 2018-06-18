#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-18-2018

from xml.sax import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler):
    #pass
    def startElement(self, name, attrs):
        print(name, attrs.keys())

    def endElement(self, name):
        print(name)

if '__main__' == __name__:
    parse('website.xml', TestHandler())