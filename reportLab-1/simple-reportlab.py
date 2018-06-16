#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-16-2018

from reportlab.graphics.shapes import Drawing , String
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50, 50 , 'Hello World!', textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')