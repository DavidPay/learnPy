#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-17-2018

'''
there are some problems when i run this. But the important one is i should check the type!
not 2.x to 3.x problems, but type match problems.
very important in python so far.
'''

from urllib import request
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label

URL = "http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt"
COMMENT_CHARS = '#:' 


drawing = Drawing(400, 200)
data = []
for line in request.urlopen(URL).readlines():
    line = line.decode()
    #if not decode line = b'xxx', after decode line = 'xxx'
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        data.append([float(n) for n in line.split( )])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low =[row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
#lp.data = [zip(times, pred), zip(times, high), zip(times, low)]
#this can be used in 2.x, but in 3.x zip return an object ....
lp.data = [tuple(zip(times, pred)),tuple( zip(times, high)),tuple( zip(times, low))]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize=14, fillColor= colors.red))

renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspot')